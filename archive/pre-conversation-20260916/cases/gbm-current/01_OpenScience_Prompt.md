# Current glioblastoma clinical-trial landscape

## Research task
Produce an evidence-based, current landscape of interventional glioblastoma (GBM) clinical trials: trial status, development phase, start-year trends, sponsor classes, therapeutic modalities, molecular targets, and supported research gaps. Address a research audience. Use public sources and local Python computation. This is a descriptive research study, not individualized treatment advice.

## Inputs and scientific conditions
- Retrieve ClinicalTrials.gov API v2 records using Glioblastoma OR Glioblastoma Multiforme as the starting disease query and interventional study filtering. Document the exact query, API version, retrieval interval, pagination, exclusions, and duplicate handling. Do not assume that every broad-query match is GBM-specific: distinguish exclusively GBM from mixed-condition trials that explicitly include GBM and exclude incidental matches. Do not restrict to recruiting trials or recent start dates.
- Use the actual retrieval date as the snapshot date. Preserve original API responses before analysis, with unique NCT IDs and source links. Do not target a predetermined trial count. If retrieval is incomplete, describe the subset and its limitations explicitly rather than claiming a complete landscape.
- Extract trial title, conditions, status, phase(s), intervention types/names/descriptions, lead sponsor name/class, collaborators, start/completion dates and enrollment (including actual versus anticipated where available). Retain missing and non-applicable values explicitly.
- Define transparent therapeutic-modality and molecular-target classification rules. Categories may overlap; report denominators and unknown/unclassified cases. Retain trial-level evidence for labels. Avoid substring-only target matches (for example, MET in unrelated words). Distinguish therapeutic targets from biomarkers or background mentions.
- Treat phase distributions as cross-sectional counts, not observed probabilities of progression or failure. Any program-level longitudinal inference needs explicit linked evidence and follow-up. Sponsor class is not a measure of funding amount. Separate combined phases and missing phases consistently.
- Integrate a focused, documented PubMed search from 2021 through the retrieval date, supplemented by pivotal earlier studies when needed. Verify efficacy and regulatory claims against primary publications and official regulatory sources. Distinguish GBM-specific authorization, broader indications, off-label use, and devices. Abstract keyword sentiment alone is insufficient evidence of clinical failure.
- The K-Dense GBM example motivates the task scope; its January 2026 results are not prescribed answers. Do not copy its reported counts or infer current results from them.

## Required outputs
Deliver these seven groups as readable files in the case's own scientific workspace and publish the principal report and summary table through native Open Science artifacts:
1. `data/raw/`: exact trial API responses and retrieved literature metadata; `sources.json` with query, retrieval times, URLs, pagination/completeness and source inventory.
2. `data/trials.csv`: one row per included NCT ID, extracted fields, GBM eligibility scope, modality/target labels and evidence; `data/exclusions.csv` and a data dictionary. Use explicit encoding for multivalue fields.
3. `classification_rules.md` and a machine-readable rules/configuration file, including unknown and ambiguous handling and evidence traceability.
4. `tables/summary.csv`: a tidy summary with metric, category, numerator, denominator, percentage and scope; additional breakdown tables as needed. Preserve unrounded numeric values and explain all counting units.
5. `figures/`: at least five readable figures covering status, phase, time trends, sponsor distribution and modality/target distribution. Save underlying chart data and disclose multilabel counts.
6. `report.md` and a PDF rendering: methods, cohort flow and completeness, main results, supported clinical interpretation, limitations and resolvable references. Every quantitative claim should identify its supporting table/figure or source.
7. Executable analysis code, recorded dependency versions, actual parameters/seeds and `README.md` with commands to regenerate derived outputs from the frozen raw inputs without downloading new data.

Retain actual executed code and explain any later packaging edits. Do not fabricate sources, missing values, execution results or files. Make unsupported or unestimable conclusions explicit. Ensure report, tables, figures and code agree.

## Native computational execution
Perform scientific computation through the native OpenScience Python Notebook execution path. Preserve the exact raw source inputs before deriving results and use those captured frozen inputs for downstream Notebook runs. Retain executed cell code/order, parameters, seeds when applicable, and dependency versions. Publish the principal report and summary table as native artifacts linked to their actual Notebook runs and inputs. Exported Python scripts are required scientific deliverables but do not replace Notebook execution. Keep raw-input retrieval separate from downstream regeneration so regeneration can use the frozen snapshot without downloading new data.
