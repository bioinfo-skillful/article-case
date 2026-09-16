"""Exercise integrity boundaries on temporary preparation copies, never live cases."""
from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_cases import build
from validate_preparation import validate


class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'repository'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv'))

    def tearDown(self):
        self.temp.cleanup()

    def test_release_is_self_consistent_and_check_mode_is_read_only(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = validate(self.root)
        self.assertTrue(result['ok'], result['errors'])
        self.assertEqual(build(self.root, check=True), [])
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_changed_archive_is_rejected(self):
        p = self.root / 'archive/pre-conversation-20260916/cases/nhanes-current/01_OpenScience_Prompt.md'
        p.write_bytes(p.read_bytes() + b'\nchanged\n')
        self.assertTrue(any('Archive bytes changed' in e for e in validate(self.root)['errors']))

    def test_case_source_identity_changes_require_manifest_refresh(self):
        case = self.root / 'cases/covid-haemodialysis-proteomics'
        source = case / 'sources/source-manifest.json'
        obj = json.loads(source.read_text(encoding='utf-8'))
        obj['files'][0]['sha256'] = '0' * 64
        source.write_text(json.dumps(obj), encoding='utf-8')
        self.assertTrue(any('Stale generated preparation' in e for e in validate(self.root)['errors']))
        build(self.root)
        manifest = json.loads((case / 'preparation-manifest.json').read_text(encoding='utf-8'))
        self.assertIn('sources/source-manifest.json', [f['path'] for f in manifest['files']])
        self.assertTrue(validate(self.root)['ok'])

    def test_old_case_snapshot_detected_and_generation_repairs_only_preparation(self):
        spec = self.root / 'cases/gbm-clinical-trial-landscape/case-spec.json'
        obj = json.loads(spec.read_text(encoding='utf-8'))
        obj['opening_message'] += ' Focus the first discussion on feasibility.'
        spec.write_text(json.dumps(obj), encoding='utf-8')
        self.assertTrue(any('Stale generated preparation' in e for e in validate(self.root)['errors']))
        old = {p.relative_to(self.root): p.read_bytes() for p in (self.root / 'archive').rglob('*') if p.is_file()}
        self.assertTrue(build(self.root))
        self.assertTrue(validate(self.root)['ok'])
        self.assertEqual(old, {p.relative_to(self.root): p.read_bytes() for p in (self.root / 'archive').rglob('*') if p.is_file()})

    def test_broken_active_link_is_rejected(self):
        with (self.root / 'README.md').open('a', encoding='utf-8') as f:
            f.write('\n[Missing](does-not-exist.md)\n')
        self.assertTrue(any('Broken/nonportable local link' in e for e in validate(self.root)['errors']))

    def test_runtime_results_cannot_enter_publication(self):
        p = self.root / 'cases/gbm-clinical-trial-landscape/run_099/results.json'
        p.parent.mkdir()
        p.write_text('{}', encoding='utf-8')
        self.assertTrue(any('Excluded runtime content' in e for e in validate(self.root)['errors']))

    def test_unfilled_generated_placeholder_is_rejected(self):
        p = self.root / 'cases/gbm-clinical-trial-landscape/01_OpenScience_Prompt.md'
        p.write_text('{{opening_message}}\n', encoding='utf-8')
        self.assertTrue(any('Unresolved active placeholder' in e for e in validate(self.root)['errors']))

    def test_active_chinese_text_is_rejected(self):
        p = self.root / 'docs/language-regression.md'
        p.write_text('\u8fd0\u884c\u6e05\u5355\n', encoding='utf-8')
        self.assertTrue(any('Non-English CJK' in e for e in validate(self.root)['errors']))

    def test_english_checklist_tampering_is_rejected(self):
        p = self.root / '.agents/skills/building-openscience-cases/references/OpenScience_Case_Checklist_Metrics_and_References_v0.2_EN.md'
        p.write_bytes(p.read_bytes() + b'\nUntracked edit\n')
        self.assertTrue(any('English checklist hash mismatch' in e for e in validate(self.root)['errors']))

    def test_potential_secret_is_reported_without_printing_value(self):
        fake = 'ghp_' + 'A' * 40
        (self.root / 'unintended.json').write_text(json.dumps({'token': fake}), encoding='utf-8')
        result = validate(self.root)
        self.assertTrue(any('Potential secret' in e for e in result['errors']))
        self.assertNotIn(fake, json.dumps(result))


if __name__ == '__main__':
    unittest.main()
