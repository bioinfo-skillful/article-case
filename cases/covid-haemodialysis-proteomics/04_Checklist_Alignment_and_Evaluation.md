# Scientific and feature assessment: Case2: longitudinal inflammatory proteomics in COVID-19

Framework **2.1.0** · protocol **covid-haemodialysis-proteomics-conversation-v2.1.1** · **prepared; no live validation claimed**.

External operator material. The scientific opening is [01](01_OpenScience_Prompt.md). The [contract](design-basis/operating-contract.md) governs operation; the [adaptation map](design-basis/checklist-alignment.md) accounts for CP0–CP7 and every original section 8.2 result category. The original checklist stays unchanged.

## Direction and scientific obligations

- Retain the longitudinal inflammatory-proteomics question and sampling-time concern. Cohort, panels, time origin/windows, methods and outputs are justified Plan decisions.
- Verify source bytes and author documentation, sample/participant identifiers, assay identifiers and join cardinalities. Use [scientific source records](sources/source-manifest.json); never substitute historical results.
- Respect repeated observations within people. Distinguish within-person change from between-person differences and changing participant composition.
- Verify NPX scale and normalization from the source; avoid an unjustified second log transform, count normalization or replacement of missing measurements with zero.
- Inspect missingness, unequal follow-up, sampling timing, QC information and plate/time confounding as applicable. Distinguish an unavailable diagnostic from a passed check.
- Define the actual estimand, uncertainty and multiplicity policy appropriate to the selected exploratory or confirmatory claims. Bound biological interpretation to this observational cohort.
- No inherited day windows, nearest-day rule, fixed intersection cohort, paired t-test, assay threshold, q cutoff, programming language, figure list or 15-file quota applies.

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

After Plan approval, independently verify source identity, keys and join multiplicity, eligible observations, time origin, repeated-person handling, selected assay scale and missingness. For paired summaries, verify actual pair selection and direction; for longitudinal models, verify model specification, correlation/variance assumptions and the population supporting each estimate. For sampling-time comparisons, distinguish changed timing from changed people and assays. Apply only the multiplicity family and inference conventions justified in the approved stage.

Freeze claim slots and numerical tolerances before viewing results. Validate reference calculations with small hand-checkable examples or an independent implementation; inspect selected figures/tables and uncertainty against actual outputs. Published and historical estimates are not target answers. Alternative valid models are assessed on their own assumptions, not penalized for differing from the old paired-test protocol.

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
