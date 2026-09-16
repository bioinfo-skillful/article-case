---
name: building-openscience-cases
description: Prepare OpenScience research cases that begin with a scientific question and develop through native planning, execution and review. Use to create or revise case preparation, not to launch a scientific run.
metadata:
  version: "2.1.0"
---

# Build a research conversation

Prepare a realistic starting situation and an external operating package. The scientific agent develops a defensible first investigation; the operator retains the evidence needed to assess what actually happened. Preparation ends with validated documents unless running the case is separately authorized.

## Establish the case

Read the [operating contract](references/operating-contract.md) and [terms](references/CONTEXT.md). For evidence planning use the [collection matrix](references/evidence-collection.md). When creating a package, read the [English checklist edition](references/OpenScience_Case_Checklist_Metrics_and_References_v0.2_EN.md), verify its [source manifest](references/source-manifest.json), and apply the [adaptation map](references/checklist-alignment.md).

Identify the research question, motivation, indispensable context, actual attachments and allowed sources. Inspect an explicitly referenced scientific example before drawing on it; distinguish its displayed opening from a marketing summary. Treat examples and published results as references to assess, not target answers.

Keep genuine user constraints. Leave population definitions, measurements, methods, software language and output forms open when the user has not fixed them. A detailed specification is still valid when explicitly requested; record that departure from conversation mode rather than discarding requirements.

## Prepare the package

Read the [collection contract](references/collection-layout.md) when creating or revising preparation. Include the blank [collection templates](assets/evidence-template/README.md) and portable [evidence tool](scripts/evidence.py) in every case. They define minimum collection accounting, phase-local screenshots, versions and explicit gaps. Preparation carries blank templates only; actual evidence is initialized externally at launch.

Use the five [templates](assets/case-template/START_Run_Case_with_Codex.md). Create START and 01–04 plus `design-basis/` and `preparation-manifest.json`.

- **01:** only the natural opening message, containing the question and necessary context. Include genuine attachments/constraints when applicable. Keep private verification, feature scoring and operator instructions outside this message.
- **START:** how to establish decision authority and budgets before launch, find the current native controls, submit Plan first, and progress through the checkpoints.
- **02:** how to organize retained evidence and assess a completed or stopped stage without reconstructing missed historical records.
- **03:** the reusable operator checklist and blank decision/stage records. Preparation leaves run facts unfilled.
- **04:** case-specific scientific obligations, conditional checks and a feature-to-evidence map. Detailed methods, output commitments, claim slots, comparison fields and tolerances are selected for the approved stage before inspecting its results.

Copy the shared contract, terms, evidence matrix, operator checklist, checklist alignment and source manifest to `design-basis/`; copy the English checklist edition byte-for-byte. Generated packages must work away from the skill directory. Record framework version, case protocol identity, source-relative paths and hashes. Replace every template placeholder in generated case files; preserve placeholders only in reusable assets.

Offer follow-up questions as optional examples to choose after findings settle. Do not prewrite a compulsory conversation or quietly reintroduce an old report/file/model quota. Keep the same research topic distinct from the same experimental protocol: a changed opening or interaction rule creates a new protocol identity.

## Validate and hand off

Check that 01 sounds like a researcher asking for help; its methods and conclusions are not predetermined. Verify that 04 assesses valid alternatives fairly, that scientific obligations are separate from product-feature targets, and that every checkpoint and original section 8.2 result category has a mapping or an applicability rule.

Confirm that launch requires an explicit allocation of Plan approval, scope questions, extensions, recovery and acceptance; preparation itself does not choose that authority. Verify links, hashes, English active documentation, portable paths and the absence of inherited runtime/model defaults. Keep previous preparations and runs frozen when generating a replacement.

Deliver the five documents, manifest and preparation status. For an authorized run, hand off to [openscience-human-review](../openscience-human-review/SKILL.md). Document validation is not evidence of live scientific success.
