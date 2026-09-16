# Validation record — framework 2.0.0

Date: 2026-09-16. This record concerns preparation integrity and document-guided scenario walkthroughs. It is not a live OpenScience test or proof that an agent will always follow the skills.

## Checks

The release is gated on these commands and checks:

- `python scripts/build_cases.py --check`: rendered packages match case specs, shared references and five templates; no files are changed.
- `python scripts/validate_preparation.py`: archive/master hashes, active links, manifests, skill metadata, unresolved placeholders, portable paths and preparation-only inventory; potential credential patterns are reported by path without values.
- `python -m unittest discover -s tests -v`: integrity boundaries exercised in temporary copies, including tampered archive, stale case, broken link, accidental run result, unresolved placeholder and potential secret.
- Bundled skill-creator validator: both active skills' frontmatter/name constraints.
- Git object verification: archived source bytes and preserved checklist bytes remain identical after staging; current skills copied back only after remote release verification.

## Document-guided walkthroughs

These are manual checks of the instructions against concrete situations, not fabricated native runs or independent agent trials. The relevant decisions are in the [contract](../.agents/skills/building-openscience-cases/references/operating-contract.md) and [working checklist](../.agents/skills/building-openscience-cases/references/operator-checklist.md).

| Situation inspected | Required operator action and retained evidence |
|---|---|
| NHANES asks which population/outcome to explore | Use allocated scope authority or ask the user; accept a justified Plan, without imposing archived ages/cutoffs/models. Save question, accepted answer and resulting version. |
| GBM proposes a narrow initial registry overview | Judge whether it answers a useful bounded question; do not demand the old seven-group package or fixed figure count. Record source/coverage and approved commitment. |
| User delegates Plan approval but retains extensions | Operator reviews and approves the exact version; later scope expansion returns to the user. Permission grants do not expand this allocation. |
| Decision ownership has not been assigned | Hold launch and ask for the five-class allocation together with limits/budgets; do not infer ownership from “run the case.” |
| Proposed method is valid but differs from historical reference | Accept scientific justification, define appropriate independent checking before estimates, and disclose numerical incomparability if it remains. |
| Source download produces unusable input | Preserve actual bytes/error and relevant recovery attempts; report the affected commitment as blocked/partial unless an authorized scope change is made. |
| Visible question card has a preselected answer and no pending API entry | Match request/message identity and persisted answers; submit only a genuine unanswered request within authority. A stale card is recorded/dismissed without resubmission. |
| Main agent is idle while review or correction remains active | Continue observing both lifecycles; do not start an extension or treat the stage as finished. |
| Native correction stops after acknowledgment without repair | Preserve the failed chain; once settled, use only an authorized bounded operator prompt, then verify actual changes and execution. Label operator assistance. |
| Operator would need to supply reference code or numerical answers | Treat this as scientific assistance, check the allocated authority and preserve the original failure; do not call it native automatic repair. |
| Finalization/revision conflict occurs | Preserve error/state; settle old attempt and restart only within allocated allowance, with new Plan-first/approval. Zero allowance holds for a decision. |
| Native Reproduction is unavailable or preview lacks a critical input | Record actual gap/non-execution; no old-output substitution or external rerun labeled native success. |
| Replay matches bytes but has no content/scientific report or retained file | Preserve available raw results and retention state; limit comparison claims and keep correctness separate. |
| A chart is unnecessary for the approved first question | Accept an appropriate output form; record visualization/replay-of-plot as unobserved unless an explicit later objective is approved. |

Walkthrough conclusion: the active instructions provide a defined action, decision boundary and evidence requirement for each situation. Their execution remains to be tested in future authorized scientific cases.

## Execution results

- Case generation check: both packages match their specs, templates and frozen design references.
- Preparation validator: passed; 96 active local links checked, 53 copied historical files verified against source hashes (55 archive files including its README and manifest), both case packages verified, no unexpected runtime files or detected credential patterns.
- Seven integrity regression tests: passed. They exercise read-only validation, archive tampering, stale generated content, broken links, run-result exclusion, unresolved placeholders and secret-pattern reporting without printing values.
- Bundled skill validator: both active skills passed.
- Fourteen document-guided scenarios above: reviewed with defined actions and boundaries. These are operator walkthroughs, not independent agent execution tests.

Archive checks deliberately do not repair historical broken links, old paths, line endings or original-language content. Git whitespace checks apply to newly authored material; historical bytes and the original checklist are preserved. The credential-pattern scan is a publication check, not a claim of exhaustive secret detection. External historical bibliography links were not revalidated in this documentation release.

Remote ref and local skill synchronization verification are deployment checks performed after the release commit; their operational record remains outside this preparation repository. No application settings, existing scientific runs or case results were changed by these checks.
