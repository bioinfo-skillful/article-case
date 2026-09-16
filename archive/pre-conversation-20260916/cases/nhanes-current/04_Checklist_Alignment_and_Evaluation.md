# NHANES_2015_2016_SMOKING_PHQ9: External Verification and Evaluation

For **Human Review** only. Do not submit to OpenScience or autoReview. The unchanged master checklist v0.2 is in the design-basis directory; its checksum is in source-manifest.json. This English edition preserves the scientific design and evaluation rules. All run results remain unrecorded.

The September 12, 2026 protocol enables dynamic autoReview from the first submission, freezes outputs after natural checks end, and evaluates them externally. CP2 uses genuine native history where available rather than a human pause/handoff. Missing history remains missing. The separate internal Reviewer for frozen artifacts is excluded. The preserved master is not rewritten.

## A. Case and prespecified rules

Scientific design version 1.0, prepared September 12, 2026; not executed. Analyze smoking status and depressive symptoms in adults aged 18–79 using three NHANES 2015–2016 public files. The public K-Dense example uses 2017–2018 diabetes/physical activity; this case changes cycle, theme, exposure, outcome, age scope and core files while retaining survey-weighted descriptions and regression. The shared session body could not be retrieved; comparison is based on its public case description, not a verified round-by-round transcript.

No results for this new case have been inspected or predetermined. Do not claim a novel medical association or replay a paper's design and conclusions. Public scientific requirements are 01's Scientific specification items 1–7 and Required outputs. Freeze reference methods at CP0 and calculate reference values only after actual XPT inputs are frozen. The independent reference implementation is not yet written or validated; do not prefill success.

Delivery completeness is x/12, using the twelve bullet categories in 01. Original data plus documentation count as one; both figures and vector copies count as one; the executable and required source files count as one. Each category must meet all its required content. Correctness is separate.

Required table structures: prevalence = two outcomes times four groups = eight rows; models = three models times two contrasts = six rows. Retain unestimable rows with reasons. IDs, counts, cases, categories and inclusion flags require exact agreement. Unestimable values cannot count as finite numeric agreement.

For comparable methods, compare prevalence, SE, lower CI and upper CI at eight positions each; beta, SE, OR, lower CI, upper CI and p at six positions each; Holm p at two positions. For each field report matching, different, unestimable and missing positions against its fixed denominator. Do not pool cells into task accuracy. Use `abs(test-ref) <= 1e-8 + 1e-5*abs(ref)` with probabilities on the 0–1 scale. This is a study-specific operational tolerance, not a validated scale. Investigate reasonable differences in estimand, df or CI convention before calling results wrong or incomparable; never loosen tolerance after seeing differences. Compare both Holm decisions and reported directions exactly; flag threshold crossings separately.

Six fixed claim slots: population/inclusion counts; smoking/PHQ definitions; survey design/estimation; primary prevalence and uncertainty; adjusted associations/multiplicity; sensitivity and causal/diagnostic limitations. Assess presence, locatability and support independently. Fully locatable x/6; supported/contradicted/indeterminate/absent counts sum to six.

Use 03's fixed sample, supplemented by full-data independent checks. Group ambiguities by rule type; the 30-person inspection cap cannot hide known errors. Severity: major (changes population, estimates or inference), minor (local scientific error), and non-error suggestion. Never change the case based on significance or autoReview performance. Budgets are in START; preserve all failed attempts.

Map each judgment to 01's public requirements or scientific validity. Hidden preferences are not errors. External tolerances are evaluation tools, not undisclosed scientific instructions. Report item statuses and x/n, without a weighted total score or inherited denominators from other cases.

Evidence: P = product-captured; A = OpenScience-generated; H = external Human Review organization. Split mixed sources. Preserve original evidence. `missing` means required but not retained; `unavailable` requires an actual product-displayed gap; `N/A` needs an applicability reason. External blocked judgments are not invented product gap labels.

## B. Master-checklist alignment

| Master location | Case implementation | Boundary |
|---|---|---|
| Section 1, CP0 | A, START, attempt ledger | Prespecify claims/conditions; retain failures |
| Section 3, CP1 | Original Plan, assessment, feedback, approval | Three axes; no external administration imposed on Plan |
| CP2–CP3, section 5 | Dynamic checks and genuine native history | No initial handoff; missing history limits evaluation |
| Section 4, CP4 | Independent reference, layered checks, six claims | Completeness, traceability and correctness are distinct |
| Section 6, CP5–CP6 | F and reproduction differences | Real execution and actual access boundaries |
| Section 7 | Events, time, interventions, optional usage | Union overlapping intervals; unknown is not zero |
| Section 8, CP7 | 02 and case_results | Per-item sources, gaps and all attempts |
| Sections 9–10 | Citation limits and post-run reporting | References do not validate case tolerances or product performance |

Item-level correspondence is in H. The original master text remains available in the preserved design-basis directory.

## C. First Plan and execution conformity

Freeze the initial assessment before any feedback. For each item record Plan text/location, scientific adequacy, public-requirement coverage, relation to the suggested workflow, evidence and proposed handling. Use scientific statuses reasonable/error/insufficient information/N/A; coverage complete/partial/missing/N/A; workflow agreement/reasonable alternative/needs alignment/indeterminate/N/A. Do not substitute an approved Plan for a missing original.

Assess: public sources/cycle; age/population; SEQN joins/skips; nine PHQ items and thresholds; MEC weights/domain variance; complete cases/denominators; three models/reference group; Holm family; figures/report; executable entry point. Only scientific errors, required omissions and blockers require revision. Missing screenshots, archiving or evaluation steps do not make a scientific Plan wrong. Freeze reasonable CI/df conventions in the approved Plan and independently recompute them; do not force a preferred library's convention on a valid alternative.

Freeze the denominator of applicable execution steps at approval. Report followed/approved deviation/unapproved deviation/insufficient evidence with versioned support. Plan conformity alone does not establish scientific validity.

## D. Independent correctness and claims

Build the reference from the task and approved methods, not copied evaluated code or fitted target answers. Use actual frozen inputs; preserve reference validation and shared-dependency limitations. Replaying evaluated code alone is not independent verification. Check final results, and genuine initial/local historical evidence separately where available.

1. Inputs: official bytes/type, cycle, unique SEQN and join cardinality. Independently derive all categories/inclusion flags and compare every participant and exclusion step. Handle invalid codes per variable; do not globally treat a valid value of 9 as missing.
2. Methods: SMQ040's structural skip after SMQ020=2 must not remove never-established smokers. Do not equate that label to never trying tobacco. PHQ uses nine valid 0–3 items, no zero-filled missing items or DPQ100. Construct domains from the MEC design frame; retain strata/PSU/df. Ordinary logistic uncertainty is not complex-survey uncertainty.
3. Reference implementation: independently use R survey::svydesign and domain subsets, svymean/appropriate proportion CIs, svyglm(quasibinomial), and approved df/CI conventions. Independently apply Holm to the two primary p values. If OpenScience also uses survey, disclose the shared library.
4. Reference self-validation: use tiny hand-checkable inputs for classification, missing PHQ, weighted ratio sum(w*y)/sum(w), and two-test Holm adjustment. Independently check primary prevalence SE and regression sandwich covariance using stratum/PSU linearized contributions with the approved finite-sample convention. Save inputs, calculations and differences. If incomplete, report insufficient evidence rather than full independent validation.
5. Values: compare all eight prevalence rows, six contrast rows and two Holm values. Check cases <= n, probability/CI bounds, OR=exp(beta), CI conventions and common model population. Assess reasons for unestimability; NA is neither automatically an error nor numeric success.
6. Figures/claims: check plotted estimates, intervals, references and labels against CSV values. Primary conclusions must respect Holm; sensitivity cannot replace the primary analysis. Do not call an OR a risk ratio, an association a cessation effect, or a screen a diagnosis. Freeze the independent final-issue list before detailed review-history matching. Disclose prior exposure to feedback during monitoring; do not claim completely blinded assessment.

Report input, methods/Plan, structure, values/conclusions and figures/report separately: pass/fail/incomparable/not evaluated/insufficient evidence. A verified error makes the overall result fail while retaining unresolved items. Without known errors, unresolved assessment stays unresolved; necessary incomparable values stay incomparable. Only all applicable layers passing supports a pass within the predefined scope.

For each of the six claim slots, full presence and full evidence location are required for the locatable numerator. Partial slots do not count. Any substantive contradiction makes support contradicted; otherwise incomplete evidence is indeterminate and absent claims are absent. Accurately describing an erroneous method may support that description while the method itself fails scientific assessment.

## E. Dynamic autoReview quantification

Freeze the first run's final originals before external assessment or repair. First independently assess final outputs and freeze the issue list; then associate complete available autoReview history. Do not feed scores or reference issues into the measured run. Later corrections are separate assisted attempts. No standalone frozen-artifact Reviewer is included.

### 1. Residual issues and misses

Deduplicate issues by root cause and retain ID, evidence, version, severity and inspected scope. Final residual issues are not automatically missed errors.

- An explicitly detected but still incorrect issue is detected/unresolved, not missed.
- With complete relevant scientific autoReview records, an unmentioned residual is an unreported issue within the verified scope.
- Call it a confirmable miss only if evidence additionally shows it existed in the version actually visible to an effective scientific check.
- Separate issues introduced after the last check from blocked access; neither directly measures detection ability.
- Incomplete findings, unmatched versions or unobservable reads make detection/attribution indeterminate. No visible record is not proof of no detection.

Report the residual total with mutually exclusive detected-unresolved, unreported and indeterminate components, then separately qualify visibility, later introduction and confirmable misses. State coverage; do not claim exhaustive error discovery.

### 2. Evidence for detection and change

Link actual check/feedback -> contemporary version -> change -> subsequent version/affected execution -> final state using native events, findings, reads, versions, diffs and reruns. Final contents, repair comments or system self-reports alone do not establish prior error or autoReview-induced repair. Temporal adjacency alone is not causal evidence.

Retrieve immutable history with both generation and collection timestamps. Do not backdate collection or reconstruct an initial version. Local before/after fragments support only the documented local scope. Missing evidence makes the corresponding repair conclusion indeterminate.

### 3. Finding validity

Judge each finding against its actual target version, execution context, task and approved Plan: true error / false positive / reasonable non-error suggestion / indeterminate. Preserve original text and native ID, or clearly label an external H index. A later fix does not invalidate a true finding about an earlier version. Hidden preferences are not errors.

Report raw finding counts and deduplicated issue counts separately. Keep original product pass/fail alongside Human Review's scope/binding assessment. Packaging-only passes do not establish scientific review. Wrong binding/inaccessible files mean blocked review; unobservable reads mean insufficient evidence. Do not rewrite product verdicts.

### 4. Repair outcome

| Outcome | Required evidence |
|---|---|
| Correctly repaired | Proven earlier error, actual change and necessary rerun, independently correct later result |
| Unchanged | True error persists; comparison/execution shows no effective change |
| Changed but unresolved | Actual edit occurred but the original error remains or is only partly resolved |
| Incorrectly changed | Before/after evidence links the edit to an incorrect result or new error; link new issue IDs |
| Indeterminate | Insufficient versions, execution evidence or scientific basis |

Keep all round-level states but count each issue's final outcome once. If an original issue is fixed and another error introduced, record the original repair and the linked new error separately. For false positives record no change / change without demonstrated harm / harmful change / indeterminate, outside the true-error repair denominator.

Attribute repairs to OpenScience following autoReview, human-prompted repair, direct Human Review repair, spontaneous change or unknown. Do not relabel external verification as autoReview.

### Ledgers and denominators

Use issue_ledger.csv fields: issue_id, version_before, version_final, source_evidence, final_problem_status, finding_ids, review_visibility, detection_status, validity, repair_status, new_issue_ids, assistance, diff_refs, rerun_refs, rereview_refs, assessment_evidence.

finding_ledger.csv retains each original feedback item, native ID or H index, event time/phase, target version, validity and linked issue IDs. Report four groups: residual/unreported issues; evidenced detection/change chains; true/false-positive/suggestion/indeterminate findings; repair outcomes for true detected issues. Include evidence-insufficient counts.

Any proportion must include numerator, denominator, unresolved count and coverage. Finding precision may be true/(true+false positive), excluding suggestions/indeterminate. Repair proportion may be correctly repaired/evaluable true detected issues, with indeterminate cases separately disclosed. Zero denominator is N/A. Without an exhaustive initial issue set, do not calculate overall recall. Final correctness cannot establish total detection. These are case-level observations, not general capability claims.

## F. Reproduction and optional comparisons

Reproduction is designed but not authorized. Its boundary is three frozen original XPT files -> recorded cleaning/domain construction/model fitting -> new prevalence.csv, models.csv and two figures. Allow original inputs, dictionary, actual code, configuration, necessary dependencies and result-free commands. Do not replace data by new downloads. Do not provide old result tables, reports, figures, autoReview feedback or independent answers.

Once authorized, use a new process/kernel and separate outputs. First inspect the actual product provenance/reproducibility entry and record start/end artifacts. External script execution cannot substitute for evidence of a missing product feature; report external re-execution separately. Freeze the intended boundary at CP0 and check actual capabilities at CP5. Separate directories or instructions not to read old values are not permission isolation; disclose accessible old values and actual reads when known.

Budget: 45 minutes per attempt; one original replay and at most one separately recorded environment/path rescue without scientific-logic changes. Logical reconstruction requires a separate record and user decision. Freeze new outputs before comparison, then apply D's tolerance and exact IDs/counts/statuses/decisions. Figures require matching scientific content, not identical pixels. Report replay/reconstruction separately from assistance, preserve first failures, and do not count NaN/Inf as numeric matches. Incorrect original results may reproduce consistently.

Bare-run comparison and probes are disabled. Future activation requires prespecified matched inputs/models/budgets/context; distinguish independent planning from shared-approved-Plan comparison. Do not expose OpenScience answers or autoReview opinions. K-Dense's public description is not a measured comparator. A few cases do not establish general superiority.

## G. Time, results and archive

T0 submission; T1 first Plan; T2 approval; T3 actual analysis start; T4 genuine initial artifact creation (missing when unavailable, never replaced by final freezing); Rstart/Rend each natural check, separating Plan and science; T5 first-run final freeze after execution/checks terminate; Vstart/Vend independent verification; T6 reproduction request; T7 new outputs frozen or terminated; T8 comparison complete.

Use timestamps with timezone and evidence. Total wall time T5-T0 includes human handoffs/waiting. Report overlapping review intervals by their union, not their sum. Record active human time separately; unknown is not zero. Preparation time is separate. Optional usage must come from real deduplicated fields.

case_results must cover every master section 8.2 item: product/model/environment/input; all attempts and display reasons; initial Plan quality; alignment/approval/help; execution conformity; delivery x/12; claims locatable x/6 and support; initial/final correctness; autoReview validity/binding; repairs/new errors/assistance; actual product gaps; reproduction boundary/path/real execution/numerical/structural/decision consistency; time; interventions; optional usage; supported claims and remaining limitations. Attach exact versioned evidence, P/A/H and gaps per item. Never use cell or finding counts as independent case counts.

## H. Item-level CP0–CP7 correspondence

The following English renderings preserve each master checklist item's operational requirement. Case adaptations appear in the evidence column. All items are currently unexecuted. The source-language master remains unchanged in the design-basis directory.

| Item | Master requirement, rendered in English | Case evidence and adaptation |
|---|---|---|
| CP0.1 | Freeze the complete prompt, outputs, parameters, environment, budgets and stopping rules; disclose method hints and never remove them retrospectively. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.2 | Preserve actual user files, sources, versions, hashes and available dictionaries. With no attachments, record prompt-only/N/A; do not invent input files. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.3 | Freeze data acquisition/generation responsibility, allowed sources, structure and randomness; determine unspecified seeds before outcomes rather than repeatedly selecting them. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.4 | Freeze the suggested workflow and first-Plan rubric; distinguish public requirements from private alignment preferences, which are not errors. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.5 | Freeze reference methods and independent self-validation; compute reference values after exact inputs become available and record timing. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.6 | Keep reference code, values and issue lists outside execution/review inputs. Log any answer exposure and affected attempts; method feedback remains identifiable. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.7 | Freeze fields, ID alignment, tolerances, decision rules and claim slots using case-specific denominators before results. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.8 | Freeze reproduction inputs, data regeneration scope, context/old-value access, dependency handling and human rescue limits; register optional probes. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP0.9 | Enable available execution/time/usage records and an all-attempt ledger; never overwrite debugging attempts. | input/, logs/config, attempts; A/D/F. No attachments: N/A; probes disabled. |
| CP1.1 | Submit the full task with Plan-first; define permitted preapproval checks. Analysis followed by a methods summary is not an initial Plan. | planning/: original Plan, assessment, feedback, approval and diffs. |
| CP1.2 | Retain complete plan_v1, version, timestamp and accessible context before feedback; log missing plans or premature execution. | planning/: original Plan, assessment, feedback, approval and diffs. |
| CP1.3 | Independently assess plan_v1 and freeze that assessment before feedback; never improve its historical score using later revisions. | planning/: original Plan, assessment, feedback, approval and diffs. |
| CP1.4 | Retain every feedback item, Plan version, difference and reason, distinguishing scientific correction, omission, alignment and wording. | planning/: original Plan, assessment, feedback, approval and diffs. |
| CP1.5 | Retain actual approval, approver, exact approved Plan and relation to the suggested workflow, including unchanged approvals and review time. | planning/: original Plan, assessment, feedback, approval and diffs. |
| CP1.6 | Start only after approval; document and reapprove necessary scientific changes and their affected steps without concealing valid deviations. | planning/: original Plan, assessment, feedback, approval and diffs. |
| CP2.1 | At first scientific use retain exact data bytes, hashes, sources, generating code/commands, parameters/seeds/environment; check task/Plan compliance. | data/, genuine initial/ history, logs/execution and versions; no dynamic-run pause; no invented history. |
| CP2.2 | Version later data changes and affected reruns; correct calculations on invalid input do not make the case correct. | data/, genuine initial/ history, logs/execution and versions; no dynamic-run pause; no invented history. |
| CP2.3 | Retain actual code, commands/Notebook sequence, start/end, exit status and stdout/stderr or product equivalents. | data/, genuine initial/ history, logs/execution and versions; no dynamic-run pause; no invented history. |
| CP2.4 | Retain genuine pre-review tables, figures, report and hashes; distinguish generation, scientific execution and file organization. | data/, genuine initial/ history, logs/execution and versions; no dynamic-run pause; no invented history. |
| CP2.5 | Compare actual design/methods/parameters/outputs to the approved Plan; retain installations, errors, retries and change reasons. | data/, genuine initial/ history, logs/execution and versions; no dynamic-run pause; no invented history. |
| CP2.6 | If outputs appear only after review, state that initial snapshots are unavailable; never reconstruct an initial version. | data/, genuine initial/ history, logs/execution and versions; no dynamic-run pause; no invented history. |
| CP3.1 | Retain trigger, time, internal model, prompt and accessible files/context, including visibility of the approved Plan. | review/: dynamic events/findings, version diffs and reruns; standalone Reviewer excluded. |
| CP3.2 | Retain finding text, native or external ID, target version, evidence and status; separate issues, suggestions and insufficient evidence. | review/: dynamic events/findings, version diffs and reruns; standalone Reviewer excluded. |
| CP3.3 | Retain before/after code/data/tables/figures/report and change attribution; numerical changes require corresponding execution evidence. | review/: dynamic events/findings, version diffs and reruns; standalone Reviewer excluded. |
| CP3.4 | Retain rechecks and stopping reasons, including no findings, no edits, limits and errors. | review/: dynamic events/findings, version diffs and reruns; standalone Reviewer excluded. |
| CP3.5 | Independently assess findings, prior errors, repairs and introduced errors without giving answers to the measured system; record scientific assistance separately. | review/: dynamic events/findings, version diffs and reruns; standalone Reviewer excluded. |
| CP4.1 | Freeze the prespecified deliverables with artifact versions and hashes; use this case's twelve categories rather than the master's five-item example. | final/, verification/: self-validation, full differences, six claims; twelve delivery categories. |
| CP4.2 | Link final data, input hashes, approved Plan, actual executed code and delivered scripts; identify consolidated scripts and check equivalence without substituting them for missing logs. | final/, verification/: self-validation, full differences, six claims; twelve delivery categories. |
| CP4.3 | Use a validated independent reference for inputs, methods, structure, values and figures; report available initial and final checks separately. | final/, verification/: self-validation, full differences, six claims; twelve delivery categories. |
| CP4.4 | Assess each claim's presence, locatability and support; locating erroneous code does not prove correctness. | final/, verification/: self-validation, full differences, six claims; twelve delivery categories. |
| CP4.5 | Select exact reproduction target versions and generating inputs, not mutable latest files; this case targets prevalence/models tables and figures. | final/, verification/: self-validation, full differences, six claims; twelve delivery categories. |
| CP5.1 | Retain the reproduction request, exact target, allowed materials, environment and context under the CP0 boundary. | reproduction/attempt_ID/: boundary, inputs, process and permissions; no execution without authorization. |
| CP5.2 | Retain product-identified inputs/code/parameters/dependencies/gaps and P/A/H origins before and after any human supplementation. | reproduction/attempt_ID/: boundary, inputs, process and permissions; no execution without authorization. |
| CP5.3 | Use a new process/kernel and separate outputs; record inherited conversation/memory/variables and access to old numbers. | reproduction/attempt_ID/: boundary, inputs, process and permissions; no execution without authorization. |
| CP5.4 | Record same-machine/same-environment, new-environment or different-machine conditions; disclose limitations instead of claiming isolation. | reproduction/attempt_ID/: boundary, inputs, process and permissions; no execution without authorization. |
| CP5.5 | Record each replay/reconstruction, automatic dependency handling and human rescue; later success does not erase first failure. | reproduction/attempt_ID/: boundary, inputs, process and permissions; no execution without authorization. |
| CP6.1 | Retain real execution from frozen inputs to new results, actual code, exit status and new hashes; verify regeneration separately if claimed. | reproduction/attempt_ID/: execution/new files/differences; eight prevalence and six model rows replace marker examples. |
| CP6.2 | Check exact ID sets, uniqueness, row counts and analytic populations; record duplicate/missing IDs as structural failures. | reproduction/attempt_ID/: execution/new files/differences; eight prevalence and six model rows replace marker examples. |
| CP6.3 | Compare numeric fields separately with fixed denominators; distinguish missing/nonfinite/out-of-tolerance positions. | reproduction/attempt_ID/: execution/new files/differences; eight prevalence and six model rows replace marker examples. |
| CP6.4 | Retain per-field differences, maximum absolute error, relative error for nonzero references and corrected-decision comparisons. | reproduction/attempt_ID/: execution/new files/differences; eight prevalence and six model rows replace marker examples. |
| CP6.5 | Retain every reproduction attempt's path, assistance, time, usage, ending and unresolved gaps. | reproduction/attempt_ID/: execution/new files/differences; eight prevalence and six model rows replace marker examples. |
| CP7.1 | Retain all cases/attempts and display-selection reasons; do not inflate sample size with cells. | manifest, logs/attempts, figures/index, verification/case_results; no prefilled success. |
| CP7.2 | Bind paper tables/figures to exact versions; include P/A/H and missing/unavailable/N/A per result. | manifest, logs/attempts, figures/index, verification/case_results; no prefilled success. |
| CP7.3 | Retain plan_v1, initial assessment, feedback, approval and later deviations; disclose human planning conditions. | manifest, logs/attempts, figures/index, verification/case_results; no prefilled success. |
| CP7.4 | Archive natural runs separately from optional probes; without a benchmark restrict claims to observed case evidence. | manifest, logs/attempts, figures/index, verification/case_results; no prefilled success. |
| CP7.5 | Check credential-redacted packages remain scientifically interpretable; preserve failures and unverified claims without implying human-assembled evidence is native product capture. | manifest, logs/attempts, figures/index, verification/case_results; no prefilled success. |


Current execution adaptation: [run_001/OPERATING_ADDENDUM.md](run_001/OPERATING_ADDENDUM.md). Original supplied edition retained under original-package.
