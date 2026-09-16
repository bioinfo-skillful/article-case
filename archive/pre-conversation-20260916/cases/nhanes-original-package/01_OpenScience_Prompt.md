# Established Cigarette Smoking and Depressive Symptoms in NHANES 2015–2016

## Research task

Analyze the association between established cigarette-smoking status and depressive symptoms among adults aged 18–79 years in NHANES 2015–2016. Estimate survey-weighted symptom prevalence and crude and adjusted prevalence odds ratios. Assess whether the association is sensitive to a higher symptom-score threshold. Treat this as an exploratory cross-sectional analysis, without assuming any direction or statistical significance. Do not infer causation, smoking-cessation effects, a clinical diagnosis, or treatment recommendations.

## Inputs and scientific conditions

Use only the public CDC NHANES 2015–2016 files DEMO_I, SMQ_I and DPQ_I and their official documentation. Retrieve the original XPT files from CDC; do not substitute simulated observations, published result tables, other cycles, or other cohorts.

Official codebooks:
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DEMO_I.htm
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/SMQ_I.htm
- https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2015/DataFiles/DPQ_I.htm
- Survey methods: https://wwwn.cdc.gov/nchs/nhanes/analyticguidelines.aspx

Scientific specification:
1. Link participants by SEQN, validating unique keys and preserving a participant-level exclusion flow. Start with the full eligible MEC survey-design frame and estimate the age 18–79 analytic domains using appropriate domain/subpopulation methods. Do not treat the selected observations as a simple random sample.
2. Define established smoking status from SMQ020 and SMQ040: never-established = SMQ020=2; former = SMQ020=1 and SMQ040=3; current = SMQ020=1 and SMQ040 in {1,2}. Other responses are unknown. A structural skip of SMQ040 after SMQ020=2 is not missing smoking status. The never-established category means fewer than 100 lifetime cigarettes, not necessarily never having tried a cigarette or no current tobacco exposure. Do not mix in vaping or youth questions.
3. Compute PHQ-9 as the sum of DPQ010 through DPQ090, each valid only at 0–3; all nine must be observed. Treat refusal, unknown and missing as missing, never as zero. Do not include DPQ100. Primary outcome: score >=10; sensitivity outcome: score >=15. Describe these as symptom-screen thresholds, not confirmed diagnoses.
4. Use WTMEC2YR, SDMVSTRA and SDMVPSU. State the variance estimator, confidence-interval method, degrees of freedom and handling of any single-PSU domain or sparse estimates. The DPQ documentation requires MEC weights despite the questionnaire format.
5. Descriptive domain: ages 18–79 with known smoking status and complete PHQ-9. Report overall and each smoking category for both thresholds. Adjusted-model covariates: RIDAGEYR (continuous), RIAGENDR (categorical), RIDRETH3 (categorical), and INDFMPIR (continuous). Keep valid zero income-to-poverty ratios. Explain top-coding and missing-data limitations. Do not use automated variable selection or add covariates.
6. Use a common complete-covariate domain for the primary crude and adjusted survey-weighted logistic models; never-established is the exposure reference. Fit the threshold-15 adjusted model on that same domain. Report former/current contrasts for each model, including uncertainty and two-sided unadjusted p values. The two primary adjusted exposure contrasts form one family: additionally report Holm-adjusted p values and decisions at adjusted p <0.05. Crude and sensitivity results are descriptive/exploratory, not additional confirmatory tests. Document the prespecified inferential convention in the plan before fitting models. Do not change thresholds or pooling based on significance.
7. Retain missingness counts, design diagnostics and convergence/sparse-cell warnings. If an estimate is not scientifically estimable, retain its row with an explicit status and reason rather than fabricating a finite value. No imputation, multi-cycle pooling, interaction search, machine learning, or additional literature-derived endpoints is required.

## Required outputs

Use relative paths within the provided scientific working directory. Deliver English text and labels:

- `data/raw/`: the three original XPT files, source URLs, retrieval dates and official variable documentation.
- `data_dictionary.csv`: original and derived variables, types, valid/missing codes, definitions and source references.
- `analysis_data.csv`: one row per linked survey-frame participant, SEQN, required source fields, derived smoking/PHQ variables, design fields and explicit descriptive/model inclusion flags. Preserve enough information for domain estimation; do not export only complete cases as the full design frame.
- `cohort_flow.csv`: ordered mutually exclusive exclusion steps, n_before, n_excluded, n_after and reasons, with separate descriptive and model branches.
- `missingness.csv`: variable, population denominator, missing count/proportion; distinguish structural skips from missing values.
- `prevalence.csv`: eight rows keyed by outcome (phq_ge10/phq_ge15) and group (overall/never_established/former/current); unweighted n, cases, weighted prevalence in [0,1], SE, 95% CI lower/upper, estimation status and reliability notes.
- `models.csv`: six exposure-contrast rows keyed by model (primary_crude/primary_adjusted/sensitivity_adjusted) and contrast (former_vs_never/current_vs_never); outcome, reference, n, cases, log-odds coefficient, design-based SE, OR, 95% CI, unadjusted p, and status. For the two primary_adjusted rows also give Holm p and Holm decision; mark these fields not applicable in other rows. Preserve model formulas and degrees of freedom.
- `figures/prevalence.png` and `figures/odds_ratios.png`, plus vector PDF or SVG copies: show primary prevalence with 95% CIs and primary crude/adjusted ORs with 95% CIs; use clear reference groups and a log OR axis. Keep plotted values available in the CSV files.
- `analysis.R` (or an equivalent executable entry point with all source files): regenerate the analysis tables and figures from the original XPT files in a new process, with explicit input/output arguments.
- `analysis_config.json`: definitions, model formulas, reference levels, estimation/CI/df choices, multiplicity rule, parameters and any actual seed. Record software/package versions and executable commands in README.
- `report.md`: concise scientific report, preferably 1,500–2,500 words, covering the question, sources, methods, cohort/missingness, estimates and uncertainty, sensitivity results, and limitations. Discuss selection from complete cases, residual confounding, reverse causality, survey nonresponse and screening versus diagnosis. Do not require a positive result.
- `README.md`: file index, dependencies/versions, retrieval and offline rerun commands, parameters and limitations. Distinguish the actual executed code from any later consolidated script.

Retain full numerical precision in CSV files; round only for presentation. Keep unestimable fields explicitly marked with reasons. Deliver actual executed scientific outputs; explain any incomplete item.

Preserve the actual inputs and source details. Document the methods and tools used so that the requested work can be retraced. For computational work, retain the executable code, actual parameters and random seeds used, and commands and dependencies needed to regenerate the outputs. For source-based qualitative work, retain resolvable source locations, the interpretation method, and any processing code actually used; do not invent a computational workflow. Keep unsupported or unestimable results explicit, and ensure that the report agrees with its supporting evidence and any requested tables or figures.


