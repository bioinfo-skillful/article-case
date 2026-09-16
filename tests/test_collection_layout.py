import json
import tempfile
import unittest
from pathlib import Path
from test_evidence import ev, SKILL


class LayoutTests(unittest.TestCase):
    def test_default_and_legacy_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            for layout in ('checkpoints', 'stages'):
                root = base / layout
                kwargs = {} if layout == 'checkpoints' else {'layout': layout}
                ev.initialize(root, SKILL / 'assets/evidence-template', base / 'science',
                              'case', 'protocol', 'attempt', **kwargs)
                obj = json.loads((root / 'manifest.json').read_text())
                self.assertEqual(obj['collection_layout'], layout)
                self.assertTrue(all((root / name).is_dir() for name in ev.LAYOUTS[layout]))
                self.assertTrue(ev.validate(root)['valid'])
                if layout == 'stages':
                    del obj['collection_layout']
                    ev.write_json(root / 'manifest.json', obj)
                    self.assertTrue(ev.validate(root)['valid'])

    def test_unknown_layout_and_missing_checkpoint(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            with self.assertRaises(ValueError):
                ev.initialize(base / 'bad', SKILL / 'assets/evidence-template', base / 'science',
                              'case', 'protocol', 'attempt', layout='invalid')
            root = base / 'good'
            ev.initialize(root, SKILL / 'assets/evidence-template', base / 'science',
                          'case', 'protocol', 'attempt')
            (root / 'CP6-reproduction-execution').rmdir()
            self.assertFalse(ev.validate(root)['valid'])
