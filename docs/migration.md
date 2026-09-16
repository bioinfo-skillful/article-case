# Migration to framework 2.0.0

## Which material to use

The active source is this repository's `.agents/skills/` and `cases/`. The [archive](../archive/pre-conversation-20260916/README.md) preserves five distinct source bundles; it is not an installable alternative default. The original source workspace's scientific runs and their protocols remain unchanged.

| Preparation | Archived identity | New active identity |
|---|---|---|
| Skills/templates/references at snapshot | `skills/` in pre-conversation archive | framework `2.0.0` |
| Current NHANES preparation | `cases/nhanes-current/` in archive | `nhanes-smoking-phq9-conversation-v2.0.0` |
| Earlier original NHANES package | `cases/nhanes-original-package/` in archive | Historical only; not merged into the new protocol |
| Current GBM preparation | `cases/gbm-current/` in archive | `gbm-trial-landscape-conversation-v2.0.0` |
| Earlier GBM preparation | `cases/gbm-before-run005/` in archive | Historical only; not merged into the new protocol |

New openings and interaction conditions mean these are not directly comparable fixed-prompt repetitions of previous runs. Preserve any future comparison's differences in scope, model, authority and assistance.

## Install and launch later

Use this repository as a project or copy **both** active skill directories together into the target project's `.agents/skills/`. Their sibling relationship is required by the operator's shared-reference links. Keep the English checklist edition and source manifest with the builder skill. Use only the active copy; leave archived skills outside discovery/installation paths.

Each generated case has five entry documents, a frozen `design-basis/` and a preparation manifest. A case folder is portable on its own. Read START externally; send only 01 and legitimate scientific attachments/context to OpenScience. Choose new scientific and evidence directories at launch rather than reusing old runs. The preparation repository and private checks are not the scientific agent's workspace.

Before launch, explicitly assign decision owners and limits; discover the machine's actual configuration. Windows/Linux paths, model names, a Python/R installation and old permission grants are not part of the case definition. Native UI/API availability must be verified on the installed release.

## Maintain and roll back

Edit shared behavior in the active skills/references. Edit case-specific content in `cases/<case>/case-spec.json`; edit shared preparation structure in the builder's five templates. Run `python scripts/build_cases.py`, then the validation commands in the repository README. Generated documents and design-basis copies are frozen preparation outputs, not independent sources to edit.

The first commit/tag preserves the preparation archive. The release tag fixes the new framework and cases. Later framework/case changes require new versions and newly generated manifests; do not rewrite released archives or historical run records. Restore a prior skill release by explicitly selecting its Git tag and copying its skill pair into a separate chosen environment, not by resetting a live scientific session.

Active instructions, display metadata, checklists and case references are English. The English checklist is a separately hashed working edition, not the original bytes. Historical documents and the original checklist retain exact bytes and original language only in the archive. Source manifests retain the original filename/path as provenance identifiers. Some old absolute paths, external references and manifest entries deliberately point to excluded historical records; they are not current dependencies. The active packages use portable local links and source-relative manifests.
