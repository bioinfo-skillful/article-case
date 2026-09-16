"""Validate preparation integrity and publication boundaries without running cases."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote

from build_cases import build

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [
    re.compile(r'gh[pousr]_[A-Za-z0-9]{30,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{40,}'),
    re.compile(r'sk-(?:proj-)?[A-Za-z0-9_-]{35,}'),
    re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repo_files(root):
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and not any(part in {'.git', '__pycache__', '.venv'} for part in p.relative_to(root).parts))


def validate(root=ROOT):
    errors = []
    files = repo_files(root)
    config = json.loads((root / 'framework.json').read_text(encoding='utf-8'))
    archive = root / config['archive']
    manifest = json.loads((archive / 'manifest.json').read_text(encoding='utf-8'))
    expected_archive = {'README.md', 'manifest.json'}
    for item in manifest['files']:
        expected_archive.add(item['archive_path'])
        p = archive / item['archive_path']
        if not p.is_file() or sha(p) != item['sha256'] or p.stat().st_size != item['bytes']:
            errors.append(f'Archive bytes changed/missing: {item["archive_path"]}')
    actual_archive = {p.relative_to(archive).as_posix() for p in files if p.is_relative_to(archive)}
    if actual_archive != expected_archive:
        errors.append('Archive inventory differs from its frozen manifest')
    try:
        stale = build(root, check=True)
        errors.extend(f'Stale generated preparation: {p}' for p in stale)
    except (ValueError, KeyError, FileNotFoundError) as exc:
        errors.append(f'Case generation check: {exc}')

    source_manifest = json.loads((root / '.agents/skills/building-openscience-cases/references/source-manifest.json').read_text(encoding='utf-8'))
    original = root / source_manifest['archive_source_relative_path']
    if sha(original) != source_manifest['original_sha256'] or sha(original) != config['master_checklist_sha256']:
        errors.append('Archived original checklist hash mismatch')
    english_name = source_manifest['file']
    links = 0
    archive_historical = 0
    for p in files:
        relative = p.relative_to(root)
        rel = relative.as_posix()
        if p.is_symlink():
            errors.append(f'Publication contains a symlink: {rel}')
        if any(re.fullmatch(r'run_\d+', part) or part in {'human_records', 'runtime-evidence', 'node_modules'} for part in relative.parts):
            errors.append(f'Excluded runtime content present: {rel}')
        if p.suffix.lower() not in {'.md', '.json', '.jsonl', '.yaml', '.py'} and p.name not in {'.gitignore', '.gitattributes'}:
            errors.append(f'Unexpected publication file type: {rel}')
        if p.name.startswith('.env') or p.name in {'web-token', 'credentials.json'}:
            errors.append(f'Credential file present: {rel}')
        text = p.read_text(encoding='utf-8')
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            errors.append(f'Potential secret detected: {rel}')
        if p.is_relative_to(archive):
            archive_historical += 1
            continue
        if re.search(r'[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]', rel + text):
            errors.append(f'Non-English CJK text or filename in active file: {rel}')
        if p.name == english_name and sha(p) != source_manifest['sha256']:
            errors.append(f'English checklist hash mismatch: {rel}')
        if re.search(r'(?<![A-Za-z])[A-Za-z]:[\\/]', text) or re.search(r'/(?:home|Users)/[A-Za-z0-9_-]+/', text):
            errors.append(f'Machine-specific path in active file: {rel}')
        template = 'assets/case-template' in rel
        if not template and p.suffix in {'.md', '.json', '.yaml'} and re.search(r'\{\{[a-z_]+\}\}', text):
            errors.append(f'Unresolved active placeholder: {rel}')
        if p.suffix == '.md' and not template:
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if re.match(r'(?:https?://|mailto:|#)', target):
                    continue
                target = unquote(target.split('#', 1)[0].strip('<>'))
                if not target:
                    continue
                links += 1
                resolved = (p.parent / target).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(f'Broken/nonportable local link: {rel} -> {target}')
    for skill in config['skills']:
        p = root / '.agents/skills' / skill / 'SKILL.md'
        text = p.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            errors.append(f'Invalid skill frontmatter: {skill}')
            continue
        front = text.split('---', 2)[1]
        if not re.search(rf'^name: {re.escape(skill)}$', front, re.M) or not re.search(r'^description: .+', front, re.M):
            errors.append(f'Invalid skill name/description: {skill}')
        if f'version: "{config["version"]}"' not in front:
            errors.append(f'Skill version differs from framework: {skill}')
    return {'ok': not errors, 'files_checked': len(files), 'archive_files_checked': archive_historical,
            'local_links_checked': links, 'cases_checked': len(config['cases']), 'errors': errors}


if __name__ == '__main__':
    try:
        report = validate()
    except (ValueError, KeyError, FileNotFoundError, UnicodeError) as exc:
        report = {'ok': False, 'errors': [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report['ok'] else 1)
