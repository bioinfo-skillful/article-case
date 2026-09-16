# Case2 agent-led source acquisition

Start with an empty scientific workspace. Submit [the conversational opening](../01_OpenScience_Prompt.md), which supplies the public repository link and the two filenames. Do not download, attach or prepopulate data on the agent's behalf. Let OpenScience retrieve the files, read the author documentation, assess the actual cohort and propose an investigation through native Plan first. The data are not claimed to be attached.

Add only this launch context: "Please use English for our discussion and deliverables." Do not submit START, 02–04, design-basis, the external source manifest, private assessments or the preparation ZIP as scientific inputs. No analysis script or historical result is an initial attachment.

## Verify acquisition externally

The [source manifest](source-manifest.json) retains the previously verified commit, byte counts and SHA-256 values. After the agent downloads the data, retain its actual retrieval URL/time, source revision when available, file bytes/hashes, and native input/run/artifact identities. Compare against the pinned baseline externally. The opening points to mutable `main`: a hash difference is a version discrepancy to investigate, not automatic proof of corrupt data or incorrect science. Resolve a changed source version under the allocated scope authority and record it before analysis; do not silently replace the agent's files.

The author documentation identifies a plasma subcohort of people receiving haemodialysis, NPX normalized log2 expression, binned age, and participant/sample/assay fields. Let the agent establish these facts from the source; assess that it does not generalize to all COVID-19 patients. Attribution and source terms remain applicable (the verified author README states CC BY 4.0).

## Bounded fallback

If repository discovery or retrieval fails, allow the agent's native recovery to settle. Within the agreed operator-recovery authority and allowance, supply the relevant commit-pinned raw download URL(s) from the manifest, including the pinned README if needed. The agent still downloads and verifies the files. Record the exact fallback prompt, reason, URLs and subsequent execution in the intervention ledger; label the run operator-assisted acquisition. Do not send numerical answers or a prescribed analysis recipe.

If access remains unavailable, retain the blocker or request the out-of-scope decision. Do not synthesize observations or silently substitute operator-downloaded files. Preparation hashes establish source identity, not live acquisition success, scientific correctness or native Reproduction.
