# GBM-001 / upgraded protocol：外部人工操作提示词


你承担本 Case 的人工审核职责。先读 01、03、04，以及设计依据中的 [运行契约](设计依据/operating-contract.md) 和 [证据矩阵](设计依据/evidence-collection.md)，遵循其中共同规则。本准备包不表示已执行；仅在用户要求开始运行或已有同等授权时提交科学任务。

## 本次条件

- Case 根目录：E:/codex/open-science-server/cases/gbm-clinical-trial-landscape；预留尝试：run_NNN。
- 科学任务及真实输入：01中的GBM临床试验研究任务；初始无用户数据文件。OpenScience按公开规则取得ClinicalTrials.gov与文献/官方来源，冻结本次确切输入；K-Dense仅为任务灵感，历史结果不输入。。
- 用户选择的模型/环境及其他配置：使用本机OpenScience当前选择的provider/model/effort与现有Reviewer路由，提交前读回；本地Notebook default-python环境需核对就绪。auto-review开启、Memory关闭、delegation deny、无选定或启用compute hosts，沿用用户已授权full命令权限；不改变全局路由或代理。。
- 总预算、计划修订/Reviewer 修订/复现/新 session 重启额度与终止规则：沿用本 Case 的总计120分钟活动预算：Plan 15、科学执行60、审阅及修订30、Reproduction 15分钟；用户审批/权限等待不计活动预算，计总墙钟时间。阶段不自动借用预算；最多2次Plan反馈、2次科学修订、1次原生Reproduction。指定finalization/revision conflict最多新开1个session，消耗同一总/分阶段剩余额度，不重置预算；不做发布重试或产品修复。到额停止受影响工作并核对终态。。
- 用户审批分工：用户批准本次准确Plan版本、实质科学变更及结果验收；人工审核先留存原版并完成三轴初评，之后执行原生审批。一般权限批准不替代科学Plan审批。。
- 复现/平行展示/probe 的启用与范围：原生Reproduction启用，最终汇总表original captured inputs/end-to-end；不启用平行baseline或注错probe。。
- 审批前允许输入检查范围：配置/模型/环境读取、输入元数据、少量公开来源连通性和已有取证入口核对。未经准确Plan审批不开展全量取数、分类或分析。。

只将 01、真实附件和必要已验证科学环境事实提供给 OpenScience。外部参考、评价、截图和归档不进入科学 Plan；Reviewer 可见题目、批准 Plan 和准确科学版本，不能看到独立参考答案。

## CP0：就绪及原生提交

查已有登记和当前状态，分配未占用 attempt；按 04 冻结本题条件、来源/生成规则和独立核验方法。只预检必要依赖、原生 Notebook 到产物的执行/交付通路和实际取证入口；无计算的任务将对应项记 N/A。

按契约启用并读回 auto-review；提交前、新 session 创建后、科学执行前均确认有效配置。使用原生逐消息 Plan first，保存真实提交与意图证据、session/message ID 和时间。新请求受理后继续查状态，不把 receipt/idle 当原生 Plan 已生成。

截图按 03 和证据矩阵即时捕获、保存并校验。已有原生记录可只读采集；任何采集缺口如实保留。

## CP1：先初评，再用户批准

保存完整 plan_v1 及引用/版本，然后按 04 三轴初评并冻结意见。把结论、必要问题和准确版本交用户；获准反馈与获准执行分列。用户批准当前版本后执行产品审批，读回结果并确认科学执行已启动。

## CP2/CP3：持续执行与自动审阅循环

按证据矩阵记录输入首次使用、Notebook runs、Artifact 版本及每个原生 review 的 scope/读取/findings。受审前后版本在形成时保存；首次完整交付另记 `delivery_first_complete` 及此前审阅历史。CP2/CP3 可以交错，不等完整交付才启用 Reviewer。

本题需审阅的科学文件及依赖：当前题目、批准Plan、原始来源与队列/排除表、标签规则及逐试验证据、实际Notebook代码/run、全部汇总与图数据、图、报告/引用、依赖/科学重跑说明；以每轮真实版本和读取为准。。仅当确有访问缺口时按预算和真实接口补充允许的材料，另标人工干预；不要预设必须增加一个“登记触发 review”轮次。外部不替代内置 Reviewer，也不提供答案。

对实际发现记录 finding→修订前版本→新版本→重跑→再审。分别保存 product_verdict 和外部范围判断；科学方法/范围的实质变化按用户审批规则处理。每轮修复效果按 04 评价，无自然错误或无修订时只报告观察到的流程。

## CP4：核验终态与科学正确性

分别检查 execution/review 终态及末轮实际覆盖。二者终止且文件稳定后冻结 final；按规则受阻/中止也可归档，但不称已通过。对首次完整版、可得的逐轮前后版本及最终版开展适用的独立核验，说明缺口和帮助归因。先完成外部验收意见，再交用户确认。

## CP5/CP6：原生 Reproduction

按 04 的预设范围确认准确目标版本。主展示使用 original captured inputs / end-to-end；checkpoint 另列 downstream-only。保存 S08 起点预览、实际步骤、锁/缺口和比较规则后，执行获准的原生 Reproduction。

结束时保存 receipt 或实际失败记录、日志、逐输出 byte/content/scientific 原始字段及其可得性。新输出的 actual hash/大小、保留/导出状态分列；有真实新文件时再做外部文件比较，未保留时明确限制。原生重执行与外部普通复跑分开，科学正确性与复现一致性分开。

## 指定错误与继续条件

实际 finalization / revision conflict 按契约留证、结束受影响尝试，并在预设预算内创建全新 Case session，从 CP0 配置核对、原生 Plan first 和新版本审批重来。失败记录保留，各尝试分开，不在本计划内排查或修复产品。额度用尽后按停止规则提交当前事实，不无限重开。

## CP7：整理与展示

执行 02 整理已有证据并填 04 结果，核对全部尝试、截图、版本/哈希和缺口。展示采用一条完整尝试的证据并说明选择理由，避免拼接跨 session 的“成功”。按用户选择完成封存，明确已完成与尚未验证范围。
