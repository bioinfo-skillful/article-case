# Scientific and feature assessment: Smoking and depressive symptoms in NHANES

Framework **2.1.0** · protocol **nhanes-smoking-phq9-conversation-v2.1.0** · **prepared; no live validation claimed**.

External operator material. The scientific opening is [01](01_OpenScience_Prompt.md). The [contract](design-basis/operating-contract.md) governs operation; the [adaptation map](design-basis/checklist-alignment.md) accounts for CP0–CP7 and every original section 8.2 result category. The original checklist stays unchanged.

## Direction and scientific obligations

- Retain the NHANES 2015–2016 smoking/depressive-symptom direction. Let the agent justify population, measurements, needed modules, methods and useful outputs.
- Verify actual official source contents and documentation for the variables selected. Validate downloaded file formats, unique respondent identifiers, linkage and cohort definitions. A retrieved HTML error page is not an XPT dataset.
- Check coding, valid values, structural skips and missingness against the selected instruments; screening scores are not automatically clinical diagnoses.
- For population estimates or uncertainty, verify appropriate complex-survey design, weights, domains and variance assumptions for the selected measurements. Do not silently assess against a preferred software language.
- Retrospective refers to secondary analysis of already collected survey data; it does not establish a longitudinal or retrospective cohort design. Interpret this observational cross-sectional setting with appropriately bounded claims; adjustment alone does not establish a causal explanation.
- No inherited age bounds, module quota, symptom cutoff, fixed model list, multiplicity family, required file count or report length applies. Scientific validity still applies to choices actually made.

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

For the approved analysis, independently check participant keys and joins, selected coding/score definitions, inclusion/exclusion logic, counts and missingness. If weighted estimates are chosen, verify the relevant weighting/design assumptions and independently calculate appropriate summaries and uncertainty. If models or sensitivity analyses are chosen, check the actual formulas, populations, reference groups, variance/inference conventions and stated comparisons. Validate the checking method on small hand-checkable examples or an independent implementation.

Check every assessed numerical/qualitative claim against its source and selected method, and check plot/table/report consistency for actual deliverables. Establish numerical tolerances and claim slots before viewing estimates. Published examples and prior case outputs are not target values. An unavailable source or unestimable analysis must remain a documented limitation, not fabricated data or a silently changed cycle.

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
