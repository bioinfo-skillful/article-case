# Framework 2.1.0 collection upgrade

Preparation update, 2026-09-16. Publication to main was separately authorized after local review. No scientific cases are launched; actual run evidence and delivery ZIPs remain outside this repository.

## What changes

Both skills now require the [standard collection contract](../.agents/skills/building-openscience-cases/references/collection-layout.md). Every case includes blank external record templates and a portable initialization/inventory/validation tool. All four case protocols advance to v2.1.0 because operating requirements changed; their scientific openings remain byte-identical.

The external root uses the agreed six numbered phase folders, deliverables and logs. It includes README, REPORT, HANDOFF, append-only evidence/intervention indices and a hash manifest. Minimum categories explicitly account for questions, Plan versions, prospective assessment, real execution, review/correction chains, scientific outputs, Reproduction and terminal states. Screenshots accompany their actual events. Native evidence remains distinct from operator organization.

The validator reports integrity errors separately from collection gaps. Final handoff requires terminal execution/review/correction states and no pending category accounting. Transparently unavailable evidence may permit handoff while collection remains incomplete. The validator checks structure and references, not scientific truth or whether every native event was observed.

## Migration and preservation

Initialize only fresh external evidence roots; never overwrite historical runs. Existing protocol identities remain attached to past runs. A retrospective reorganization uses schema 1/framework 2.1.0 for storage while preserving its original scientific protocol and software context. Preserve original bytes, source-relative paths and known collection times; mark unknown original event times. Preserve old reports/handoffs and add a new organization summary without rewriting them.

The previous committed preparation is retained as a separate local pre-upgrade ZIP and in Git history. The immutable archive is unchanged. The original checklist and its English working edition retain their original hashes; only the applicability/operating references are updated. No historical result is imported into this preparation repository.

## Validation

Run the preparation generator check, repository validator and test suite described in the root README. Evidence tests use explicitly synthetic temporary fixtures, never native records. They cover complete records, absence states, missing/altered files, broken references, duplicate IDs, unsafe paths, timezone/field errors, pending accounting and unfinished handoffs. Test initialization refusal for existing/nested roots and read-only validation.

Before delivery, validate a fresh filesystem copy, verify unchanged historical archive hashes and scientific opening bytes, synchronize both workspace skills by byte identity, and test ZIP CRC plus member hashes. Save measured results in the local delivery's validation record. The package remains prepared, not live-validated.
