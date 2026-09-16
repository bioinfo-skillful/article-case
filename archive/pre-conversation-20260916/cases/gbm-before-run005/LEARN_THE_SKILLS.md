# Learn the two case-study skills

1. Read 01: this is what the scientific agent sees. It asks for science, data and reproducible code.
2. Read 03: this is the short operator sequence. Each checkpoint has something to save before proceeding.
3. Read 04: this explains how correctness, Reviewer quality and reproduction are judged separately.
4. Read START to operate the case; read 02 only when collecting existing evidence. The original checklist contains generic examples, not GBM answers.

building-openscience-cases builds these documents before a run. openscience-human-review operates the run, preserves evidence and prepares assessments for your decisions. Neither is an autonomous monitoring service. Both are installed in this project's .agents/skills and available for subsequent task turns; the operator has explicitly read them for this run.

Examples: an idle session means no main-agent response is active, not that review passed. A file path does not prove the Reviewer opened the correct version. A screenshot is useful UI evidence but not the complete Plan. A successful rerun can faithfully reproduce a wrong result. A PASS that checked only archive hashes says nothing about scientific validity.

Your role: review the operator's assessment of the exact scientific Plan before approval; decide substantive method changes; review final acceptance and display recommendations. Routine monitoring, copying, hashing and independent calculations are the operator's work. Implementation approval has already been given; scientific Plan approval has not.
