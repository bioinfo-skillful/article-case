# 证据收集矩阵与记录格式

共同边界见 [运行契约](operating-contract.md)，术语见 [CONTEXT](CONTEXT.md)。生成 Case 时将本文件随准备包复制到设计依据；用 04 填入该 Case 的实际入口、目标和分母。下列路径是收集结构，不是产品必然生成的文件名。

## 操作顺序与真实入口

采集角色均为外部人工审核；P/A/H 表示被采集内容的来源。优先原生 UI/导出与受支持 CLI/API，其次是核实产品版本和当前数据根后的只读原文件。先定位准确 session 和 Artifact Version，再解析记录里的 storage key，不能按旧绝对路径猜测。产品 DB/JSON 只读，不注入或改写状态来补齐证据。

| CP / 截图节点 | 采集时点 | 收集物及入口 | 留下的关联 | 继续条件与缺口处理 |
|---|---|---|---|---|
| CP0 / S00 | 提交前 | 已冻结输入/规则；原生设置页及有效配置读回；测试截图保存 | attempt、配置、允许输入及版本/哈希 | auto-review 有效、必要入口可用；若截图不可用先按授权恢复，无法恢复则明确缺口和是否已有例外授权 |
| CP0 / S01 | 原生 Plan first 提交时及之后 | 草稿/发送菜单图；实际提交消息及原生 planning intent | session、message ID、提交时间、附件哈希 | 请求与意图已确认；受理回执不代表 Plan 已完成，状态不明先查询避免重复提交 |
| CP1 / S02 | 初版 Plan 待审批、反馈前 | 原生 Plan 全文/附件与版本；UI 审批状态 | Plan ID/version/hash、初评文件、时间 | 完整版已保存且三轴初评冻结；只有截图/摘要时范围有限，不能改写当原文 |
| CP1 / S03 | 用户批准后 | 用户决定及原生准确版本审批结果、执行启动状态 | 决定时间、操作时间、批准版本 | 已核实审批与实际启动；反馈批准不替代执行审批 |
| CP2 / S04_r | 输入首次使用、run/产物形成或变更 | Notebook run/执行日志；Artifact 不可变版本、原始输入与依赖 | input→run→artifact/version；代码/参数/seed；源/副本哈希 | 版本可定位；活文件变化只作时点快照，缺原生关联单列 H 补链，不称 P 捕获 |
| CP3 / S05_r | 每次原生审阅排队/启动 | Reviewer UI、原生 scope/dispatch/读取调用或等价事件 | Review ID、触发类型、Plan step/run 关联（若可得）、受审版本 | 按真实边界继续；瞬时 UI 错过记 operator omission 或不可捕获原因，保留原生记录但不冒充截图 |
| CP3 / S06_r | 审阅结果、修订及再审事件 | 原生 findings/verdict；不可变前后版本、受影响 run 与后续 review | finding→before→after→rerun→re-review | 有证据的范围才可评价；无读取观察≠没读；真实读取失败=审查受阻。轮次重复追加不覆盖 |
| CP2 / S04_first | 首次完整交付时（可能与 CP3 交错） | 首个完整交付版及截至此时审阅历史 | delivery_first_complete、此前/同期 review IDs | 保存可得版本，不要求关 auto-review，不称全局未经审阅初版 |
| CP4 / S07 | execution 与 review 均终止且文件稳定 | 原生两个生命周期状态、末轮范围、最终原件；外部独立检查 | final versions、末轮覆盖/缺口、参考验证及逐项差异 | 完成或按规则终止都可归档，只有实际通过范围可称已审；向用户提交具体验收意见 |
| CP5 / S08 | 点击正式 Reproduction 之前 | 原生起点预览、原始 recipe、待执行 step IDs、锁/缺口、比较规则 | target version、frontier、claimScope、inputs、lock checksum | 原始起点优先；关键依赖缺失阻断；预览可运行≠执行成功 |
| CP6 / S09 | 正式重执行完成或失败 | 原生 receipt/失败记录、完整日志、逐输出字段；原生历史页/Export verification record（若支持） | operation/receipt ID、完成 steps、expected/actual hash/size、日志引用 | 保存成功或失败；未生成 receipt 时保留失败状态/日志，不构造成功记录 |
| CP6 / S09_outputs | 输出可取得时 | 原生保留/导出的新文件；导出 ZIP 成员清单及哈希 | output identity、retained/exportable、源与副本/成员哈希 | 匹配输出可能未保留；如实记录，只有真实新文件才能进行独立文件比较 |
| CP7 / S10 | 收集完成、展示选择时 | 02 的清单、全部尝试、缺口、用户选择；当前 UI（适用时） | 引用版本、展示理由、时间/帮助、可选用量 | 通道可用、证据完整、功能成功分开；未知保持未知 |
| Exception / SX | 指定错误出现时 | 原始错误、当前状态及已有版本证据 | old attempt/session→新 attempt/session、原因/预算 | finalization / revision conflict 按契约新会话重来；不进入缺陷排查 |

CP2/CP3 是循环，不因表格行序推定产品事件顺序。时间以原生事件及实际观察为准。新 session 开始重新执行 CP0 配置核对及 CP1 审批；旧 session 的 approval/version 不移植。

## 单一索引与文件规则

图像在捕获后立即保存；`captured_at` 与 `archived_at` 分列，若捕获时刻未知则标未知。原图不裁切、不标注；演示副本单列。每轮生成唯一文件名，避免覆盖。至少有：

```text
evidence_id, checkpoint, attempt_id, session_id, event_id,
captured_at, archived_at, source_kind(P/A/H), source_locator,
native_ids, version_refs, path, sha256, size_bytes,
availability, reason, collector, collection_method
```

`availability` 取 captured / missing / unavailable / not_generated / not_retained / not_applicable / insufficient_evidence，并保留产品原文。含义不同，不能合并为“缺失”或自动映射 PASS。另列 `channel_verified`、`evidence_complete`、`feature_outcome`；前两者不能推导第三者。

工具截图只是展示不等于已归档。UI 瞬时状态需要可用事件或经验证的 hold 才能保证捕获；没有支持时在阶段前声明限制，不改变 turn 边界制造画面。运行中捕获失败先保留可得原生证据，标明已丢截图；不能回放界面伪造当时状态。

原文件、不可变快照、ZIP 导出都核对哈希。ZIP 另检 CRC、成员清单和版本绑定；原生 bundle 不含输入/新文件时不能把它称完整离线复现包。私有凭证仅在派生分享副本脱敏，保留原件和变更说明。

## CP3 轮次/问题记录

```text
review_id, trigger_kind(native_auto/manual/registration_assisted/unknown),
queued_at, started_at, ended_at, product_state, product_verdict,
plan_ref, step_refs_or_unknown, scope_version_refs, required_reads,
observed_reads(success/failure/unknown), human_scope_assessment,
finding_refs, before_version_refs, after_version_refs, rerun_refs,
re_review_refs, termination_reason, evidence_refs
```

每个独立问题另行记录问题 ID、版本、finding IDs、成立性、独立依据、发现/未发现、修复/未改/修错、新错误、归因、前后及再审证据。缺前版本只限制相应修复结论，不抹去可评价 finding。报告已核验问题的 x/n，n=0 为 N/A，不将自然案例与注错 probe 混算。

## CP5/CP6 复现记录

```text
attempt_id, target_version, frontier_id, claim_scope,
preview_ref, planned_step_ids, completed_step_ids, captured_inputs,
environment_locks, critical_gaps, noncritical_gaps,
comparison_policy, requested_at, completed_at, native_operation_id,
receipt_ref_or_reason, log_refs, logs_truncated, native_outcome,
output_relative_path, expected_checksum, actual_checksum,
expected_size, actual_size, byte_result_raw,
content_result_raw_or_status, scientific_result_raw_or_status,
output_retained, output_exportable, new_file_ref_or_reason,
independent_comparison_ref_or_limit, intervention, evidence_refs
```

格式是外部记录契约，不要求原生字段同名。缺少原生 ID 则使用明确的 H 索引编号，并写出缺失项。不要从顶层 matched/different 推造数值、像素或科学层结论。

## 已实测的范围（维护基线，不替代本题 CP0）

2026-09-12，安装版 0.28.0 的 reproduction_003 两个新会话：代码内常量、零外部 frozen files、自包含 Notebook 单元、同一 default-python 锁。表格和 PNG 均原生 end-to-end、1/1 run、byte matched；两项 receipt/日志/锁可只读归档，图像原生验证 ZIP 导出可用。独立 content/scientific 报告未生成，匹配重跑文件未保留。真实外部文件输入闭包、多步骤科学 Case、领域比较仍需按任务实测。

此前 attempt_001 已观察审阅触发与 scope/读取记录，也观察到读取失败；尚无完整 warn/fail→自动修订→再审的成功实证。收集入口可用不能替代该闭环效果证据。维护验证报告位于验证仓库 `docs/case-skills-upgrade/validation/`；每次准备包保存所引用报告的版本/位置即可，不把历史数据根、session ID 写成运行默认。
