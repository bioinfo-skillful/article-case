"""Initialize and validate external case evidence. Python 3.10+, no dependencies."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re
import shutil

STAGE_FOLDERS = ('00-setup', '01-plan', '02-execution', '03-review',
           '04-scientific-assessment', '05-reproduction', 'deliverables', 'logs')
CHECKPOINT_FOLDERS = ('CP0-setup', 'CP1-plan', 'CP2-execution', 'CP3-review',
    'CP4-assessment', 'CP5-reproduction-preview', 'CP6-reproduction-execution',
    'CP7-archive', 'deliverables', 'logs')
LAYOUTS = {'checkpoints': CHECKPOINT_FOLDERS, 'stages': STAGE_FOLDERS}
FOLDERS = CHECKPOINT_FOLDERS
ROOT_FILES = ('README.md', 'REPORT.md', 'HANDOFF.md', 'evidence-index.jsonl',
              'manifest.json', 'interventions.jsonl')
REQUIREMENTS = (
    'setup', 'submission', 'questions-and-decisions', 'initial-plan',
    'plan-revisions-and-approval', 'prospective-assessment', 'inputs',
    'notebook-executions', 'artifact-provenance', 'reviews-and-corrections',
    'first-and-final-delivery', 'scientific-assessment', 'reproduction-target',
    'reproduction-preview-and-locks', 'reproduction-receipt-and-logs',
    'reproduction-outputs-and-comparisons', 'native-logs', 'terminal-state',
    'intervention-accounting')
AVAILABILITY = {'captured', 'missing', 'unavailable', 'not_generated',
                'not_retained', 'not_applicable', 'insufficient_evidence'}
CATEGORIES = {'plan-feedback', 'scope-answer', 'approval', 'permission',
              'extension', 'environment', 'recovery-prompt', 'scientific-assistance',
              'acceptance', 'stop'}
TERMINAL = {'completed', 'failed', 'stopped', 'not_started', 'unavailable'}


def stamp():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))


def timestamp(value):
    if not isinstance(value, str):
        return False
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).utcoffset() is not None
    except ValueError:
        return False


def safe_path(root, value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError('Path must be a nonempty portable relative path')
    parts = value.split('/')
    if any(p in {'', '.', '..'} for p in parts) or PurePosixPath(value).is_absolute():
        raise ValueError('Unsafe relative path')
    path = root.joinpath(*parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path escapes evidence root')
    if any(p.is_symlink() for p in [path, *path.parents] if p.is_relative_to(root)):
        raise ValueError('Evidence paths cannot use symlinks')
    return path


def inventory(root):
    entries = []
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Evidence inventory contains a symlink')
        if path.is_file() and path != root / 'manifest.json':
            data = path.read_bytes()
            entries.append(dict(path=path.relative_to(root).as_posix(), bytes=len(data),
                                sha256=hashlib.sha256(data).hexdigest()))
    return entries


def seal(root):
    """Refresh file inventory only; never infer collection status or native evidence."""
    path = root / 'manifest.json'
    obj = json.loads(path.read_text(encoding='utf-8'))
    obj['files'] = inventory(root)
    obj['updated_at'] = stamp()
    write_json(path, obj)


def initialize(root, template, scientific_root, case_id, protocol_id, attempt_id,
               layout='checkpoints'):
    if layout not in LAYOUTS:
        raise ValueError('Unknown collection layout')
    root, template, scientific_root = root.resolve(), template.resolve(), scientific_root.resolve()
    if root.exists():
        raise ValueError('Use a new evidence directory; existing evidence is never overwritten')
    if root.is_relative_to(scientific_root) or scientific_root.is_relative_to(root):
        raise ValueError('Scientific and evidence locations must be separate')
    if root.is_relative_to(template) or any((p / 'framework.json').is_file() for p in root.parents):
        raise ValueError('Evidence must be outside the preparation repository/package')
    for filename in ROOT_FILES:
        if not (template / filename).is_file():
            raise ValueError(f'Missing template: {filename}')
    shutil.copytree(template, root)
    for folder in LAYOUTS[layout]:
        (root / folder).mkdir(exist_ok=True)
    obj = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
    obj.update(case_id=case_id, protocol_id=protocol_id, attempt_id=attempt_id,
               collection_layout=layout)
    obj['stages'] = [dict(stage_id='stage-1', requirements=[
        dict(id=name, status='pending', evidence_ids=[], reason='') for name in REQUIREMENTS])]
    write_json(root / 'manifest.json', obj)
    seal(root)


def validate(root, mode='in-progress'):
    root = root.resolve()
    errors, gaps = [], []
    def error(message):
        errors.append(message)
    def load(path):
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            error(f'Cannot read JSON {path.name}: {type(exc).__name__}')
            return None
    for name in ROOT_FILES:
        if not (root / name).is_file():
            error(f'Missing required file: {name}')
    manifest = load(root / 'manifest.json')
    if not isinstance(manifest, dict):
        return dict(valid=False, collection_complete=False, handoff_ready=False,
                    validation_errors=errors or ['Manifest must be an object'], collection_gaps=gaps)
    layout = manifest.get('collection_layout', 'stages')
    if layout not in LAYOUTS:
        error('Unknown collection_layout')
    for name in LAYOUTS.get(layout, ()):
        if not (root / name).is_dir():
            error(f'Missing required directory: {name}')
    if manifest.get('schema_version') != 1:
        error('Unsupported manifest schema_version')
    for key in ('case_id', 'protocol_id', 'attempt_id'):
        if not isinstance(manifest.get(key), str) or not manifest[key].strip():
            error(f'Missing identity: {key}')
    if not timestamp(manifest.get('updated_at')):
        error('Manifest updated_at must include a timezone')
    stage_rows = manifest.get('stages')
    if not isinstance(stage_rows, list) or not stage_rows:
        error('Manifest requires at least one stage')
        stage_rows = []
    stages = set()
    for stage in stage_rows:
        sid = stage.get('stage_id') if isinstance(stage, dict) else None
        if not isinstance(sid, str) or not sid or sid in stages:
            error('Missing or duplicate stage_id')
        else:
            stages.add(sid)
    indexed = {}
    files = manifest.get('files')
    if not isinstance(files, list):
        error('Manifest files must be an array')
        files = []
    for item in files:
        if not isinstance(item, dict):
            error('Invalid manifest file record')
            continue
        name = item.get('path')
        try:
            path = safe_path(root, name)
        except ValueError as exc:
            error(f'Unsafe manifest path: {exc}')
            continue
        if name == 'manifest.json' or name in indexed:
            error(f'Self-reference or duplicate manifest path: {name}')
        indexed[name] = item
        if not path.is_file():
            error(f'Listed file missing: {name}')
        elif item.get('bytes') != path.stat().st_size or item.get('sha256') != hashlib.sha256(path.read_bytes()).hexdigest():
            error(f'File size/hash mismatch: {name}')
    try:
        actual = {p['path'] for p in inventory(root)}
        for name in sorted(actual - set(indexed)):
            error(f'Unlisted file: {name}')
    except ValueError as exc:
        error(str(exc))
    def rows(filename):
        try:
            lines = (root / filename).read_text(encoding='utf-8').splitlines()
        except (OSError, UnicodeError):
            return []
        result = []
        for number, line in enumerate(lines, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError()
                result.append(row)
            except ValueError:
                error(f'Invalid JSON object: {filename}:{number}')
        return result
    evidence = {}
    for row in rows('evidence-index.jsonl'):
        eid = row.get('evidence_id')
        if not isinstance(eid, str) or not eid or eid in evidence:
            error('Missing or duplicate evidence_id')
            continue
        evidence[eid] = row
        required = {'stage_id', 'attempt_id', 'session_id', 'source', 'checkpoint',
                    'event_time', 'captured_at', 'archived_at', 'native_ids', 'versions',
                    'source_locator', 'collection_method', 'path', 'availability',
                    'reason', 'bytes', 'sha256'}
        if required - row.keys():
            error(f'Missing evidence fields: {eid}: {sorted(required - row.keys())}')
        if row.get('stage_id') not in stages or row.get('attempt_id') != manifest.get('attempt_id'):
            error(f'Wrong evidence stage/attempt: {eid}')
        if row.get('source') not in {'P', 'A', 'H'} or row.get('checkpoint') not in {f'CP{i}' for i in range(8)}:
            error(f'Invalid evidence source/checkpoint: {eid}')
        if not isinstance(row.get('native_ids'), dict) or not isinstance(row.get('versions'), list):
            error(f'Invalid native IDs/versions: {eid}')
        if row.get('session_id') is not None and not isinstance(row['session_id'], str):
            error(f'Invalid session ID: {eid}')
        for key in ('event_time', 'captured_at', 'archived_at'):
            if row.get(key) is not None and not timestamp(row[key]):
                error(f'Invalid timezone timestamp: {eid}/{key}')
        state = row.get('availability')
        if state not in AVAILABILITY:
            error(f'Invalid availability: {eid}')
        if state == 'captured':
            name = row.get('path')
            try:
                safe_path(root, name)
            except ValueError:
                error(f'Unsafe evidence path: {eid}')
                name = None
            if name not in indexed:
                error(f'Evidence path absent from manifest: {eid}')
            elif any(row.get(k) != indexed[name].get(k) for k in ('bytes', 'sha256')):
                error(f'Evidence size/hash disagrees with manifest: {eid}')
            for key in ('source_locator', 'collection_method'):
                if not isinstance(row.get(key), str) or not row[key].strip():
                    error(f'Missing capture field: {eid}/{key}')
            if not timestamp(row.get('captured_at')) or not timestamp(row.get('archived_at')):
                error(f'Captured evidence needs capture/archive times: {eid}')
            if row.get('event_time') is None and not row.get('reason'):
                error(f'Unknown event time requires explanation: {eid}')
        else:
            if not row.get('reason'):
                error(f'Absent evidence needs reason: {eid}')
            if any(row.get(k) is not None for k in ('path', 'bytes', 'sha256')):
                error(f'Absent evidence cannot claim file bytes: {eid}')
            if state != 'not_applicable':
                gaps.append(dict(evidence_id=eid, status=state, reason=row.get('reason')))
    for stage in stage_rows:
        if not isinstance(stage, dict):
            continue
        requirements = stage.get('requirements')
        if not isinstance(requirements, list):
            error('Stage requirements must be an array')
            continue
        seen = set()
        for item in requirements:
            if not isinstance(item, dict):
                error('Invalid requirement record')
                continue
            name, state = item.get('id'), item.get('status')
            if not isinstance(name, str) or name in seen:
                error('Missing or duplicate requirement ID')
                continue
            seen.add(name)
            if state not in AVAILABILITY | {'pending'}:
                error(f'Invalid requirement status: {name}')
            refs = item.get('evidence_ids')
            if not isinstance(refs, list) or not all(isinstance(x, str) for x in refs):
                error(f'Invalid evidence references: {name}')
                refs = []
            for eid in refs:
                if eid not in evidence or evidence[eid].get('stage_id') != stage.get('stage_id'):
                    error(f'Broken or cross-stage evidence reference: {name}/{eid}')
            if state == 'captured' and (not refs or any(evidence.get(eid, {}).get('availability') != 'captured' for eid in refs)):
                error(f'Captured requirement needs captured evidence: {name}')
            if state not in {'captured', 'pending'} and not item.get('reason'):
                error(f'Requirement needs absence/applicability reason: {name}')
            if state not in {'captured', 'not_applicable'}:
                gaps.append(dict(stage_id=stage.get('stage_id'), requirement=name,
                                 status=state, reason=item.get('reason')))
        for name in sorted(set(REQUIREMENTS) - seen):
            error(f'Missing collection requirement: {stage.get("stage_id")}/{name}')
    interventions = set()
    for row in rows('interventions.jsonl'):
        iid = row.get('intervention_id')
        if not isinstance(iid, str) or not iid or iid in interventions:
            error('Missing or duplicate intervention_id')
            continue
        interventions.add(iid)
        required = {'stage_id', 'attempt_id', 'time', 'category', 'actor', 'action',
                    'authority_basis', 'evidence_ids'}
        if required - row.keys():
            error(f'Missing intervention fields: {iid}: {sorted(required - row.keys())}')
        if row.get('stage_id') not in stages or row.get('attempt_id') != manifest.get('attempt_id'):
            error(f'Wrong intervention stage/attempt: {iid}')
        if row.get('category') not in CATEGORIES or (row.get('time') is not None and not timestamp(row.get('time'))):
            error(f'Invalid intervention category/time: {iid}')
        if row.get('time') is None and not row.get('reason'):
            error(f'Unknown intervention time needs reason: {iid}')
        for key in ('actor', 'action', 'authority_basis'):
            if not isinstance(row.get(key), str) or not row[key].strip():
                error(f'Missing intervention field: {iid}/{key}')
        refs = row.get('evidence_ids')
        if not isinstance(refs, list) or not refs or any(not isinstance(e, str) or e not in evidence for e in refs):
            error(f'Broken intervention evidence references: {iid}')
    handoff = manifest.get('handoff')
    if not isinstance(handoff, dict):
        error('Missing structured handoff')
        handoff = {}
    if mode == 'final-handoff':
        if manifest.get('collection_origin') not in {'contemporaneous', 'retrospective'}:
            error('Final handoff needs explicit collection_origin')
        for key in ('execution', 'review', 'correction'):
            if handoff.get(key) not in TERMINAL:
                error(f'Unfinished or unknown handoff state: {key}')
        if handoff.get('status') not in {'settled', 'blocked', 'stopped'}:
            error('Final handoff status must be settled, blocked or stopped')
        for key in ('summary', 'next_action', 'remaining_budget'):
            if not isinstance(handoff.get(key), str) or not handoff[key].strip():
                error(f'Final handoff needs {key}')
        if not isinstance(handoff.get('pending_decisions'), list):
            error('Handoff pending_decisions must be an array')
        if handoff.get('status') == 'settled' and handoff.get('pending_decisions'):
            error('Settled handoff cannot have pending decisions')
        if not timestamp(handoff.get('checked_at')):
            error('Final handoff needs timestamped state check')
        for filename in ('README.md', 'REPORT.md', 'HANDOFF.md'):
            try:
                if 'UNFILLED' in (root / filename).read_text(encoding='utf-8'):
                    error(f'Unfinished handoff document: {filename}')
            except OSError:
                pass
    pending = any(g.get('status') == 'pending' for g in gaps)
    return dict(valid=not errors, collection_complete=not errors and not gaps,
                handoff_ready=mode == 'final-handoff' and not errors and not pending,
                validation_errors=errors, collection_gaps=gaps,
                limits='Structure/integrity only; does not establish scientific or Reproduction success.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    init = sub.add_parser('init')
    init.add_argument('--layout', choices=tuple(LAYOUTS), default='checkpoints')
    for name in ('root', 'template', 'scientific-root', 'case-id', 'protocol-id', 'attempt-id'):
        init.add_argument('--' + name, required=True)
    refresh = sub.add_parser('inventory')
    refresh.add_argument('--root', required=True)
    check = sub.add_parser('validate')
    check.add_argument('--root', required=True)
    check.add_argument('--mode', choices=('in-progress', 'final-handoff'), default='in-progress')
    args = parser.parse_args()
    try:
        root = Path(args.root).resolve()
        if args.command == 'init':
            initialize(root, Path(args.template), Path(args.scientific_root),
                       args.case_id, args.protocol_id, args.attempt_id, args.layout)
        elif args.command == 'inventory':
            seal(root)
        else:
            result = validate(root, args.mode)
            print(json.dumps(result, indent=2))
            return 1 if not result['valid'] else (2 if args.mode == 'final-handoff' and not result['handoff_ready'] else 0)
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({'validation_errors': [str(exc)]}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
