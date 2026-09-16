---
name: openscience-human-review
description: Operate OpenScience cases through native Plan first and runtime auto-review, capture versioned evidence, assess plans and scientific outputs externally, and verify native Reproduction. Use for case supervision and collection, not for authoring the scientific analysis.
---

# OpenScience human-review operator

Operate the authorized Case and perform the external assessment before submitting decisions to the user. This skill describes operator behavior; it is not a runtime lock or background watcher. A documents-only request ends after document validation without launching, stopping or reconfiguring a live Case.

## 1. Read and bind the attempt

Read the Case START, 01, 03 and 04. Read its frozen `设计依据/operating-contract.md` and `evidence-collection.md`; for a new Case use the shared [operating contract](../building-openscience-cases/references/operating-contract.md), [evidence matrix](../building-openscience-cases/references/evidence-collection.md) and [terms](../building-openscience-cases/references/CONTEXT.md). The current user's decisions take precedence; preserve earlier Case protocols as historical evidence rather than silently rewriting them.

Discover registration and actual project/session/run IDs, workspace and current versions before acting. Query uncertain submissions before retrying. Preserve the selected model, environment, proxy and routing. Apply the contract's auto-review readiness checks before submission, after session creation and before scientific execution. Do not infer effective settings from global defaults or from another session.

Only 01, real attachments and verified necessary scientific environment facts enter the analysis task. Keep independent references, evaluation rules and evidence management outside the scientific Plan. The built-in Reviewer and external assessment remain distinct roles.

## 2. Arm observation

Use currently supported native CLI/API for status and operations, and actual UI for screenshots. Follow the installed computer-use/browser skill before UI control. Match the app window and visible session to the registration.

Before a phase, test capture and disk saving, identify due checkpoints using the matrix, and verify any supported event/hold mechanism needed for transient states. Capture originals immediately and append one index with capture/archive times, session, visible version or unknown, source and SHA-256. A displayed-but-unsaved image is not archived evidence. Do not claim polling guarantees a transient screenshot.

If capture fails before a required phase, complete allowed recovery and use an already-authorized evidence exception when one exists. Otherwise present the actual missing capability and a concrete choice before knowingly losing required evidence. For an already active run, retain current state and surviving native records, distinguishing late capture from the missed checkpoint. A tool stop or user stop ends input immediately; do not route around it.

## 3. Submit native Plan first

Use the per-message **Plan first** send action; use UI when the user specified it. CLI/API is equivalent only after checking that the installed interface forwards native planning intent. The observed 0.28.0 field is `turnIntent: "plan-first"`; mere planning words or a configuration snapshot do not prove this.

Save the draft/menu, then the exact persisted message ID, intent, session and submission time. Require the native Plan projection/artifact, complete version and approval state. A scope question, idle turn or chat-only plan is not the Plan approval checkpoint. Resolve current scope cards using the question-card procedure below, then verify continuation.

At Plan-ready, retain the original before feedback and perform the contract's three-axis assessment. Present exact version, conclusion, necessary issues with evidence, proposed feedback and decision needed. User approval of that version authorizes the product approval action: re-read, act, verify resulting state and actual execution, save S03, then resume monitoring. Ordinary command permission and approval of feedback are not scientific Plan approval.

## 4. Monitor execution and auto-review together

While an authorized phase is active, answer status questions briefly in commentary and continue. Do not end with only “running” or a promise to keep watching.

1. Read exact execution and Reviewer status plus available attention/version events. Prefer supported event waits; otherwise poll about every 10–20 seconds during active work, keeping deliberate critical-phase waits within 30 seconds. Individual waits stay below 60 seconds; provide a meaningful update at least every 60 seconds.
2. On transitions, capture the due matrix checkpoint and fetch immutable Plan/artifact/run/review records. Verify saved files before claiming retention. CP2/CP3 checkpoints repeat and may overlap.
3. For each native review, save trigger/scope/reads/findings, exact before/after versions, affected re-execution and actual re-review. Use the contract for finding validity, scope sufficiency and causal limits. Do not manufacture native triggers by splitting turns or delaying auto-review until full delivery.
4. Save the first complete delivery with its preceding/concurrent review history. It is not necessarily an unreviewed baseline. Observe the final review and its actual scope; execution idle never substitutes for review termination.
5. Resolve authorized routine permissions through the actual native controls and handle visible questions using the procedure below. Routine valid corrections proceed under existing scope. Material scientific method/scope changes require the user's decision. Any manual/registration-assisted review is separately labeled intervention.
6. On **finalization / revision conflict**, follow the contract's new-session branch: retain error and state, settle the affected old attempt within authorization, create a new attempt within budget, return to native Plan first and exact-version approval. Do not retry publication in the failed session or start product debugging.
7. Persist handoff state and repeat. At budget expiry follow the pre-agreed stopping rule, report the affected attempt as interrupted/partial and retain evidence. A completed CLI run is only one state observation, not proof that the Case or Reviewer completed.

### Visible question cards

When a question card appears or remains visible, inspect it even if execution is idle or the native pending-question list is empty. Match the visible session, question and available request/message IDs to fresh native status and the persisted answer history. A selected option or enabled **Finish** button proves only a UI draft; an empty pending list alone does not prove the card is stale.

- **Current unanswered request:** apply the user's settled choice or delegated decision authority, submit through the native control, and verify answer acceptance and continuation. Permission to run commands does not itself settle scientific scope.
- **Previously answered request:** when the matching answer is persisted and the request is no longer pending, retain the mismatch and explain it promptly to the user. Use a supported non-submitting dismissal or navigate away if appropriate; otherwise explicitly report the remaining stale card. Do not press **Finish** or **Skip all** merely to clear its appearance.
- **Uncertain identity or conflicting state:** refresh and inspect native records before submitting. Report the uncertainty and hold only the affected decision; continue independent authorized work.

Before each question or navigation click, refresh the UI after any scroll, navigation or layout change and confirm the target is visible. After acting, inspect the resulting state before another click. If a click changes an unintended selection, stop further submission, check whether an answer was sent, restore the known prior draft only when safe, and disclose the action and observed outcome. Record the question identity, chosen answer, submission/acceptance evidence or unresolved mismatch. Keep later observations outside already sealed attempt records. At handoff, account for any visible card separately from execution and Reviewer status.

## 5. External reviews and user decisions

| Checkpoint | Complete before asking the user | Decision/action |
|---|---|---|
| CP0 | Resolve obtainable settings/input/capture facts; summarize only outstanding choices | Apply existing authorization; ask only for unresolved material conditions |
| CP1 | Save full plan_v1, freeze three-axis initial assessment, prepare necessary feedback | User approves exact version; operator performs and verifies the native action |
| CP2/CP3 | Capture execution and every actual review; independently assess scope, findings and observed repair chain | Routine authorized revisions continue; escalate material scientific changes, not every review round |
| CP4 | Confirm execution/review terminal states, last-review scope and stable final versions; independently check science and Reviewer effects | Submit a concrete acceptance assessment; retain user's actual decision |
| CP5/CP6 | Verify original-inputs/end-to-end scope, steps, locks/gaps and predeclared comparisons; save native result/logs/per-output fields | Run already-approved Reproduction without asking again; material scope changes need a decision |
| CP7 | Verify evidence index, all attempts, gaps and display candidates | Record user's selection and final claim boundaries |

Reproduction collection follows the matrix: unavailable/ungenerated reports and unretained matching output files are explicit states. Preserve actual output hashes/sizes, never substitute a copy of the old result for a new file. Native consistency and external scientific correctness remain separate.

The independent reference stays private. Once external findings are sent to the execution system, record scientific help and resulting versions. Preserve the native verdict even when external assessment finds its scope insufficient. Actual failed reads differ from unobservable reading. Neither a bound version ID nor PASS alone proves scientific review.

While a required decision is pending, hold the affected workflow at a verified safe state. Complete authorized reading and assessment first; do not send the user an unreviewed Plan. Map the reply to the pending version and question, perform the authorized action, and verify it. A changed version is not automatically approved. Acknowledging “done” without acting is not completion.

## 6. Durable handoff and completion

Maintain `human_records/<attempt>/handoff.md` after significant transitions: case/project/session and run IDs; observation time; effective settings; Plan/artifact versions; execution and review states; last/next screenshots and file paths; pending decision/version; budget/restart counts; blocker and allowed next action; monitoring status (active / awaiting user / stopped / completed / tool blocked).

After compaction, read handoff, re-query product and verify saved screenshots before resuming. Reopen a new session only when the current user or specified error branch calls for it; uncertain state is a reason to query, not duplicate the prompt.

End an active-case turn only when the user stops/replaces the task, a real decision is needed at a safe hold with assessment ready, all authorized work is verified, a tool/external blocker survives permitted recovery, or an explicitly authorized real background monitor is configured and verified. State what still runs and the exact next action. Never imply this skill continues monitoring after the turn ends. For skill/document updates, report the files and checks only; those checks do not prove scientific behavior in a live Case.
