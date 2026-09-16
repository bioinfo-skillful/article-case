# NHANES_2015_2016_SMOKING_PHQ9: Post-run Collection Prompt

Act as **Human Review** for `D:\case_all\case1_NHANES`, attempt `run_001`. Read START, 03, 04 and the master checklist in the design-basis directory. Collect only materials from the registered workspace/session. Preserve source files. Do not restart scientific analysis, overwrite failures or initial versions, or send this document to OpenScience.

1. Verify registration, actual paths and termination state. If sources are still changing, make only a timestamped partial collection. Inspect prior collections first; do not overwrite historical packages.
2. After first-run science and autoReview end, freeze `delivery_final`. Retain actual inputs, every available Plan and approval, original data and sources, code/configuration, native historical versions, autoReview feedback/scope/changes/rechecks, execution logs and existing reproduction evidence. Verify copy hashes and record source/destination paths. Do not invent native IDs.
3. Collect the completed human record sheet and real screenshot index. Mark missing transient screenshots, initial versions or initial assessments as `missing`. Never infer them from final outputs. Later examination of existing files must carry its actual time and version.
4. Complete supported independent checks, fixed sampling and ambiguity checks under 04. Save reference self-validation, differences, evidence and conclusions. Self-reported success, rerunning the evaluated code and a product pass are not independent correctness evidence. Use `not evaluated` or `insufficient evidence` where appropriate. Label external work Human Review.
5. Freeze the independent final-issue list first, then associate all available autoReview history and calculate the four evaluation groups in 04. Residual issues may be detected but unresolved or newly introduced; they are not automatically misses. Final files alone cannot prove repairs. Keep product verdicts unchanged and separately report blocked checks, unobservable reads and missing history.
6. Consolidate events, all attempts, sources and time. Collect tokens only from reliable native fields tied to this session/round. Separate execution, autoReview, reproduction and failures. Deduplicate cumulative snapshots versus increments and respect cached/reasoning-token field relationships. When separation is unreliable, retain raw values and limits; do not estimate invented costs or collect hidden reasoning.
7. Produce a timestamped evidence package and index. Redact credentials only in distributable copies, preserving necessary scientific context and the original logs securely. Retain unsuccessful attempts and reasons for paper selection. Report only the verified scope.

## Collection layout

Use `human_records/run_001/collection_<timestamp>/`, creating content only when it actually exists:

```text
manifest.md
input/
planning/
data/
initial/                    # Genuine historical versions only
review/
final/
reproduction/attempt_ID/
verification/
logs/
figures/
probe/probe_ID/              # Only if separately enabled and executed
```

The manifest records case/attempt/session, source mapping, versions/hashes, selection reasons, gaps and collection times. Large data may use fixed verified references; an offline package must contain the required data, not unusable local paths.

Keep evidence origins distinct: P = product-captured; A = OpenScience-generated; H = Human Review organization. A native log is P; its external index is H. Human-added relationships do not demonstrate native provenance. Distinguish `missing`, product-displayed `unavailable`, and justified `N/A`.

Minimum event fields: case_id, attempt_id, run_id, stage, event_id, timestamp, actor, action, status, input_refs, output_refs, evidence_path, capture_source; retain parent_event_id when available. Attempt records include type, start/end, configuration, first-attempt status, changes, assistance, termination and paper selection/reason.

## Outputs

- File inventory/checksums, missing-material list, canonical screenshot index and complete attempt/event records.
- `verification/case_results.md`: every result item in 04 and master section 8.2, including Plan, approvals/help, execution deviations, delivery completeness, claim traceability/support, initial/final correctness, autoReview scope/effects, reproduction, time, interventions, optional usage and supported claims.
- `review/finding_ledger.csv`, `verification/issue_ledger.csv`, `verification/autoreview_metrics.md`: original findings, deduplicated issues and four evaluation groups with denominators, unresolved counts and coverage; include reference self-validation and differences.
- An evidence archive and checksum when suitable. Complete files do not imply correct results.

## Existing record locations

`human_records/run_001` contains header-only events.csv, screenshots.csv, attempts.csv, human_actions.csv, finding_ledger.csv, issue_ledger.csv and missing_materials.csv. These are blank forms, not evidence that events occurred. Use their columns or lossless equivalents. Archive the canonical screenshot index rather than creating competing indexes.

The proposed scientific directory is `run_001/science_workspace`; until verified, use the registered actual source path. Freeze originals at `human_records/run_001/collection_<timestamp>/final/delivery_final` with per-file SHA-256. Repeated collections use new timestamps; preserve differing versions and reasons. Never move or clean OpenScience originals.

Locate three XPTs, code, configuration, analysis_data, cohort_flow, missingness, prevalence, models, both figures, report and README. Apply 04's twelve-category completeness denominator. Preserve actual native artifacts, versions, generating edges and displayed gaps; create external H indexes separately. Directory structure does not prove captured dependencies.
