import sys
import json
import hashlib
import unittest
from pathlib import Path
from test_evidence import EvidenceTests, ev, ROOT

sys.path.insert(0, str(ROOT / 'scripts'))
from migrate_collection import migrate, mapped_path


class MigrationTests(EvidenceTests):
    def test_copy_preserves_source_identity_bytes_and_times(self):
        self.complete_fixture()
        before = {p.relative_to(self.root).as_posix(): p.read_bytes()
                  for p in self.root.rglob('*') if p.is_file()}
        dest = self.base / 'migrated'
        migrate(self.root, dest)
        self.assertTrue(ev.validate(dest, 'final-handoff')['handoff_ready'])
        for rel, data in before.items():
            self.assertEqual((self.root / rel).read_bytes(), data)
            self.assertEqual((dest / mapped_path(rel)).read_bytes(), data)
        source_rows = [json.loads(s) for s in (self.root / 'evidence-index.jsonl').read_text().splitlines()]
        new_rows = [json.loads(s) for s in (dest / 'evidence-index.jsonl').read_text().splitlines()]
        for old, new in zip(source_rows, new_rows):
            for key in ('evidence_id', 'captured_at', 'event_time', 'sha256'):
                self.assertEqual(old[key], new[key])
        with self.assertRaises(ValueError):
            migrate(self.root, dest)

    def test_tampered_source_rejected_before_copy(self):
        self.complete_fixture()
        (self.root / '00-setup/fixture.md').write_text('changed')
        dest = self.base / 'migrated'
        with self.assertRaises(ValueError):
            migrate(self.root, dest)
        self.assertFalse(dest.exists())

    def test_prospective_contract_routes_to_plan(self):
        self.assertEqual(mapped_path('04-scientific-assessment/assessment-frozen-v1.md'),
                         'CP1-plan/assessment-frozen-v1.md')
