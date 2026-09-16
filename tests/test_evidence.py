"""Synthetic validator fixtures only; no live scientific evidence is generated."""
from pathlib import Path
import importlib.util
import json
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents/skills/building-openscience-cases'
spec = importlib.util.spec_from_file_location('evidence_tool', SKILL / 'scripts/evidence.py')
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.root = self.base / 'evidence'
        ev.initialize(self.root, SKILL / 'assets/evidence-template', self.base / 'science',
                      'fixture-case', 'fixture-protocol', 'fixture-attempt')

    def tearDown(self):
        self.temp.cleanup()

    def manifest(self):
        return json.loads((self.root / 'manifest.json').read_text())

    def write(self, obj):
        ev.write_json(self.root / 'manifest.json', obj)

    def append(self, filename, row):
        with (self.root / filename).open('a', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(row) + '\n')

    def complete_fixture(self):
        # A single fixture file tests relationships, not scientific adequacy.
        p = self.root / '00-setup/fixture.md'
        p.write_text('Synthetic unit-test evidence only.', encoding='utf-8')
        ev.seal(self.root)
        item = next(x for x in self.manifest()['files'] if x['path'] == '00-setup/fixture.md')
        row = dict(evidence_id='fixture-1', stage_id='stage-1', attempt_id='fixture-attempt',
                   session_id=None, source='H', checkpoint='CP0', event_time=ev.stamp(),
                   captured_at=ev.stamp(), archived_at=ev.stamp(), native_ids={}, versions=[],
                   source_locator='synthetic unit test', collection_method='unit-test fixture',
                   availability='captured', reason='No native session in this synthetic test', **item)
        self.append('evidence-index.jsonl', row)
        obj = self.manifest()
        obj['collection_origin'] = 'contemporaneous'
        for r in obj['stages'][0]['requirements']:
            r.update(status='captured', evidence_ids=['fixture-1'])
        obj['handoff'].update(status='settled', execution='completed', review='completed',
                              correction='not_started', checked_at=ev.stamp(),
                              summary='Synthetic fixture only', next_action='None', remaining_budget='0')
        self.write(obj)
        for name in ('README.md', 'REPORT.md', 'HANDOFF.md'):
            (self.root / name).write_text('Synthetic completed document.', encoding='utf-8')
        ev.seal(self.root)
        return row

    def test_initialization_is_pending_and_does_not_create_native_evidence(self):
        report = ev.validate(self.root)
        self.assertTrue(report['valid'], report)
        self.assertFalse(report['collection_complete'])
        self.assertEqual((self.root / 'evidence-index.jsonl').read_bytes(), b'')
        self.assertEqual(len(report['collection_gaps']), len(ev.REQUIREMENTS))

    def test_complete_read_only_validation(self):
        self.complete_fixture()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        report = ev.validate(self.root, 'final-handoff')
        self.assertTrue(report['handoff_ready'], report)
        self.assertTrue(report['collection_complete'])
        self.assertEqual(before, {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_unavailable_evidence_is_gap_not_integrity_error(self):
        self.complete_fixture()
        obj = self.manifest()
        obj['stages'][0]['requirements'][-3].update(status='unavailable', evidence_ids=[], reason='Native export unavailable')
        self.write(obj)
        report = ev.validate(self.root, 'final-handoff')
        self.assertTrue(report['handoff_ready'], report)
        self.assertFalse(report['collection_complete'])
        self.assertTrue(report['collection_gaps'])

    def test_missing_file_and_altered_bytes(self):
        self.complete_fixture()
        p = self.root / '00-setup/fixture.md'
        p.write_text('Changed', encoding='utf-8')
        self.assertTrue(any('hash mismatch' in e for e in ev.validate(self.root)['validation_errors']))
        p.unlink()
        self.assertTrue(any('Listed file missing' in e for e in ev.validate(self.root)['validation_errors']))

    def test_duplicate_evidence_and_broken_references(self):
        row = self.complete_fixture()
        self.append('evidence-index.jsonl', row)
        obj = self.manifest()
        obj['stages'][0]['requirements'][0]['evidence_ids'] = ['nonexistent']
        self.write(obj)
        ev.seal(self.root)
        errors = ev.validate(self.root)['validation_errors']
        self.assertTrue(any('duplicate evidence_id' in e for e in errors))
        self.assertTrue(any('Broken or cross-stage' in e for e in errors))

    def test_unsafe_paths(self):
        self.complete_fixture()
        for path in ('../escape', '/absolute', 'C' + ':/escape', 'a\\b', 'a/./b'):
            with self.subTest(path=path):
                obj = self.manifest()
                obj['files'][0]['path'] = path
                self.write(obj)
                self.assertTrue(any('Unsafe manifest path' in e for e in ev.validate(self.root)['validation_errors']))

    def test_unfinished_handoff_and_pending_accounting(self):
        self.complete_fixture()
        obj = self.manifest()
        obj['handoff']['review'] = 'running'
        self.write(obj)
        self.assertFalse(ev.validate(self.root, 'final-handoff')['valid'])
        obj['handoff']['review'] = 'completed'
        obj['stages'][0]['requirements'][0]['status'] = 'pending'
        self.write(obj)
        report = ev.validate(self.root, 'final-handoff')
        self.assertTrue(report['valid'])
        self.assertFalse(report['handoff_ready'])

    def test_intervention_duplicate_and_bad_reference(self):
        self.complete_fixture()
        row = dict(intervention_id='operator-1', stage_id='stage-1', attempt_id='fixture-attempt',
                   time=ev.stamp(), category='approval', actor='operator', action='Fixture approval',
                   authority_basis='Fixture only', evidence_ids=['not-found'])
        self.append('interventions.jsonl', row)
        self.append('interventions.jsonl', row)
        ev.seal(self.root)
        errors = ev.validate(self.root)['validation_errors']
        self.assertTrue(any('Broken intervention' in e for e in errors))
        self.assertTrue(any('duplicate intervention_id' in e for e in errors))

    def test_missing_record_fields_and_timezone(self):
        self.complete_fixture()
        p = self.root / 'evidence-index.jsonl'
        row = json.loads(p.read_text())
        del row['collection_method']
        row['captured_at'] = '2026-09-16T12:00:00'
        p.write_text(json.dumps(row)+'\n', encoding='utf-8')
        ev.seal(self.root)
        errors = ev.validate(self.root)['validation_errors']
        self.assertTrue(any('Missing evidence fields' in e for e in errors))
        self.assertTrue(any('Invalid timezone' in e for e in errors))

    def test_initialization_refuses_existing_and_nested_roots(self):
        with self.assertRaises(ValueError):
            ev.initialize(self.root, SKILL / 'assets/evidence-template', self.base / 'science', 'c', 'p', 'a')
        with self.assertRaises(ValueError):
            ev.initialize(self.base / 'science/inside', SKILL / 'assets/evidence-template', self.base / 'science', 'c', 'p', 'a')

    def test_absence_record_cannot_fabricate_file(self):
        row = self.complete_fixture()
        row.update(evidence_id='absence', availability='not_generated', reason='Replay blocked')
        self.append('evidence-index.jsonl', row)
        ev.seal(self.root)
        self.assertTrue(any('cannot claim file bytes' in e for e in ev.validate(self.root)['validation_errors']))
