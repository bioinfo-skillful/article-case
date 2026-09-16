# Evidence collection contract

Framework 2.1.0. Read before initializing an attempt, collecting an event, resuming work or handing it off. The [collection matrix](evidence-collection.md) defines evidence meaning and the [operating contract](operating-contract.md) defines authority. This document fixes storage and minimum accounting. Directories group records; execution and review can overlap.

## Initialize outside preparation and science

Each generated case includes `collection-template/` and `collection-tools/evidence.py`. Python 3.10+ and the standard library are sufficient. From a case directory, initialize a new external root using actual case/protocol/attempt values:

```sh
python collection-tools/evidence.py init --template collection-template --root /external-evidence/NHANES-attempt-1 --scientific-root /scientific-work/NHANES-attempt-1 --case-id nhanes-2015-2016-smoking-phq9 --protocol-id nhanes-smoking-phq9-conversation-v2.1.0 --attempt-id attempt-1
```

The paths above are portable examples, not configured locations. Select actual separate locations under the user's authority. Initialization refuses existing roots and nested scientific/evidence paths. It creates empty indices, unfilled human documents, directories and pending collection requirements; it creates no scientific/native evidence. Runtime permission and actual filesystem access must still be checked. The installed building skill contains the same tool under `scripts/` and templates under `assets/evidence-template/`.

```text
attempt/
  README.md
  REPORT.md
  HANDOFF.md
  evidence-index.jsonl
  interventions.jsonl
  manifest.json
  00-setup/
  01-plan/
  02-execution/
  03-review/
  04-scientific-assessment/
  05-reproduction/
  deliverables/
  logs/
```

## Minimum contents and collection timing

Each manifest stage must account for all requirement IDs below, using captured evidence or an explicit absence/applicability status. This is a minimum accounting list, not a fixed scientific-output quota.

| Requirement IDs | Storage and minimum record | Native/source entrance and time |
|---|---|---|
| setup | 00-setup: actual opening/context, attachments, case/protocol identity, authority, budget, version/models/runtime/permissions and capture readiness | User decisions, installed settings, real input files; before submission |
| submission | 00-setup: persisted message/session identity and Plan-first intent | Native UI/export/verified API; immediately after send |
| questions-and-decisions | 01-plan: question text, actual submitted answers, decision owner and acceptance | Current question cards and persisted response; on every question |
| initial-plan | 01-plan: complete initial version and first validity/coverage/feasibility assessment | Native Plan/version export or snapshot; before feedback |
| plan-revisions-and-approval | 01-plan: every feedback/revision and exact-version approval/read-back | Native Plan and conversation records; on change/approval |
| prospective-assessment | 04-scientific-assessment: assessment contract, bound Plan version and freeze time | External operator decision; before inspecting estimates |
| inputs | 02-execution: real input bytes, URLs/acquisition metadata and identities | Actual native/input files; first use and changes |
| notebook-executions | 02-execution: code/order/parameters, dependencies, outcomes and stdout/stderr | Native Notebook execution/export; as executions settle |
| artifact-provenance | 02-execution: native input/run/artifact-version relationships and publication/preview state | Native artifact/provenance records; formation and changes |
| reviews-and-corrections | 03-review: every available scope, finding, response, modification, rerun, re-review and end reason | Native auto-review/correction records; each observed event |
| first-and-final-delivery | deliverables: first-complete and final original bytes/versions; unretained earlier versions stated | Genuine artifact export/files; first completion and settlement |
| scientific-assessment | 04-scientific-assessment: independent checker, its self-check, detailed comparisons and limits | External assessment of frozen commitments and real outputs; after stage settlement |
| reproduction-target | 05-reproduction: exact target version, frontier, scope and comparison policy | Native target plus prospective external decision; before replay |
| reproduction-preview-and-locks | 05-reproduction: preview, recipe/steps, environment locks and gaps | Native Reproduction preview; before execution |
| reproduction-receipt-and-logs | 05-reproduction: actual receipt/status, executed steps and logs, or explicit no-execution reason | Native operation; success or failure, never inferred from preview |
| reproduction-outputs-and-comparisons | 05-reproduction: genuine new outputs/identities and raw byte/content/scientific comparisons separately | Native replay result/export; at completion; missing levels remain explicit |
| native-logs | logs: relevant native snapshots/extracts with original location, times, session coverage and redaction | Discover installed log location; capture errors immediately and collect relevant intervals at handoff |
| terminal-state | HANDOFF plus phase-local evidence: execution/review/correction state and pending decisions | Native state read-back; at settlement or stop |
| intervention-accounting | interventions index plus original action evidence | Operator/user actions and authority; when performed; empty ledger needs explicit no-intervention accounting |

Name versioned records by stage and real ID, for example `01-plan/stage-1/plan-VERSION.json`, `03-review/stage-1/REVIEW-ID/`, and `05-reproduction/stage-1/replay-1/`. Save screenshots in the corresponding event directory with timezone-bearing timestamps or an index mapping. Keep original and annotated/redacted copies separate. Export filenames may differ by product; retain originals and map them in the index rather than inventing native files.

Keep raw logs in one canonical location and reference them from events. A report or screenshot complements raw evidence; it cannot replace missing Notebook runs, Plan versions or receipts. Index actual coverage, truncation, missing inputs and failed reads. Save captured subsets even when a requirement as a whole is incomplete.

## Record formats

`evidence-index.jsonl` is append-only, one JSON object per observation. Required fields:

```json
{"evidence_id":null,"stage_id":null,"attempt_id":null,"session_id":null,"source":null,"checkpoint":null,"event_time":null,"captured_at":null,"archived_at":null,"native_ids":{},"versions":[],"source_locator":null,"collection_method":null,"path":null,"availability":null,"reason":null,"bytes":null,"sha256":null}
```

This is a blank shape, not an event to insert. Assign unique operator evidence IDs; use actual native IDs only when available. Source is P/A/H; checkpoint is CP0-CP7. Timestamps use ISO 8601 with timezone. `event_time` may be null with an explanation; captured evidence needs actual capture/archive times, a source locator and method. Session IDs may be null for unavailable/unbound evidence, with limitations explained. Capture time is not the original event time. Paths use forward slashes, stay inside the evidence root, and cannot use parent traversal, drive paths or symlinks.

Availability: captured, missing, unavailable, not_generated, not_retained, not_applicable or insufficient_evidence. Captured records have path/size/SHA-256 matching the manifest. Other states have null path/size/hash and a reason; use separate captured records for partial supporting files. To correct a mistaken index entry, append an explicitly explained corrective observation; preserve the original and reference the appropriate IDs in the current stage accounting.

`interventions.jsonl` records `intervention_id`, `stage_id`, `attempt_id`, timezone-bearing `time` (or null with `reason` when unknown), `category`, `actor`, exact `action` or its retained locator, `authority_basis`, and nonempty `evidence_ids`. Categories: plan-feedback, scope-answer, approval, permission, extension, environment, recovery-prompt, scientific-assistance, acceptance, stop. Native automatic corrections belong in review evidence, not the operator ledger. Original failed outcomes remain retained after intervention.

`manifest.json` records schema/framework/case/protocol/attempt identity, inventory update time, collection origin, stage accounting and current structured handoff. Each stage has a unique `stage_id` and all required category IDs with `status`, `evidence_ids` and `reason`. New stages receive their own accounting; shared setup may be referenced by a new stage-specific capture/index observation with disclosed reuse. `pending` is allowed only while still awaiting accounting. A captured requirement must link captured evidence in that stage. Use an absence state for incomplete required coverage even if some files exist; a reason must identify what is missing.

The file inventory has path/bytes/SHA-256 for every retained file except manifest.json itself. Hashes bind bytes, not truth or publisher identity. Before refreshing inventory, validate the prior snapshot and investigate unexpected changes. The explicit inventory command records the new snapshot; it does not approve changed science or change evidence-row hashes/statuses. Preserve meaningful old file versions and manifest snapshots under a phase-local snapshot directory before intentional replacement.

## Validate and hand off

```sh
python collection-tools/evidence.py inventory --root /external-evidence/NHANES-attempt-1
python collection-tools/evidence.py validate --root /external-evidence/NHANES-attempt-1 --mode in-progress
python collection-tools/evidence.py validate --root /external-evidence/NHANES-attempt-1 --mode final-handoff
```

Run in-progress checks after meaningful captures and before resuming; run final-handoff after updating REPORT/HANDOFF and terminal-state evidence. If saving validator output into the root, refresh its inventory afterward. Validation is read-only; initialization and inventory updates are explicit writes.

`validation_errors` are structural/integrity defects (bad records, paths, hashes, references, duplicate IDs, unfinished final handoff). `collection_gaps` describe pending/missing/unavailable evidence. `valid` means no structural errors. `collection_complete` requires no gaps; N/A needs an applicability reason. `handoff_ready` allows transparently documented gaps but no pending accounting or unknown/active execution, review or correction state. Final statuses are settled, blocked or stopped. Pending decisions require blocked/stopped status and an explicit next action. None of these fields rates scientific validity or replay success.

Exit codes: 0 structurally valid (and final handoff ready when requested); 1 validation error; 2 structurally valid final accounting still pending. Always read gaps, even at exit 0. Meaning, completeness of an apparently captured review history, scientific claims and screenshot adequacy require human/operator assessment; the tool cannot prove them from filenames.

For retrospective reorganization, preserve original bytes and collection times where known. Record current organization/archive times separately, keep historical protocol identity, and label unverified terminal states and absent records. Do not backdate a prospective assessment or fabricate native IDs/receipts to pass validation. A useful archive may legitimately remain incomplete or not handoff-ready.
