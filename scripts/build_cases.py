"""Render preparation packages from case specs, templates and shared references.

Uses only the Python standard library. Writes only the five preparation documents,
their design-basis snapshots and manifest. It never launches or operates a case.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build(root=ROOT, check=False):
    config = json.loads((root / 'framework.json').read_text(encoding='utf-8'))
    skill = root / '.agents/skills/building-openscience-cases'
    templates = sorted((skill / 'assets/case-template').glob('*.md'))
    refs = sorted(p for p in (skill / 'references').iterdir() if p.is_file())
    collection = sorted(p for p in (skill / 'assets/evidence-template').rglob('*') if p.is_file())
    collector = skill / 'scripts/evidence.py'
    if len(templates) != 5:
        raise ValueError('Expected the five preparation templates')
    changes = []
    for case_id in config['cases']:
        case = root / 'cases' / case_id
        spec_path = case / 'case-spec.json'
        spec = json.loads(spec_path.read_text(encoding='utf-8'))
        spec['framework_version'] = config['version']
        outputs = {}
        # Case-local source records travel with the generated preparation and
        # are covered by its integrity manifest, without embedding run evidence.
        resources = sorted(p for p in (case / 'sources').rglob('*') if p.is_file())
        for resource in resources:
            outputs[resource.relative_to(case)] = resource.read_bytes()
        for template in templates:
            text = template.read_text(encoding='utf-8')
            def replacement(match):
                key = match.group(1)
                if key not in spec:
                    raise ValueError(f'Missing template value {case_id}: {key}')
                return spec[key]
            outputs[Path(template.name)] = re.sub(r'\{\{([a-z_]+)\}\}', replacement, text).encode('utf-8')
        for ref in refs:
            outputs[Path('design-basis') / ref.name] = ref.read_bytes()
        for resource in collection:
            outputs[Path('collection-template') / resource.relative_to(skill / 'assets/evidence-template')] = resource.read_bytes()
        outputs[Path('collection-tools/evidence.py')] = collector.read_bytes()
        manifest = {
            'case_id': case_id, 'protocol_id': spec['protocol_id'],
            'framework_version': config['version'], 'status': 'prepared_not_live_validated',
            'prepared_date': config['release_date'],
            'inputs': [{'source_relative_path': p.relative_to(root).as_posix(),
                        'sha256': digest(p.read_bytes())} for p in [spec_path, *templates, *refs, *resources, *collection, collector]],
            'files': [{'path': path.as_posix(), 'bytes': len(data), 'sha256': digest(data)}
                      for path, data in sorted(outputs.items())],
        }
        outputs[Path('preparation-manifest.json')] = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        for relative, data in outputs.items():
            dest = case / relative
            if not dest.exists() or dest.read_bytes() != data:
                changes.append(dest.relative_to(root).as_posix())
                if not check:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(data)
    return changes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report stale/missing preparation without writing')
    args = parser.parse_args()
    changed = build(check=args.check)
    print(json.dumps({'mode': 'check' if args.check else 'write', 'changed_files': changed}, indent=2))
    raise SystemExit(1 if args.check and changed else 0)
