# Scientific and feature assessment: Case3: pathological stage and survival in clear-cell renal cancer

Framework **2.2.0** · protocol **tcga-kirc-stage-survival-conversation-v2.1.1** · **prepared; no live validation claimed**.

External operator material. The scientific opening is [01](01_OpenScience_Prompt.md). The [contract](design-basis/operating-contract.md) governs operation; the [adaptation map](design-basis/checklist-alignment.md) accounts for CP0–CP7 and every original section 8.2 result category. The original checklist stays unchanged.

## Direction and scientific obligations

- Retain retrospective stage/overall-survival analysis in TCGA clear-cell renal cancer. Stage grouping, follow-up horizon, adjustment, analysis methods and output forms remain justified Plan decisions.
- Verify patient-level source identity, study membership, metadata, unique participant keys and exclusions using [scientific source records](sources/source-manifest.json). A Git LFS pointer or HTML page is not the clinical dataset.
- Establish endpoint meaning, time origin/units, event coding, censoring and handling of missing or invalid observations from actual documentation. Do not interchange overall and disease-specific survival.
- Justify stage representation and disclose the staging information available. Avoid unsupported equivalence between staging editions.
- Assess follow-up support, events, uncertainty and assumptions appropriate to each selected estimator or model. If Cox modeling is chosen, examine proportional hazards and relevant diagnostic limitations.
- Address selection, missingness, covariate timing and limitations on generalizing from the cohort. Stage associations do not establish causal effects or a validated individual prognosis tool.
- No inherited early/late grouping, 60/36-month horizon, fixed age bounds, Python-only rule, specific Cox implementation, coefficient count or 13-deliverable quota applies.

These are validity checks applicable to the chosen investigation, not a fixed analysis recipe. Raise a concrete validity problem during Plan review when necessary; disclose any scientific help. The agreed Plan establishes actual scope. An archived example or external study does not supply required estimates or a hidden answer.

## Freeze the stage-specific assessment

Prepare during Plan review and bind to the exact approved version before reading its estimates:

- The useful first question, estimand or qualitative claims; allowed sources; population/scope and exclusions.
- Justified methods, assumptions, missingness/uncertainty handling and genuine scientific limitations.
- Promised output content, claim slots and applicable execution evidence. Output format is chosen for communication, not an inherited quota.
- Independent verification strategy and its self-validation, captured input identities, comparison keys/fields, missing/duplicate/nonfinite handling, tolerances and conclusion rules as applicable.
- Applicable feature observations, stopping conditions and limitations. Zero natural findings means correction is unobserved, not automatically successful.

Freeze the denominator of promised items/claims for that stage; do not delete failed items afterward. A later authorized extension has its own contract and version lineage. Reasonable alternative methods may be incomparable numerically while remaining valid; investigate before judging.

## Conditional independent checks

After Plan approval, independently verify patient identity, cohort/exclusion logic, stage coding, selected endpoint, time units, event indicators and censoring rules. For survival curves, check risk sets, event/censor ordering, support at reported times and the selected uncertainty method. For models, check the actual formula, reference groups, adjustment variables, estimation conventions, diagnostics and interpretation; method-specific checks apply only when chosen.

Freeze assessment claims and tolerances before reading estimates. Use hand-checkable censored examples or an independent implementation to validate the external checker. Compare reported numbers, curves, tables and narrative against approved commitments. No historical numerical result is a target; justified alternatives may be scientifically valid without numerical equivalence. Unsupported horizons, causal claims or missing promised work remain explicit failures or limitations.

The independent check uses the selected methods and exact captured inputs. It must validate itself and disclose shared dependencies. Re-running the agent's own code alone establishes repeatability, not independent correctness. Record pass/fail/incomparable/not-evaluated/insufficient-evidence per applicable layer; a genuine error does not disappear because the output follows an approved Plan.

## Feature objectives and evidence

| Feature/design | Evidence to observe | Limit |
|---|---|---|
| Research clarification and Plan first | Actual questions/answers, persisted native planning intent, full first Plan, assessment and exact-version approval | A written plan or selected question option alone is insufficient |
| Notebook execution | Captured inputs, executed code/parameters, run outcomes and genuine outputs | Exported script is not execution proof; qualitative-only stages may be N/A |
| Provenance and artifacts | Native input/run/artifact-version links; publication and preview state where inspected | External mapping and physical file existence do not establish native publication |
| Runtime auto-review | Actual trigger/scope/reads/findings and any repair/rerun/re-review chain | Normal warnings are not defects; no forced trigger or injected error |
| Progressive interaction | Evidence-backed acceptance/extension decisions and stage/task/Plan lineage | New scope is distinct from automatic repair |
| Native Reproduction | Versioned target, captured-input/checkpoint scope, preview/locks/gaps, receipt/logs and actual comparison results | Preview success and top-level match do not establish full replay or correctness |

Observe these features under their authorized conditions; no claim is predetermined. The short scientific prompt does not carry external scoring, screenshot duties or reference answers. Operational constraints needed for computation are made clear during Plan review.

## Evaluation boundaries

Use [02](02_Post_Run_Collection.md) to report research usefulness, scientific validity, product-feature evidence and Reproduction consistency separately. Preserve every attempt and intervention. Incomplete data justify bounded conclusions only with documented feasibility checks and relevant recovery attempts; they do not automatically convert an approved analysis into a completed proposal.

Reproduction targets and comparison policy are chosen before native replay from the actual useful outputs. If the operation or required evidence is unavailable, record that state without substituting an external rerun. No result in this preparation package is claimed to reproduce another product's published scientific result.
