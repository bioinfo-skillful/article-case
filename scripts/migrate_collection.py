"""Copy a legacy collection into checkpoint layout without modifying source bytes.

No application access or scientific execution. Review mixed-record mappings and
checkpoint coverage manually; this tool does not infer scientific completion.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('collection_tool', ROOT / '.agents/skills/building-openscience-cases/scripts/evidence.py')
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)
PREFIXES = dict(zip(ev.STAGE_FOLDERS[:5], ev.CHECKPOINT_FOLDERS[:5]))
PREFIXES['05-reproduction'] = 'CP5-reproduction-preview'


def mapped_path(rel):
    parts = Path(rel).parts
    if len(parts) == 1:
        return 'CP7-archive/original-records/' + rel
    name = parts[-1].lower()
    if parts[0] == '04-scientific-assessment' and ('frozen' in name or 'contract' in name):
        return '/'.join(('CP1-plan', *parts[1:]))
    return '/'.join((PREFIXES.get(parts[0], parts[0]), *parts[1:]))


def migrate(source, dest):
    source, dest = Path(source).resolve(), Path(dest).resolve()
    if dest.exists() or dest.is_relative_to(source) or source.is_relative_to(dest):
        raise ValueError('Destination must be new and separate from source')
    validation = ev.validate(source, 'final-handoff')
    if not validation['valid']:
        raise ValueError('Source integrity validation failed: ' + str(validation['validation_errors']))
    original = json.loads((source / 'manifest.json').read_text(encoding='utf-8'))
    if original.get('collection_layout', 'stages') != 'stages':
        raise ValueError('Expected legacy stages source')
    stamp = ev.stamp()
    mappings, targets = [], set()
    for p in sorted(source.rglob('*')):
        if p.is_symlink():
            raise ValueError('Source symlinks are not supported')
        if not p.is_file():
            continue
        rel = p.relative_to(source).as_posix()
        target = mapped_path(rel)
        ev.safe_path(dest, target)
        if target in targets:
            raise ValueError('Destination mapping collision: ' + target)
        targets.add(target)
        mappings.append(dict(source_path=rel, destination_path=target,
                             bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    dest.mkdir(parents=True)
    for folder in ev.CHECKPOINT_FOLDERS:
        (dest / folder).mkdir(exist_ok=True)
    for item in mappings:
        target = dest / item['destination_path']
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((source / item['source_path']).read_bytes())
        if hashlib.sha256(target.read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('Copied bytes changed')
    pathmap = {row['source_path']: row['destination_path'] for row in mappings}
    records = []
    for line in (source / 'evidence-index.jsonl').read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get('path'):
            row['original_path'] = row['path']
            row['path'] = pathmap[row['path']]
        row['reorganized_at'] = stamp
        records.append(row)
    (dest / 'evidence-index.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in records), encoding='utf-8')
    (dest / 'interventions.jsonl').write_bytes((source / 'interventions.jsonl').read_bytes())
    obj = dict(original)
    obj.update(collection_layout='checkpoints', collection_framework_version='2.2.0',
               source_collection_framework_version=original.get('framework_version'),
               collection_origin='retrospective', reorganized_at=stamp)
    # framework_version/protocol_id describe historical records and remain unchanged.
    ev.write_json(dest / 'manifest.json', obj)
    ev.write_json(dest / 'CP7-archive/migration-map.json', dict(
        reorganized_at=stamp, source_root=str(source), files=mappings,
        identity_policy='Historical attempt/protocol/framework identities unchanged; collection framework 2.2.0.',
        original_links='Original document bytes retained. Resolve old embedded paths using this map.'))
    ev.write_json(dest / 'CP7-archive/source-validation.json', validation)
    for name in ('README.md', 'REPORT.md', 'HANDOFF.md'):
        text = (source / name).read_text(encoding='utf-8')
        (dest / name).write_text('# Retrospective checkpoint collection\n\n'
            'Collection framework 2.2.0. No rerun or new native review. Historical outcome text follows; '
            'its old paths resolve through CP7-archive/migration-map.json. Original documents remain byte-identical '
            'in CP7-archive/original-records. Prior terminal observations were not freshly rechecked.\n\n' + text, encoding='utf-8')
    ev.seal(dest)
    return dest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--destination', required=True)
    args = parser.parse_args()
    print(migrate(args.source, args.destination))
