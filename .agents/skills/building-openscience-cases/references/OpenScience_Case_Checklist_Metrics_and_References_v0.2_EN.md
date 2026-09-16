# OpenScience case checklist, quantitative measures and references

English working edition of checklist v0.2 (source date: 2026-09-10). Prepared 2026-09-16. This edition restates the source in English, retaining its sections, evidence distinctions and numerical example; it is not the byte-identical original. Original identity and translation hash are recorded in [source-manifest.json](source-manifest.json). The unchanged source is retained in the repository archive.

**Status:** execution template; results remain unfilled. No case execution or product capability is established by this document. For conversation cases, the [operating contract](operating-contract.md) and [adaptation map](checklist-alignment.md) govern timing and applicability. The historical two-group, 12-marker, five-deliverable example below is not a requirement for NHANES, GBM or other cases.

Scope: one to three cases for a preprint's empirical evaluation of workflow, evidence retention, correctness, traceability/reproducibility and Reviewer quality. No independent benchmark is assumed. Any later benchmark must report its own tasks, conditions and scores.

Cases may start with a prompt alone; freeze user files only when supplied. The historical protocol uses Plan first: retain and assess the initial Plan, document human revisions and approval, then analyze. Report execution as conditional on that planning assistance; assess the initial Plan separately. CP0–CP7 are evidence checkpoints, not requests for additional product approval dialogs. Verify Reproduction interfaces against the tested release/commit.

The source mentions a separate workflow-design document v0.1 dated 2026-09-10; its contents and the full preprint were not supplied. Do not infer missing task parameters from that reference.

## Material passport

- Source: user-supplied v0.1 checklist, agent critique and user-confirmed revisions, assembled as v0.2.
- Source workflow: academic-research-suite / experiment-agent / plan.
- Verification status: preparation organized; case execution and experimental results unverified. Section 9 records the original literature-check scope, not a new literature review.

## 1. Evaluation scope and execution cover sheet

### 1.1 Claims and evidence

Declare intended case-level claims before CP0. Outcomes may support, partly support, contradict or leave a claim unresolved. Public product descriptions select what to examine; they do not replace runtime evidence.

| Intended claim | Direct evidence and assessment | Boundary |
|---|---|---|
| The initial Plan proposes reasonable, complete methods | Unedited `plan_v1` against prospectively frozen assessment criteria | Separate scientific validity, requirement coverage and proposed-workflow alignment |
| Outputs are correct within the checked scope after human-approved planning | Actual execution versus approved Plan; independent reference computation; numeric, visual and claim checks | Conditional human–agent performance, not autonomous end-to-end success |
| An exact artifact version is traceable to its generating process | Artifact ID/version/checksum linked to inputs, code, parameters and execution | Author-added links are not automatic product capture |
| Reviewer findings and corrections have valid grounds and version bindings | Original finding → exact target → external assessment → revision/rerun → re-review; check new errors | Without initial errors, detection and repair ability remain untested |
| The selected artifact's generating process can execute again | New process/kernel, actual execution, new outputs, field differences and conclusion comparison | Distinguish replay, code reconstruction and human recovery; errors can reproduce identically |
| Missing evidence is explicitly presented | Actual product `unavailable` states, gap details and any manual completion | No encountered gap means not observed, not universal gap detection |

The [OpenScience README](https://github.com/aipoch/open-science) motivates examination of immutable artifacts, provenance and version-scoped Reviewer evidence. Persistent kernels/projects are operating conditions; restart recovery needs its own test.

### 1.2 Case selection and limits

- Planned independent cases: ____ (1–3). Record IDs, tasks, selection rationale and desired coverage.
- Register all candidates and attempts before running. Later additions/removals require dates, reasons and whether results were already seen. Retain failures in the ledger.
- Case 01 may use the simulated two-group example. Other tasks require their own criteria and denominators; `12 × 5 = 60` does not transfer automatically.
- Retries, review rounds, replay attempts and injected-error probes are not independent cases. Repeated runs do not establish task diversity.
- Report case-specific feasibility and limitations. One to three cases do not estimate general success, Reviewer recall, or superiority over a coding agent.

### 1.3 Per-case cover sheet

| Field | Record |
|---|---|
| Identity | Case ID; main attempt ID; replay attempt ID; first attempt? |
| People | Operator; initial-Plan assessor; independent verifier; overlapping roles and involvement in revisions |
| Software | Date/time zone; product release/commit; Reproduction commit; agent/runtime and ACP adapter |
| Models | Execution model/provider/actual route; Reviewer model/provider |
| Environment | Platform; Python/R and packages; skills/specialists/configuration snapshot |
| Initial access | Prompt only or prompt/files; accessible project files, memory, sessions and network |
| Planning | Suggested workflow version; first and approved Plan versions; approval mechanism |
| Limits | Tools/network; total budget; Plan-revision, correction and replay/recovery limits |
| State | Not started / running / completed awaiting verification / partial / failed / stopped |

For each checklist item use done/not done/N/A with an evidence locator. Required but uncollected evidence is `missing`; N/A needs a reason. `unavailable` means a gap actually presented by the product. Missing historical snapshots must not be reconstructed as contemporaneous evidence.

Label sources **P** (product captured), **A** (agent generated), **H** (author/operator assembled). Split mixed sources, for example P execution log plus H claim index. Agent statements of success are not execution records. Carry labels into the result tables.

## 2. Chronological checklist

### CP0 — Freeze before execution

- [ ] Freeze the actual opening, deliverable commitments, parameters, environment, budget and stopping rules. Retain any disclosed method guidance in the input record.
- [ ] Preserve real attachments, origins/versions, SHA-256 and available data dictionaries. For prompt-only cases mark initial files N/A; do not manufacture CSV/code/seed attachments.
- [ ] Specify subsequent data generation/acquisition: responsible actor, allowed sources, structure, simulation parameters and randomness where applicable. Record when unspecified seeds will be selected; do not select by outcome.
- [ ] Freeze the author-side suggested workflow and initial-Plan criteria. Separate disclosed requirements from private preferences. Hidden preferences are not initial-Plan errors.
- [ ] Establish the reference method and independent self-check. With fixed inputs, reference values may be computed in advance; otherwise compute only after actual inputs are frozen and record the time.
- [ ] Keep reference code/values and author finding lists outside agent/Reviewer access. Record any exposure. Method suggestions through Plan feedback count as assistance.
- [ ] Define output fields, ID matching, tolerances, conclusion rules and claim slots prospectively. Replace the section 4 example for other tasks before seeing their results.
- [ ] Declare replay scope, data-regeneration inclusion, old-context/value visibility, dependency operations, recovery budget and any separate error probe.
- [ ] Enable available execution/time/usage records and an all-attempt ledger. Never overwrite prior attempts with debugging reruns.

Freeze only what exists at that time. Save newly formed data/code at first formation; do not call post-run material pre-frozen. In conversation mode, use the contract's stage-specific approval timing for detailed verification rules.

### CP1 — Assess, revise and approve the first Plan

- [ ] Submit through Plan first; define permitted preapproval input/metadata inspection. A method narrative written after analysis is not an initial Plan.
- [ ] Before feedback, save complete `plan_v1`, version, time and accessible context. Record missing Plans or premature execution as such.
- [ ] Complete and freeze the initial assessment before sending feedback. Later improvements do not change its historical assessment.
- [ ] Save each feedback message, Plan version, difference and rationale. Distinguish scientific corrections, omissions, workflow standardization and wording.
- [ ] Save the exact approval event, approver and `plan_approved`. Record review/approval time even if no revision was needed.
- [ ] Begin analysis after approval. Record justified method changes, renewed approval and affected steps; preserve reasonable deviations.

Initial-Plan quality and assisted execution are separate. Approval is a decision event; substantive method feedback is scientific help, not merely permission handling.

### CP2 — Inputs and initial analysis

- [ ] At first analytical use, retain exact generated/acquired data bytes, hashes, source, code/commands, actual parameters, seeds and environment; assess compliance with the task/Plan.
- [ ] Version later data changes and affected reruns. Correct calculations on invalid task data do not make the overall result correct.
- [ ] Preserve executed code and command/Notebook order, start/end, status and stdout/stderr or native equivalents.
- [ ] Save available pre-correction tables, figures, reports and checksums; distinguish data generation, analysis and file packaging.
- [ ] Compare actual design/methods/parameters/outputs with the approved Plan; retain installations, errors, retries and change reasons.
- [ ] If only post-review artifacts are exposed, record the missing initial snapshot rather than reconstructing one.

Distinguish writing code, executing it and summarizing it afterward. Generated inputs are not user attachments. Runtime auto-review may overlap CP2; conversation cases do not require an artificial globally unreviewed baseline.

### CP3 — Reviewer findings and revisions

- [ ] Save trigger, time, model, available prompts and actual file/context access; establish whether the approved Plan was accessible.
- [ ] Preserve each original finding, ID or H index, exact target version, grounds and state. Distinguish substantive errors, suggestions and insufficient evidence.
- [ ] Save before/after code/data/table/figure/report versions and actor. Data/numerical changes require associated rerun evidence.
- [ ] Save re-reviews and termination reasons, including no findings, no change, limits and errors.
- [ ] Independently assess findings, initial issues, repairs and introduced errors without supplying the answers to the Reviewer. If results are fed back, record scientific assistance and attribution.

Internal PASS is not scientific correctness. Missing before/after snapshots can make repair or new-error assessment impossible. With zero initial errors, the repair denominator is zero/N/A, not perfect detection or repair.

### CP4 — Freeze final original outputs and verify

- [ ] Freeze actual deliverables, artifact versions and hashes against the prospectively agreed content list.
- [ ] Link final data/input hashes, approved Plan, executed code and delivered scripts. Label reconstructed scripts and verify equivalence; they cannot replace execution records.
- [ ] Apply a validated independent reference to inputs, methods, structure, values and presentation. Report available initial and final checks separately.
- [ ] Assess claim presence, locatability and support separately. A link to incorrect code does not support a scientific claim.
- [ ] Select an exact replay target version and its generating inputs; do not use a moving latest-file reference.

Scientific correctness and replay agreement remain separate. An incorrect original may still be replay-tested with disclosure. Any subsequent scientific repair creates another version.

### CP5 — Start Reproduction

- [ ] Save request, frozen target, permitted materials, environment and context boundaries.
- [ ] Retain native identified inputs/code/parameters/dependencies/gaps and P/A/H labels, before and after any assistance.
- [ ] Use a new process/kernel and output directory where supported; record inherited session memory/variables and access to old result values.
- [ ] Distinguish same-machine/same-environment, same-machine/new-environment and different-machine tests. Describe actual isolation limits.
- [ ] Record each direct replay, reconstruction, automatic dependency action and human recovery. A later success does not replace a first failure.

For current conversation cases also retain native preview, declared frontier, actual steps, environment locks and gaps. A successful preview is not successful execution.

### CP6 — Complete replay and compare

- [ ] Retain actual execution from frozen analysis inputs to new outputs, code, status, native receipt/logs and new-file hashes. Check data-generation steps separately if included in the claim.
- [ ] For the historical example, check the exact 12 marker IDs, uniqueness, rows and group sample counts; classify duplicate/missing IDs as structural failures.
- [ ] Compare the five numeric fields separately (`x/12`), with optional total `x/60`; distinguish missing, nonfinite and outside-tolerance values.
- [ ] Preserve per-field differences, maximum absolute error, relative error for nonzero reference values and all 12 adjusted conclusion flags.
- [ ] Record path, assistance, timing, usage, termination and unresolved gaps for every attempt.

Agreement requires real re-execution, correct structure, required numbers within tolerance, and consistent sample counts/conclusions. Insufficient evidence is neither success nor a demonstrated numerical mismatch. Keep byte/content/scientific reports and actual replay-file retention separate.

### CP7 — Archive paper evidence

- [ ] Retain all cases/attempts and display-selection reasons. Report by case, not by treating cells as independent samples.
- [ ] Link figures/tables to exact files/versions; include P/A/H and missing/unavailable/N/A in results.
- [ ] Retain the first assessment, all feedback, approved Plan and later deviations; describe assistance conditions.
- [ ] Archive natural cases and optional probes separately; bound claims to observed case evidence where no benchmark exists.
- [ ] Remove credentials from sharing copies while retaining necessary method evidence. State untested contributions and failure modes; an author-assembled evidence package does not prove complete native capture.

## 3. Plan-first assessment and human alignment

### 3.1 Prospective suggested workflow

Historical CP0 workflow: source/generation → quality/preprocessing → study design/comparison direction → methods/parameters → multiplicity/conclusions → tables/figures/report → Reviewer → Reproduction. Document acceptable alternatives and parameters that must be standardized, with reasons. Different cases have their own workflows; protocol changes distinguish repeat attempts.

Judge initial defects against disclosed requirements and scientific validity. Private preferences may motivate later standardization but are not errors. A human-approved Plan still needs scientific checking. Conversation v2 replaces hidden workflow conformity with feasibility and question coverage.

### 3.2 Initial assessment table

| Criterion | Plan quote/locator | Scientific validity | Disclosed coverage | Workflow relationship | Proposed action/reason |
|---|---|---|---|---|---|
| Task, objective and input sources | ____ | ____ | ____ | ____ | ____ |
| Acquisition/generation, quality and preprocessing | ____ | ____ | ____ | ____ | ____ |
| Independent/paired or task-appropriate design and direction | ____ | ____ | ____ | ____ | ____ |
| Methods, assumptions and parameters | ____ | ____ | ____ | ____ | ____ |
| Multiplicity, thresholds and conclusion rules | ____ | ____ | ____ | ____ | ____ |
| Tables/figures/report and consistency checks | ____ | ____ | ____ | ____ | ____ |
| Execution evidence, review, replay and limits | ____ | ____ | ____ | ____ | ____ |

Validity: reasonable/error/insufficient information/N/A. Coverage: complete/partial/missing/N/A. Historical alignment: aligned/reasonable alternative/needs alignment/indeterminate/N/A. Provide item-level evidence; no weighted score. Record an absent first Plan as missing, not as its revised replacement.

### 3.3 Feedback and approval

| Event/time | Before/after versions | Feedback and actual change | Type | Active minutes | Approver/version | Evidence |
|---|---|---|---|---|---|---|
| ____ | ____ | ____ | Review/approval; scientific correction; omission; standardization; wording | ____ | ____ | ____ |

Execution conformity: applicable approved steps ____; followed ____; authorized deviation ____; unauthorized deviation ____; insufficient evidence ____. Freeze the denominator at approval. Do not remove failed steps; adherence is not scientific accuracy.

## 4. Correctness and deliverable assessment

This section preserves the historical two-group, 12-marker Case 01 example. Before running that example, specify actual columns, sample-count rules, test family, independent/paired design, sidedness, correction family/method and threshold including `<` versus `<=`. No omitted parameter is inferred here.

### 4.1 Five example deliverables

| Deliverable | Minimum content for completion |
|---|---|
| `analysis.py` | Readable executed implementation or executable reconstruction; inputs/outputs, preprocessing, direction, methods, correction, randomness and entry point; relationship to executed version |
| `results.csv` | All 12 unique expected markers, group effective sample counts, mean_A, mean_B, B−A, raw p, adjusted p and conclusion flags or declared equivalents; valid finite numeric cells, with precision limits disclosed |
| `comparison.png` | Opens legibly; A/B, markers, axes/units and direction identifiable; values match table; error bars/significance annotations defined and method-consistent |
| `report.md` | Task/source, design/methods, correction/threshold, main results and simulated-data limits; all five claim slots; referenced table/figure versions |
| `README.md` | File inventory, provenance/generation, dependencies, actual entry point/output location, necessary parameters/randomness and limitations |

Record satisfied/not satisfied/missing with reasons, reporting `x/5` only for this example. Completeness and scientific validity are separate. A different task uses its prospectively agreed denominator, not a relaxed post-failure denominator.

### 4.2 Five claim slots

| Slot | Complete assessment unit |
|---|---|
| Sample size | Both analyzed groups; all marker-specific n_A/n_B if missingness varies; valid-pair counts when paired |
| Direction | B−A or declared alternative; verify signs/groups for each marker summarized, not just formula wording |
| Test method | Family, design, sidedness and important parameters covering every actual method branch |
| Correction | Algorithm, corrected test family and threshold, aligned with actual code/table |
| Significance summary | One slot covering the full 12-marker adjusted classification; a subset alone is only partially present |

For each slot record presence (complete/partial/missing), locatability (complete/partial/not locatable), and support (supported/contradicted/indeterminate/missing).

Count a locatable slot only when fully present and supported by exact-version locators throughout. Partial coverage is not one full unit. Support requires evidence for the complete content; any substantive contradiction makes the slot contradicted. Incomplete content/evidence without an observed contradiction is indeterminate; no claim is missing. The four support counts sum to five. Attach all 12 significance classifications so aggregation cannot hide errors.

An accurate report of a wrong method can be supported as a description while still failing scientific method assessment.

### 4.3 Independent reference and original-result checks

Derive reference code independently from the task/approved methods and actual frozen inputs. Do not copy the evaluated implementation or fit reference answers to its results. Save at least one independent self-check: hand-checkable data/formulas/correction, or a separate implementation. Document coverage and shared dependencies; repeating the same library call is not fully independent verification.

For prompt-only cases, establish the reference method first; check generated data requirements and compute references after data freeze. Identical seeds do not guarantee identical data from different implementations. Verify both generation compliance and analysis of the actual data. An unvalidated author reference cannot establish PASS.

| Layer | Checks |
|---|---|
| Input/generation | Source, structure, sample design, simulation parameters/randomness and input-to-run version match |
| Methods/Plan | Scientific validity, task compliance, adherence or authorized deviations |
| Structure | IDs, rows, columns, counts, missing and abnormal values |
| Numbers/conclusions | Prospective fields/reference; establish comparability of alternative methods before declaring disagreement |
| Figures/report | Correct directions, labels, values and claims; simulations do not establish real biological discoveries |

States: pass/fail/not comparable/not assessed/insufficient evidence. Not comparable means a performed comparison cannot directly equate the methods; not assessed means no check; insufficient evidence means inadequate records. Overall, a confirmed error yields fail while retaining unresolved items; otherwise unresolved checks remain unresolved, then necessary incomparable values remain not comparable. Only all applicable checks passing permits PASS within the declared scope. Report initial/final versions separately; a reasonable alternative's different numbers are not automatically errors.

## 5. Reviewer quality — core per-case evidence

| Item | Operational record |
|---|---|
| Finding validity | Supported/unsupported/indeterminate, checked against original wording, correct basis and target version |
| Natural initial issues | Deduplicated author-confirmed issues, IDs, versions and external checking coverage; no recall estimate without exhaustive ground truth |
| Detection | Which known issues were/weren't identified; associate findings explicitly; claims limited to the known list |
| Repair | Repaired/unrepaired/indeterminate per issue; inspect changes, rerun and report; separate native-feedback repair, operator-assisted repair and direct author repair |
| Introduced errors | Verified issues absent before and present after, with version and attribution evidence; final PASS does not establish zero |
| Binding/re-review | Finding target, changed version and subsequent review; a same-name file path is not a version binding |

Repair may be reported `x/n` for known initial issues; n=0 is N/A. Keep assistance categories separate, not a combined autonomous repair rate. Missing before snapshots usually prevent initial/new-error judgments but do not preclude checking available findings and bindings.

### 5.1 Optional separate error probe

Register separately before execution; exclude from natural cases by default. With no natural errors, no probe means detection/repair was not tested, not proven by PASS.

- Derive a separate probe ID/copy from a frozen parent. Prespecify one error, such as reversed report direction or raw-p significance presented as adjusted-p significance on a fixed dataset where classifications differ. Do not repeatedly select cases to manufacture an effect.
- Preserve correct/error versions, injector/time, sole change and expected basis. Keep error location/answer out of Reviewer context; record actual access and prompt.
- Record detection, basis, repair and introduced errors. The unmodified case is descriptive context, not a matched benchmark baseline.
- Report probe time, injection and attempts separately. Do not merge with natural issue, deliverable or case counts. Conclusions are limited to this preset error.

## 6. Reproduction boundaries and consistency

### 6.1 Prespecify conditions, then verify actual access

| Condition | Historical default; disclose deviations |
|---|---|
| Generating materials | Exact original or generated frozen inputs, executed code, parameters, approved methods and necessary environment records; list versions/providers |
| Conversation/project | Prefer new session/process/kernel without hidden state; document required inherited memory, reports and tool outputs |
| Old target values | Prefer separate comparison after new outputs freeze; execution does not read old values or value-bearing reports/logs; target identity/schema may be supplied |
| Actual isolation | Check permissions/material access; asking not to look is not isolation. If accessible, disclose old-value availability and actual reads where observable |
| Dependencies | Within declared environment/network authority, record needed installations/retries. Missing fixed versions, method/code changes or exceeded budgets are deviations/reconstruction or stop conditions |
| Human recovery | Save unassisted failure first; bounded supplemental files/dependency/code help is separately recorded and attributed |
| Author answers | Keep reference code/values/checklists separate. Feeding differences back before a blind run ends invalidates that isolation claim |
| New outputs | Freeze new files/logs/hashes before independent comparison. Copying or hardcoding old answers is not re-execution |

Prompt-only initial input does not imply prompt-only replay. The default target is the recorded generating process with exact analysis inputs. Data regeneration needs an explicit scope, code/parameter/seed replay and regenerated-data comparison. Reusing data does not validate regeneration. Asking an LLM to freely solve the same opening again is a new task run, not automatically replay.

### 6.2 Record execution path separately from assistance

| Dimension | Values |
|---|---|
| Execution path | Direct recorded-code/order/parameter replay; or code reconstruction. Retain path/environment adaptation diffs and their logic impact too |
| Assistance | None; additional permission handling; environment recovery; supplementary materials; method/code help; allow multiple labels |
| Outcome | Agreement; execution failure; structural/numeric/conclusion disagreement; insufficient evidence; not run; record stop reason |

Direct replay failure followed by automatic reconstruction differs from direct replay succeeding after human dependency help. Reconstruction and human assistance can coexist.

### 6.3 Historical numeric rule

For the example only: `abs(new-old) <= 1e-10 + 1e-6*abs(old)` on expected finite, unrounded file values. NaN/Inf, missing and nonnumeric values do not count as matches. Disclose output rounding. The absolute term allows small near-zero differences; the relative term scales with magnitude. This is a prespecified operational tolerance, not equal relative precision or bit identity: old=`1e-12`, new=`1e-10` still passes. Any justified adjustment must precede observed differences.

| Field | Denominator | Matched | Outside tolerance | Missing/abnormal | Max absolute error | Max relative error (old ≠ 0) |
|---|---|---|---|---|---|---|
| mean_A | 12 | ____ | ____ | ____ | ____ | ____ |
| mean_B | 12 | ____ | ____ | ____ | ____ | ____ |
| B−A | 12 | ____ | ____ | ____ | ____ | ____ |
| Raw p | 12 | ____ | ____ | ____ | ____ | ____ |
| Adjusted p | 12 | ____ | ____ | ____ | ____ | ____ |
| Optional total | 60 | ____ | ____ | ____ | Keep field details | Keep field details |

The three outcome counts sum to 12 per field. Compute errors only on comparable finite values and state their count; none means N/A. Align exact marker IDs; duplicates are abnormal, not resolved by arbitrary row choice. Extra/missing IDs are structural failures. Marker sets and effective sample counts must match exactly. Check all adjusted flags against the frozen threshold/boundary and each output's own p values. In-tolerance values with changed conclusions still fail consistency. Shared original errors remain possible; original correctness is assessed separately.

## 7. Descriptive measures, time and intervention

Six basic measures supplement the core Plan and Reviewer records. These are case-level operational definitions, not validated scales or a weighted score.

| Measure | Interpretation |
|---|---|
| Completed deliverables | Example x/5 content satisfaction, not scientific accuracy |
| Locatable claims | Example x/5; report supported/contradicted/indeterminate/missing separately |
| Original verification | Initial/final layered scientific states and unresolved scope |
| Replay values | Per-field x/12 and optional x/60; separate structure/counts/conclusions/real-execution checks |
| Time | Event-defined wall time plus separate human active time; avoid overlapping sums |
| Intervention | Events/categories/actions/active minutes; distinguish approval from scientific help |

### 7.1 Events and intervals

Record zones. A phase not occurring is N/A; an uncollected required time is missing, never zero.

| Event | Definition |
|---|---|
| T0 | Full initial request submitted |
| T1 | First Plan ready for review |
| T2 | Execution Plan approved |
| T3 | Actual analysis starts |
| T4 | Initial pre-correction artifacts available, if observable |
| Rstart_i / Rend_i | Each review/correction interval |
| T5 | Final originals frozen after review settles or stops under declared rules |
| Vstart_i / Vend_i | Independent verification intervals |
| T6 | Replay request submitted |
| T7 | New outputs frozen or execution stops |
| T8 | Replay comparison ends |

Report original wall time T5−T0; planning T2−T0; approval wait/revision T2−T1; review intervals and their union; replay T7−T6; comparison T8−T7; verification intervals/active time. Failures end at actual termination. An entire-case duration is last necessary check/comparison minus T0 with the endpoint stated, not a sum of overlapping phases. Separate preparation, human wait and network wait. Prelaunch work is outside T5−T0. Missing snapshots may make corresponding timings missing.

### 7.2 Intervention ledger

| Event/stage/time | Category | Actual action | Versions/impact | Active minutes | Evidence |
|---|---|---|---|---|---|
| ____ | Permission / environment / Plan review-approval / scientific / presentation | ____ | ____ | ____ | ____ |

One continuous action for one purpose is one event with potentially multiple category labels; do not double-count its total. Distinct purposes/times are separate. The original request is not a correction. Distinguish formatting advice from statistical code edits. Avoid overlapping time for one person; sum multiple people as person-minutes with disclosure. Independent author evaluation is evaluation labor; feeding it back adds scientific assistance. Missing active time is not zero.

### 7.3 Optional usage and costs

Separate execution, review, replay and failed attempts. Record actual models, dated rates and billing units; avoid duplicate reasoning-token counts. If costs cannot be established, report observed usage only. Optional records include correction rounds, five dependency-category coverage and evidence-location effort. Without matched comparisons, do not claim efficiency or accuracy gains. Log lines, numeric cells and findings are not independent sample sizes.

## 8. Evidence organization and final tables

### 8.1 Retained materials

This is an author-side organization example, not a promise of native generation. Create contents only for actual evidence.

```text
case_ID/
  manifest.md                 # configuration, selection, versions, all attempts
  input/                      # opening and actual attachments
  planning/                   # first Plan, assessment, feedback, versions, approval
  data/                       # acquired/generated inputs, provenance and hashes
  initial/                    # available pre-correction code and outputs
  review/                     # findings, bindings, changes and re-reviews
  final/                      # frozen final originals
  reproduction/attempt_ID/    # scope, request, materials, execution, new outputs, logs
  verification/               # independent reference, self-check and assessments
  logs/                       # events, time, usage and intervention
  figures/                    # actual screenshots and version index
  probe/probe_ID/             # only authorized separate error probes
```

Keep private workflows, references, first assessments and probe answers outside execution-agent/Reviewer access. Logical folders may reside separately; this diagram grants no access.

Minimum event fields: `case_id, attempt_id, run_id, stage, event_id, timestamp, actor, action, status, input_refs, output_refs, evidence_path, capture_source`; record `parent_event_id` when available. Artifact refs carry native ID/version/checksum where available. Label H indexes explicitly; do not invent native IDs/tool payloads or collect inaccessible hidden reasoning.

Minimum attempt ledger: case/attempt ID, natural/replay/probe, start/end, configuration version, first attempt?, changes since failure, help, terminal state, display inclusion/reason. Preserve unassisted failures and assisted successes.

### 8.2 Per-case results

Use this main table with detailed section 3–6 records in supplementary material. Every row needs specific evidence/version and P/A/H or an explicit gap; split mixed sources.

| Category | Actual result to fill | Evidence/version | P/A/H and gaps |
|---|---|---|---|
| Product/model/environment/input type | ____ | ____ | ____ |
| All attempts and displayed selection | Count and rationale: ____ | ____ | ____ |
| Initial Plan | Item judgments, errors, omissions, alternatives: ____ | First Plan/assessment: ____ | ____ |
| Human planning/approval | Changes, approvals, scientific help, active time: ____ | Approved Plan/feedback: ____ | ____ |
| Execution versus Plan | Followed/authorized deviation/unauthorized deviation/insufficient evidence: ____ | ____ | ____ |
| Deliverables | ____ /5, or task-specific frozen denominator | ____ | ____ |
| Claims | Locatable ____ /5; supported/contradicted/indeterminate/missing: ____ | ____ | ____ |
| Initial/final correctness | Separate states, errors, incomparable/unresolved scope: ____ | Reference validation/differences: ____ | ____ |
| Reviewer finding basis/binding | Supported/unsupported/indeterminate and binding completeness: ____ | Finding → target: ____ | ____ |
| Reviewer repair | Known issues, native-agent/assisted/direct repairs, new errors: ____ | Changes/re-review: ____ | ____ or unassessable |
| Gap presentation | Actual unavailable states, undisplayed known gaps, manual completion; not observed if none | ____ | ____ |
| Replay boundary/path | Reused/regenerated data; old context/value visibility; replay/reconstruction/help: ____ | ____ | ____ |
| Actual re-execution | Evidence and first/final attempt outcomes: ____ | Process/kernel/log/new files: ____ | ____ |
| Numeric agreement | Per-field ____ /12, optional ____ /60; error details | ____ | ____ |
| Structure/conclusions | IDs/counts; ____ /12 conclusions; internal flag consistency | ____ | ____ |
| Time | Original/planning/review/replay/comparison/verification: ____ | Event ledger: ____ | ____ |
| Human intervention | Categories/actions/person-minutes; planning help separately: ____ | ____ | ____ |
| Optional usage/cost | ____ or missing | ____ | ____ |
| Claims and limitations | Section 1.1: supported/partial/unsupported/insufficient evidence | ____ | ____ |

An optional probe gets a separate table with parent version, injected error, detection, grounds, repair, new errors, assistance and sources; never merge its issues into natural counts.

### 8.3 One-to-three-case summary

| Case | Inputs/planning assistance | Correctness: initial → final | Traceability/replay | Reviewer | Main gaps/sources |
|---|---|---|---|---|---|
| Case 01 | ____ | ____ | ____ | ____ | ____ |
| Case 02, if run | ____ | ____ | ____ | ____ | ____ |
| Case 03, if run | ____ | ____ | ____ | ____ | ____ |

Remove unrun display rows with a candidate-ledger explanation. Do not add unlike denominators into overall accuracy. Present a system/case study with disclosed assistance and untested scope; later benchmarks support only their actual tested conditions.

## 9. References and applicability

The source reports checks dated 2026-09-10 of product descriptions and relevant abstracts/passages. This is not a new source verification, systematic full-text review or proof of OpenScience effectiveness.

| Primary source | Design relevance | Unsupported inference |
|---|---|---|
| Leo et al. *Recording provenance of workflow runs with RO-Crate.* PLOS ONE 19(9), e0309210 (2024). DOI 10.1371/journal.pone.0309210. [Article](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0309210) | Execution/input/output/code links in CP0/2/5/6 | No claim that OpenScience implements or conforms to RO-Crate |
| Sandve et al. *Ten Simple Rules for Reproducible Computational Research.* PLOS Computational Biology 9(10), e1003285 (2013). DOI 10.1371/journal.pcbi.1003285. [Article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285) | Steps, inputs, parameters, versions, randomness and executable workflows | Does not validate case denominators, tolerances or agent effectiveness |
| Schmidgall et al. *Agent Laboratory: Using LLM Agents as Research Assistants.* arXiv:2501.04227 (2025), cited arXiv version. [Paper](https://arxiv.org/abs/2501.04227) | Literature/experiment/report stages and human feedback | No inherited performance or cost result |
| *K-Dense Analyst: Towards Fully Automated Scientific Analysis.* arXiv:2508.07043v2 (2025), preprint. [Paper](https://arxiv.org/html/2508.07043v2) | Figure 2 planning/implementation loop as design context | No required role count or verification of OpenScience approval/Reviewer behavior |
| Gou et al. *CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing.* ICLR 2024; arXiv:2305.11738. [Paper](https://arxiv.org/abs/2305.11738) | Tool-supported critique, feedback and correction evidence | Internal PASS or feedback count is not correctness |
| Chen et al. *ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery.* ICLR 2025; arXiv:2410.05080. [Paper](https://arxiv.org/abs/2410.05080) | Executable scientific outputs and external task assessment | Cases are not that benchmark; 60 cells are not benchmark task accuracy |

The first two primarily support evidence/reproducibility design; others give workflow/evaluation context. Initial-Plan scoring, human alignment, x/5, x/12, x/60 and tolerance are prospectively declared operational choices, not literature-validated scales.

## 10. Paper methods wording — only after actual execution

> We evaluated [N] selected cases to examine workflow execution and evidence retention under a human-approved planning protocol. Inputs consisted of task prompts, with files included when applicable. We preserved and assessed the first agent-generated plan before human feedback, distinguishing scientific adequacy from alignment with a prespecified workflow. Human revisions and approval were documented before analysis, and subsequent results were interpreted as performance conditional on that assistance. We assessed artifact correctness, evidential traceability, Reviewer findings and revisions, and numerical agreement after re-executing the selected artifact's recorded generating process as separate dimensions. Reproduction inputs, context access, execution paths, and human remediation were documented. Evidence captured by the product, generated by agents, and assembled by authors was distinguished. These case-level observations do not estimate population-level performance or comparative gains.

Adapt wording to the actual conversation protocol. Add generated-data rules, freeze/reference times, old-value access, reused inputs, reconstruction and recovery where applicable. Report probe methods/results separately. Use completed tense only for completed operations; remove unsupported claims or mark missing. Replace [N] with the actual number of independent cases.
