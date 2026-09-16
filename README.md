# OpenScience research conversations

**Framework 2.2.0** prepares realistic research conversations and an external evidence/assessment workflow. Begin with a scientific question; develop a useful first investigation through native Plan first, execution and runtime auto-review; decide on extensions from the findings.

Status: **preparation release; no new live scientific validation claimed**. This repository contains skills, templates, prepared cases and historical preparation only. It contains no scientific run results or application patches.

## Start here

- [Framework and roles](docs/framework.md)
- [NHANES: smoking and depressive symptoms](cases/nhanes-2015-2016-smoking-phq9/START_Run_Case_with_Codex.md)
- [GBM: clinical-trial landscape](cases/gbm-clinical-trial-landscape/START_Run_Case_with_Codex.md)
- [Case2: longitudinal COVID-19 proteomics](cases/covid-haemodialysis-proteomics/START_Run_Case_with_Codex.md)
- [Case3: TCGA kidney-cancer survival](cases/tcga-kirc-stage-survival/START_Run_Case_with_Codex.md)
- [Case2/Case3 migration and local delivery](docs/case2-case3-migration.md)
- [Build case preparations](.agents/skills/building-openscience-cases/SKILL.md)
- [Operate and assess an authorized case](.agents/skills/openscience-human-review/SKILL.md)
- [Migration and installation](docs/migration.md)
- [Immutable preparation archive](archive/pre-conversation-20260916/README.md)
- [Validation and limitations](docs/validation.md)

Before each launch, assign who owns Plan approval, scope questions, extensions, recovery and acceptance. Record authority limits, budget and restart allowance. Preparing or installing these files does not launch a run.

Send only a case's `01_OpenScience_Prompt.md` and legitimate scientific context to OpenScience. Keep operating instructions and independent reference work outside the scientific workspace. Configure the current runtime/model through the installed application; this framework carries no machine-specific defaults.

## Maintain and validate

Python 3.10+ is sufficient; the repository scripts use the standard library. From the repository root:

```sh
python scripts/build_cases.py --check
python scripts/validate_preparation.py
python -m unittest discover -s tests -v
```

To regenerate after an intentional spec/template/reference edit, run `python scripts/build_cases.py` before checking. Case outputs include source hashes and protocol identities. Frozen archive bytes are never regenerated.

Historical release tags: `archive-pre-conversation-20260916` for the preparation baseline; `framework-v2.0.0` for the original conversation release. Report research usefulness, scientific validity, observed product features and Reproduction consistency separately. Consult [CHANGELOG](CHANGELOG.md) for the transition.

## Framework 2.2.0 update

The [collection upgrade](docs/collection-migration-2.2.0.md) adds explicit evidence folders, blank records and a portable validator to all four cases. Version 2.2.0 is identified by the framework-v2.2.0 tag; earlier release tags remain historical identities. Actual run evidence and delivery ZIPs remain outside this repository.
