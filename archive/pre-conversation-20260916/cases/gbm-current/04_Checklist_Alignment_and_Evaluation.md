# GBM-001 / upgraded protocol：外部核验、适配与评价


仅供人工审核。依据设计依据中的母规范 v0.2 原文、运行契约及证据矩阵；原文哈希见 source-manifest.json。所有结果待运行后填写，不给执行 agent 或 Reviewer 提供本文件和独立参考答案。

## A. 本题事前规则

All scientific requirements are in 01: current interventional cohort, eligibility/pagination/unique IDs, trial fields, evidence-based overlapping labels, descriptive phase/sponsor interpretation, literature/regulatory evidence and seven deliverable groups. Suggested flow: retrieval/eligibility → frozen raw inputs → validation → documented labeling → descriptive counts → evidence integration → figures/report/code. Reasonable alternative methods are allowed. Hidden preferences do not count as errors; scientific evaluation does not demand external screenshot/hash-index/Reviewer orchestration inside the scientific Plan.

本次run_NNN重新运行已确认的GBM任务，公开要求位于01的Research task、Inputs and scientific conditions、Required outputs和Native computational execution。使用现行通用契约取代旧运行程序；旧包完整归档于 E:/codex/open-science-server/case-archives/gbm-clinical-trial-landscape-before-run005-20260912。

沿用本 Case 的总计120分钟活动预算：Plan 15、科学执行60、审阅及修订30、Reproduction 15分钟；用户审批/权限等待不计活动预算，计总墙钟时间。阶段不自动借用预算；最多2次Plan反馈、2次科学修订、1次原生Reproduction。指定finalization/revision conflict最多新开1个session，消耗同一总/分阶段剩余额度，不重置预算；不做发布重试或产品修复。到额停止受影响工作并核对终态。

Seven delivery groups from 01 form the completion denominator (x/7), not an accuracy score. Independently reconstruct counts from frozen raw JSON, a separately written parser and declared classifications; do not copy the evaluated code. Verify the reference on a small constructed dataset with known deduplication, missing phase, combined phase, mixed-condition eligibility and overlapping-label counts. Shared dependencies and coverage limits are disclosed. All summary integer counts, cohort IDs, denominators and labels require exact agreement; finite fractional values use abs(new-reference) <= 1e-10 + 1e-6*abs(reference). NaN/Inf/missing are not automatic matches. Check source query/pagination completeness; cohort errors invalidate downstream completeness claims.

Audit up to 60 unique NCT IDs: sort included IDs, sample min(40,N) using Python random.Random(20260912). From remaining IDs choose up to 20 with ambiguous/multiple/unknown labels first, ordered by NCT ID; fill remaining slots by ascending label frequency then NCT ID (minimum frequency across assigned labels). Freeze chosen IDs before examining classification correctness. Keep random and targeted strata separate, disclose both denominators; no population accuracy or recall extrapolation. Verify eligibility and target/modality evidence using raw fields and primary sources. Audit all high-level clinical/regulatory claims and all figures against their underlying tables, counting units and legends.

Six fixed claim groups: cohort/completeness, status, phase, modality/targets, sponsorship, clinical interpretation. Each gets existence, complete version-linked locatability, and support (supported/contradicted/undetermined/missing). Report locatable x/6 separately from truth. Explicitly stating a quantity cannot be estimated may satisfy an evidence-backed claim. No hidden requirement to make causal or funding claims. Any substantiated error makes correctness fail in the tested scope; otherwise retain unassessed/insufficient/incomparable outcomes until all applicable checks pass. Evaluate the first complete delivery, available local before/after versions and final versions separately; the first delivery may already be reviewed.

每个公开科学要求指向 01 的准确位置；外部隐藏偏好不算任务错误。核验容差、样本和分母事先冻结；无需把外部评分过程交给执行系统。科学任务适用时指定原生 Notebook 执行；非计算任务给出 N/A 理由。最终只报告逐项状态和 x/n，不加权成总分。

## B. 母规范适配与逐项索引

母规范原件不改；下列用户批准的适配用于新 Case，旧 Case 协议保持不变：

| 原文位置 | 新实现 | 适配理由 |
|---|---|---|
| CP0/CP1、第3节 | 原生逐消息 Plan first；完整plan_v1先留存/三轴初评，用户批准准确版本 | 验证真实规划模式；科学错误与合理替代分开 |
| CP2/CP3、第5节 | auto-review 从执行开始生效，按原生边界循环；首次完整交付与每轮修订前版本分列 | 展示运行中审阅和修订，而非等全任务结束再启动；无全局未审基线时不伪造 |
| CP4、第4节 | 输入、方法、结构、数值/结论、图/报告独立核验；验证作者参考自身 | 参考是检查依据，不是无条件真理；产品PASS不是正确性 |
| CP5/CP6、第6节 | 主路径original-inputs/end-to-end；checkpoint单列；预览与正式结果分开 | 原生范围才是复现主张范围；脚本导出或普通复跑不替代执行证据 |
| CP6、第6.3节 | 普通模拟marker按ID和数值规则比较；byte/content/scientific与报告可得性分列 | 领域策略按科学含义选择；界面选项不把marker变成基因 |
| CP6、第6.1节及8.1节 | 保存新输出身份；文件仅在原生保留时复制；原生先比较后导出如实记录 | 原生匹配输出可能未保留，不以旧文件副本代替；未生成内容报告不写PASS |
| 第7节/8.2节 | T4_first为首个完整交付；各轮before/after和Rstart/Rend另列；原生比较结束时间直接保存 | 审阅与执行交错，不能相加重叠时间或硬套不存在的先后关系 |
| CP7 | 全部attempt和展示选择保留；指定会话错误按预算新session从Planfirst重来 | 用户排除产品缺陷排查；失败不从样本台账消失、不拼接会话 |

生成本题时逐行填写下面 CP 项的具体证据位置和适用性；引用母规范节/序号保持可定位。示例 marker 数量、五类交付和容差需替换为本题事前值，不能运行后放宽。

| 母规范项 | 原要求定位摘要 | 实现位置 | 本题实例化 |
|---|---|---|---|
| CP0.1 | 冻结完整初始提示词、交付要求、参数、环境、预算及终止规则 | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP0.2 | 若有用户文件，保存原件、版本/来源、SHA-256，数据字典有则保存 | A、START CP0 | N/A：无初始用户数据附件；仅冻结01原文。后续本次检索响应按CP2.1留存。 |
| CP0.3 | 冻结后续数据生成/获取规则：谁生成、允许来源、结构、模拟参数与随机性要求 | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP0.4 | 冻结作者侧“建议流程”和第 3 节初版计划评价规则 | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP0.5 | 冻结作者参考实现及其独立验证方法 | A、START CP0 | 04 A/D独立parser方法与小型构造数据自检已预设；CP4前实现并验证，结果保存verification/reference/；不输入科学workspace。 |
| CP0.6 | 参考代码、参考数值、作者问题清单不给执行 agent 或内部 Reviewer | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP0.7 | 冻结输出字段、ID 对齐、容差、结论规则和声明槽位 | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP0.8 | 冻结第 6 节复现边界：生成材料、是否包含数据再生成、原会话/旧数值可见性、环境依赖操作与人工补救上限 | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP0.9 | 开启可获得的执行、时间与用量记录 | A、START CP0 | run_NNN/cp0-freeze.json、submitted-prompt.md、effective-configuration*.json；human_records/run_NNN/figures/S00及evidence-index.jsonl |
| CP1.1 | 发送完整任务，并明确 plan-first：先交付计划，等待人工批准后再开展实质分析 | C、START CP1 | human_records/run_NNN/planning/完整原生Plan、三轴初评和批准事件；figures/S01-S03 |
| CP1.2 | 在任何人工反馈前保存第一版计划 `plan_v1` 的全文、版本、时间、实际可访问上下文 | C、START CP1 | human_records/run_NNN/planning/完整原生Plan、三轴初评和批准事件；figures/S01-S03 |
| CP1.3 | 用第 3 节表独立评价 plan_v1 | C、START CP1 | human_records/run_NNN/planning/完整原生Plan、三轴初评和批准事件；figures/S01-S03 |
| CP1.4 | 人工对照预定建议流程审阅、修改 | C、START CP1 | human_records/run_NNN/planning/完整原生Plan、三轴初评和批准事件；figures/S01-S03 |
| CP1.5 | 保存最终人工批准事件、批准人、批准计划版本 `plan_approved` 及其与建议流程的对应 | C、START CP1 | human_records/run_NNN/planning/完整原生Plan、三轴初评和批准事件；figures/S01-S03 |
| CP1.6 | 批准后启动分析 | C、START CP1 | human_records/run_NNN/planning/完整原生Plan、三轴初评和批准事件；figures/S01-S03 |
| CP2.1 | 对运行中新生成/获取的数据，首次用于分析时保存确切字节、SHA-256、来源、生成代码/命令、实际参数、… | E、START CP2/CP3 | human_records/run_NNN/versions/、notebook/、first_complete/及figures/S04_r；按证据矩阵保留input→run→version |
| CP2.2 | 数据后续变化形成新版本，记录原因及受影响重跑 | E、START CP2/CP3 | human_records/run_NNN/versions/、notebook/、first_complete/及figures/S04_r；按证据矩阵保留input→run→version |
| CP2.3 | 保存实际执行代码、命令/Notebook 单元顺序、开始/结束时间、退出状态、stdout/stderr… | E、START CP2/CP3 | human_records/run_NNN/versions/、notebook/、first_complete/及figures/S04_r；按证据矩阵保留input→run→version |
| CP2.4 | 保存审核前初始结果表、图、报告及校验和 | E、START CP2/CP3 | 按新契约保存首个完整交付与已有审阅历史、每次局部修订前版本；不关闭auto-review制造全局未审初版。 |
| CP2.5 | 对照批准计划记录实际设计、方法、参数、输出及偏离 | E、START CP2/CP3 | human_records/run_NNN/versions/、notebook/、first_complete/及figures/S04_r；按证据矩阵保留input→run→version |
| CP2.6 | 若产品仅在审核后暴露产物，注明初始快照不可得，不事后重建一个“初始版本” | E、START CP2/CP3 | 若前版本不可得，记录对应时间和原因；保留首个可得版，不重造未审历史。 |
| CP3.1 | 保存检查触发方式、时间、模型、提示词和实际可访问文件/上下文 | E、START CP2/CP3 | human_records/run_NNN/review/round_ID/及figures/S05_r-S06_r；原生scope/读取/findings与局部修订链 |
| CP3.2 | 保存每条 finding 原文、ID/人工编号、所指产物确切版本、依据与状态 | E、START CP2/CP3 | human_records/run_NNN/review/round_ID/及figures/S05_r-S06_r；原生scope/读取/findings与局部修订链 |
| CP3.3 | 保存修改前后代码/数据/表/图/报告的版本及修改者 | E、START CP2/CP3 | human_records/run_NNN/review/round_ID/及figures/S05_r-S06_r；原生scope/读取/findings与局部修订链 |
| CP3.4 | 保存复核及终止原因 | E、START CP2/CP3 | human_records/run_NNN/review/round_ID/及figures/S05_r-S06_r；原生scope/读取/findings与局部修订链 |
| CP3.5 | 作者在不向内部 Reviewer 提供答案的条件下核实 finding、初始问题、修复及新引入错误 | E、START CP2/CP3 | human_records/run_NNN/review/round_ID/及figures/S05_r-S06_r；原生scope/读取/findings与局部修订链 |
| CP4.1 | 按第 4 节检查并冻结五类交付物（其他 case 使用预定清单），记录 artifact 版本和校验和 | D、START CP4 | human_records/run_NNN/final/、verification/及figures/S07；7组交付、6类声明和本节独立核验规则 |
| CP4.2 | 核对最终数据版本、输入校验和、批准计划、实际执行代码和交付脚本之间的关系 | D、START CP4 | human_records/run_NNN/final/、verification/及figures/S07；7组交付、6类声明和本节独立核验规则 |
| CP4.3 | 作者用已验证的参考实现核对数据/任务符合性、方法、结构、数值及图表 | D、START CP4 | human_records/run_NNN/final/、verification/及figures/S07；7组交付、6类声明和本节独立核验规则 |
| CP4.4 | 逐项填写固定声明槽位的存在、可定位、支持判定 | D、START CP4 | human_records/run_NNN/final/、verification/及figures/S07；7组交付、6类声明和本节独立核验规则 |
| CP4.5 | 指定 Reproduction 目标 `results.csv` 的确切版本及生成输入 | D、START CP4 | human_records/run_NNN/final/、verification/及figures/S07；7组交付、6类声明和本节独立核验规则 |
| CP5.1 | 按 CP0 冻结的第 6 节边界保存请求、目标版本、允许材料清单、环境和上下文条件 | F、START CP5/CP6 | human_records/run_NNN/reproduction/preview/及figures/S08；summary.csv准确版本、原始输入闭包、步骤/锁/缺口 |
| CP5.2 | 保存产品识别的输入、代码、参数、依赖与缺口 | F、START CP5/CP6 | human_records/run_NNN/reproduction/preview/及figures/S08；summary.csv准确版本、原始输入闭包、步骤/锁/缺口 |
| CP5.3 | 使用新进程/内核及独立输出目录 | F、START CP5/CP6 | human_records/run_NNN/reproduction/preview/及figures/S08；summary.csv准确版本、原始输入闭包、步骤/锁/缺口 |
| CP5.4 | 记录同机器同环境、同机器新环境或异机 | F、START CP5/CP6 | human_records/run_NNN/reproduction/preview/及figures/S08；summary.csv准确版本、原始输入闭包、步骤/锁/缺口 |
| CP5.5 | 逐次记录直接重放/代码重建、自动依赖处理和人工补救，不用后一次成功覆盖首次失败 | F、START CP5/CP6 | human_records/run_NNN/reproduction/preview/及figures/S08；summary.csv准确版本、原始输入闭包、步骤/锁/缺口 |
| CP6.1 | 保存从已冻结分析输入到新结果的真实执行证据、实际代码、退出状态及新文件校验和 | F、START CP5/CP6 | human_records/run_NNN/reproduction/attempt_001/及figures/S09；receipt/日志、逐输出字段和真实新文件可得性 |
| CP6.2 | 对 Case 01 核对 12 个 marker 集合、唯一性、行数及各组实际分析样本量 | F、START CP5/CP6 | 原12 marker示例N/A；本题按(metric,category,scope)键、唯一性、计数/分母和NCT集合核对。 |
| CP6.3 | 五个数值字段分别比较并报告 x/12，辅以总计 x/60 | F、START CP5/CP6 | 原12/60分母N/A；本题逐字段用实际行数为分母报告x/n，计数精确、有限比例按冻结容差。 |
| CP6.4 | 保存逐字段差异、最大绝对误差、非零参考值的相对误差及 12 项校正后结论标记比较 | F、START CP5/CP6 | 原校正p值标记N/A；保存本题逐字段误差、类别/计数及6类声明的一致性，不能由byte matched推造科学报告。 |
| CP6.5 | 保存每次复现的执行路径、帮助情况、时间、用量、终止原因和未解决缺口 | F、START CP5/CP6 | human_records/run_NNN/reproduction/attempt_001/及figures/S09；receipt/日志、逐输出字段和真实新文件可得性 |
| CP7.1 | 保存全部 case、尝试及展示选择的台账 | G、02收集 | human_records/run_NNN/collection_<timestamp>/、verification/case_results.md、all-attempts.json和figures/S10 |
| CP7.2 | 正文图表引用具体文件和版本 | G、02收集 | human_records/run_NNN/collection_<timestamp>/、verification/case_results.md、all-attempts.json和figures/S10 |
| CP7.3 | 保留 plan_v1、初版评价、人工反馈、批准计划及后续偏离，正文明确人工审批/对齐条件 | G、02收集 | human_records/run_NNN/collection_<timestamp>/、verification/case_results.md、all-attempts.json和figures/S10 |
| CP7.4 | 正常运行与可选错误探针分别封存 | G、02收集 | probe未启用；旧run001–004在外部历史归档，本次与后续指定错误重启分别登记。 |
| CP7.5 | 清除凭证后检查证据包仍保留必要方法信息 | G、02收集 | human_records/run_NNN/collection_<timestamp>/、verification/case_results.md、all-attempts.json和figures/S10 |

## C. 计划初评与执行符合性

For the actual plan_v1 and associated rules, assess task/cohort, acquisition/completeness, quality/missingness, classification validity, counting units/denominators, clinical-source validation, output coverage and regeneration. Each row records exact evidence, scientific validity (reasonable/error/insufficient/N/A), public coverage (complete/partial/missing/N/A), suggested-flow relation (aligned/reasonable alternative/needs alignment/unknown) and necessary action. Freeze before feedback. Only scientific errors, public omissions and blockers mandate change. Preserve every Plan version and actual user approval. Freeze the execution-step denominator at approval, then report followed/approved deviation/unapproved deviation/insufficient evidence.

每项记录 plan_v1 原文位置、科学合理性（合理/错误/信息不足/N/A）、公开要求覆盖、与建议流程关系（含合理替代）、依据和拟处理。初评在任何反馈前冻结；缺完整原版如实限制评价，不以批准版替代。只修正科学错误、明确要求遗漏和实际执行阻碍。批准时固定适用步骤分母，执行分别列符合、获准偏离、未获准偏离和证据不足。

## D. 独立科学正确性与声明

Seven delivery groups from 01 form the completion denominator (x/7), not an accuracy score. Independently reconstruct counts from frozen raw JSON, a separately written parser and declared classifications; do not copy the evaluated code. Verify the reference on a small constructed dataset with known deduplication, missing phase, combined phase, mixed-condition eligibility and overlapping-label counts. Shared dependencies and coverage limits are disclosed. All summary integer counts, cohort IDs, denominators and labels require exact agreement; finite fractional values use abs(new-reference) <= 1e-10 + 1e-6*abs(reference). NaN/Inf/missing are not automatic matches. Check source query/pagination completeness; cohort errors invalidate downstream completeness claims.

Audit up to 60 unique NCT IDs: sort included IDs, sample min(40,N) using Python random.Random(20260912). From remaining IDs choose up to 20 with ambiguous/multiple/unknown labels first, ordered by NCT ID; fill remaining slots by ascending label frequency then NCT ID (minimum frequency across assigned labels). Freeze chosen IDs before examining classification correctness. Keep random and targeted strata separate, disclose both denominators; no population accuracy or recall extrapolation. Verify eligibility and target/modality evidence using raw fields and primary sources. Audit all high-level clinical/regulatory claims and all figures against their underlying tables, counting units and legends.

Six fixed claim groups: cohort/completeness, status, phase, modality/targets, sponsorship, clinical interpretation. Each gets existence, complete version-linked locatability, and support (supported/contradicted/undetermined/missing). Report locatable x/6 separately from truth. Explicitly stating a quantity cannot be estimated may satisfy an evidence-backed claim. No hidden requirement to make causal or funding claims. Any substantiated error makes correctness fail in the tested scope; otherwise retain unassessed/insufficient/incomparable outcomes until all applicable checks pass. Evaluate the first complete delivery, available local before/after versions and final versions separately; the first delivery may already be reviewed.

独立参考从任务/批准方法及确切输入推导，用手算小样本或另一实现验证自身并说明共享依赖；数据尚未形成时先冻结方法，形成后再算参考值和记时。非数值任务用可定位来源、方法和论证核验，不强造数值测试。既有官方输出可作参考，不能直接当真值。

对首次完整交付版、可得的局部前后版本及最终版分别核验输入规范、方法、结构、数值/结论、图/报告。状态为通过/不通过/不可比/未评估/证据不足/N/A；任一已证实错误即不通过，保留其他未决项。合理替代导致数值不可比不自动是科学错误。

声明槽位分存在、可定位、支持：完整存在且全槽位有确切版本证据才计入定位分子；支持另判支持/矛盾/无法判断/缺失。准确描述错误方法可支持“使用了什么”的描述，但方法仍错误。交付完整性不等于科学正确性。

## E. 四类 review 与效果评价

Plan初评由外部完成、用户批准；运行中/结束时审阅由内置Reviewer按原生事件完成；独立科学核验与Reviewer评价由外部完成。按证据矩阵保存每轮触发、scope、实际读取、findings、版本和重跑/再审。

首先分列 product_verdict 与 human_scope_assessment，判断准确版本、题目/Plan和必需科学文件的可读性与覆盖。不可读/错版为受阻，无读取观察为证据不足，清单/哈希PASS只支持打包检查。手动或登记辅助审阅单列干预；不得冒充原生自动触发。execution idle 时仍需检查 review queued/running 及末轮实际范围。

| 问题ID / 修订前版本 | review与finding原文 | 独立依据 / 成立性 | 是否发现 | 后版本 / 修复及新错误 | 帮助归因 | 重跑 / 再审 |
|---|---|---|---|---|---|---|
| 待记录 | | | | | | |

按契约分类并去重；分母是已独立核验的问题集合，n=0写N/A，不报未知完整错误集的召回率。首次完整交付可能已有审阅，不能据它推断运行前所有错误；无前版本的修复和新错误不可评估。原生PASS不说明新错误为零。无自然错误/未发生修订时只报告流程可观察，纠错效果未验证；probe另表且仅按授权启用。

## F. 原生 Reproduction 与可选轨道

目标为最终 tables/summary.csv 的准确原生版本。原始捕获输入是本次新获取并冻结的API原始响应、文献元数据、实际代码/配置/依赖；不联网刷新，也不复用历史Case checkpoint。主展示 original captured inputs / end-to-end 限于从这些科学输入到汇总表的生成过程；不声称复现在线注册库随时间的状态。按原生预览确认全部必要步骤、锁和缺口，关键缺口阻断。checkpoint仅可另列downstream-only，不能替代主展示。1次正式原生执行；新进程/内核、实际恢复环境、旧输出可见性按真实结果记录。表格按(metric,category,scope)对齐，检查复合键唯一性/缺失，计数和分母精确，有限浮点 abs(new-reference)<=1e-10+1e-6*abs(reference)，非有限值单列。采用普通表格比较，不选差异表达领域策略。保存receipt、日志、逐输出byte/content/scientific真实字段或未生成状态、actual hash/大小；文件保留/可导出单列，无新文件不冒充独立新文件比对。科学正确性使用独立参考另评。

列明 CP0 预设的原始捕获起点、目标版本和范围；CP5 核对实际 steps、锁及关键/非关键缺口。正式 receipt 与逐输出记录按证据矩阵；保留全部失败、重试和帮助。主结果为 original-inputs/end-to-end；checkpoint为downstream-only。全链路范围仅指声明的生成过程，不自动含外部来源重新获取。

byte、content、scientific 分列原始字段/报告状态；未生成、未保留、N/A、产品unavailable与应收未收分别记录。新文件可得时先原样归档再外部比较；不可得时保存actual checksum/大小，说明外部未做独立新文件比较。原生先比较后导出按实际事件留证。完整ZIP不等于完整离线复现包；需检查成员是否含实际必需内容。

本题表格按预设ID对齐，重复/缺失/额外ID单列结构问题，NaN/Inf不默认为一致；数量/样本量和结论规则单独核对。模拟连续marker不是基因；无领域含义时scientific=None/N/A。两次一致可以共同复制科学错误，因此D的独立核验与本节分开。

未启用平行对照或注错probe；指定会话错误按START额度重开全新session，不开展产品缺陷排查。

未启用轨道记未运行。平行展示说明原题独立规划或共享批准Plan的条件，不能混称；不提供原答案或Reviewer意见。注错probe与自然尝试、重开session均不增加独立Case数。

## G. 时间、结果与封存

时间保存实际来源和时区：T0提交、T1初Plan、T2批准、T3执行开始、T4_first首个完整交付、各轮修订前后及Rstart/Rend、T5最终冻结、Vstart/Vend独立核验、T6原生复现请求、实际执行终止/比较结束/新文件归档时间。原生事件先后与外部采集时间分别记录，无法拆开则标缺口。总墙钟直接取所声明端点差，执行/review重叠取并集；等待不当人工活跃分钟，未知不记零。

每行结果须附准确版本证据、P/A/H、适用性和缺口。最终case_results覆盖母规范8.2的全部19项：

| 项目 | 本题结果 | 证据 / 来源 / 限制 |
|---|---|---|
| 产品/模型/环境与输入 | 待记录 | |
| 全部尝试及展示理由 | 待记录 | |
| 初版计划质量三轴 | 待记录 | |
| 人工反馈与准确版本审批 | 待记录 | |
| 执行与批准Plan关系 | 待记录 | |
| 交付完成x/n | 待记录 | |
| 声明定位x/n及支持 | 待记录 | |
| 首次完整/局部前后/最终正确性 | 待记录 | 不冒充全局未审基线 |
| Reviewer finding依据和绑定 | 待记录 | |
| Reviewer修订结果、帮助及新错误 | 待记录 | 无基线的类别不可评估 |
| 实际产品缺口及外部未收证据 | 待记录 | |
| 复现起点/路径/环境/帮助 | 待记录 | |
| 真实重执行及各次结局 | 待记录 | |
| 逐输出byte/content/scientific及数值比较 | 待记录 | 未生成的报告保持未生成 |
| 复现结构/结论及文件保留 | 待记录 | |
| 实际时间及区间并集 | 待记录 | |
| 人工介入/计划帮助 | 待记录 | |
| 可选用量/费用 | 待记录 | |
| 主张支持与局限 | 待记录 | |

1–3个Case仅支持所测条件；单元格、finding、复查轮次和新session都不当独立样本。正文同时保留失败/未决范围及用户展示选择。
