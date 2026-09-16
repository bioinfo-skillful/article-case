"""Verify an extracted focused review bundle; standard library, no network."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

from build_cases import build

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    expected = {}
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        path = (root / name).resolve()
        if not path.is_relative_to(root.resolve()):
            errors.append('Unsafe checksum path')
            continue
        expected[name] = digest
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f'Missing or changed: {name}')
    files = [p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    actual = {p.relative_to(root).as_posix() for p in files} - {'SHA256SUMS.txt'}
    if actual != set(expected):
        errors.append('Unexpected or missing bundle files')
    links = 0
    for p in files:
        name = p.relative_to(root).as_posix()
        if any(part in {'human_records', 'node_modules', '.git'} or re.fullmatch(r'run_\d+', part)
               for part in p.relative_to(root).parts):
            errors.append(f'Unexpected runtime content: {name}')
        if p.suffix == '.md' and 'assets/case-template/' not in name:
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
                if re.match(r'(?:https?://|mailto:|#)', target):
                    continue
                target = unquote(target.split('#', 1)[0].strip('<>'))
                if target:
                    links += 1
                    dest = (p.parent / target).resolve()
                    if not dest.is_relative_to(root.resolve()) or not dest.exists():
                        errors.append(f'Broken link: {name} -> {target}')
    errors.extend(f'Stale preparation: {p}' for p in build(root, check=True))
    return dict(ok=not errors, files_checked=len(files), local_links_checked=links, errors=errors)


if __name__ == '__main__':
    result = validate()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['ok'] else 1)
