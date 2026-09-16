# NHANES_2015_2016_SMOKING_PHQ9: Human Record Sheet

Root: `E:/codex/open-science-server/cases/nhanes-2015-2016-smoking-phq9`; attempt: `run_001`. Label all external work **Human Review**. Follow the order below; detailed rules are in 04.

| Step | Action | Save | Continue when | Status / evidence |
|---|---|---|---|---|
| 1 · CP0 | Check conditions; enable Plan and autoReview | Inputs, evaluation rules, effective settings; S00 | Readiness verified | Not recorded |
| 2 · CP0 | Submit 01 | Submitted copy, session, T0; S01 | Submission confirmed | Not recorded |
| 3 · CP1 | Save and assess the first Plan | Full text, version, initial assessment, T1; S02 | Original retained before feedback | Not recorded |
| 4 · CP1 | Execute after user approval | Exact approved version, T2/T3; S03 | Actual execution confirmed | Not recorded |
| 5 · CP2–CP3 | Observe science and dynamic autoReview | Native versions, findings, reads, changes, reruns; S04/S05 | No inserted registration round | Not recorded |
| 6 · CP4 | Freeze after termination | delivery_final, hashes, genuine history, T5; S06 | Files stable and termination clear | Not recorded |
| 7 · CP4 | Independently verify final outputs | Issue list, evidence, assessment time | Issue list frozen | Not recorded |
| 8 · CP4 | Associate autoReview and quantify | Four count groups, before/after evidence, unresolved items | Residuals distinguished from misses | Not recorded |
| 9 · CP4 | Obtain user review of the assessment | Actual decision and version | Later repairs kept separate | Not recorded |
| 10 · CP5–CP6 | Reproduce and compare if authorized | Boundary, T6/T7/T8, new outputs; S07/S08 | New outputs frozen before comparison | Not recorded |
| 11 · CP7 | Archive under 02 | All attempts, results, gaps, package | Failures retained | Not recorded |

Do not recreate historical screenshots or missing initial artifacts. Append screenshots per actual review event. Unobservable reads mean insufficient evidence. If reproduction is not enabled, record not run/N/A with the reason. Enabled autoReview does not prove every round was checked.

| Time / stage | Human action | Reason | Before/after version and evidence | Active minutes |
|---|---|---|---|---|
| Not recorded | | | | |

Unknown active time is `missing`, not zero or waiting time. Record scientific assistance separately without rewriting baseline results.

## Fixed sample

Check all records with independent code. Inspect at most 30 participants individually: the first five by ascending SEQN in each smoking category, followed by the first fifteen previously unselected IDs in the merged structural-skip, missing-PHQ, missing-PIR and age-boundary queue. Do not invent replacements when fewer exist. Check boundary rules and all differences in batch. The sample limit does not permit ignoring known errors. Record actions and evidence paths here; keep calculations separately.

## Screenshots

Save originals under `human_records/run_001`; use the single `screenshots.csv` index.

- S00: effective settings before submission.
- S01: confirmed submission and matching session.
- S02: complete first Plan awaiting approval.
- S03: actual state after approval of the exact version.
- S04/S05: observable scientific output, autoReview feedback and changes; append by event.
- S06: termination/completion and final outputs.
- S07/S08: authorized reproduction boundary and termination.
- Exception: actual error before recovery.

Record actual capture time, checkpoint, session, visible version (or unknown), original path and hash. Mark uncaptured transient states missing; do not stage historical evidence.


Current execution adaptation: [run_001/OPERATING_ADDENDUM.md](run_001/OPERATING_ADDENDUM.md). Original supplied edition retained under original-package.
