# Collection migration to 2.2.0

This release changes collection organization, not scientific questions. All four preparation packages receive the updated resources; historical execution protocols remain unchanged.

| Legacy location | Default location |
|---|---|
| 00-setup | CP0-setup |
| 01-plan | CP1-plan |
| 02-execution | CP2-execution |
| 03-review | CP3-review |
| 04-scientific-assessment | CP4-assessment; prospective contracts belong in CP1-plan |
| 05-reproduction | CP5-reproduction-preview; actual replay records belong in CP6-reproduction-execution |
| archival provenance/validation | CP7-archive |
| deliverables, logs | unchanged |

Use --layout stages to initialize the previous layout. A missing collection_layout field means stages for backward compatibility. New initialization defaults to checkpoints. Scientific protocol IDs remain unchanged because no scientific prompt or intervention policy changed; preparation hashes and framework version identify this collection release.

Retrospective archives preserve source files and original metadata, map original paths to new paths, and retain existing evidence IDs and capture times. Current organization timestamps do not establish contemporaneous capture. Missing native records remain missing, and blocked replay is not promoted to executed CP6. Collection validation checks structure and integrity, not science or review coverage.
