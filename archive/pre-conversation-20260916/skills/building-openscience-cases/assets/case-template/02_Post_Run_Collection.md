# {{case_id}}：外部收集与核验提示词

对 {{case_root}} 的 {{run_id}} 承担人工审核。读取 START、03、04 和设计依据的运行契约/证据矩阵；只整理本次登记的真实材料。此说明不提供给 OpenScience，也不授权重新启动分析或修改科学输出。

1. 读 handoff/尝试台账，核对准确 session、实际目录与 execution/review 当前状态；活文件只作带时点的部分收集。先查已有清单，追加收集不覆盖历史。
2. 按证据矩阵保留真实输入、Plan 全文与初评/批准、runs、不可变产物版本、首个完整交付版、各轮修订前后版本、最终版。引用准确版本与源/副本哈希；原生 ID 缺失不构造。
3. 整理每个原生 auto-review 的触发类型、时间、scope、读取、findings、修订/重跑/再审及终止原因；人工补充交接/手动 review 另标，首次完整版不得冒充全局未经审阅初版。
4. 对已有材料按 04 完成独立科学核验和 Reviewer 评价，保留参考方法自身验证、逐项差异、已知问题分母和帮助归因；不能从产品 PASS 推导正确。没有前版本的修复与新错误结论记不可评估。
5. 整理各次原生 Reproduction 的 CP5 预览与 CP6 结果。保存实际 receipt/失败记录、日志、逐输出 hash/大小、byte/content/scientific 的原始字段、报告可得性和文件保留/导出状态。有新文件才做独立文件比较；不复制旧产物补齐，不从 matched 生成不存在的数值或像素报告。
6. 核对实际截图文件和单一索引，区分捕获/归档时间；无法补回的历史初评、版本、瞬时图标 missing 及责任原因。收集全部尝试，包括指定错误后的新 session。保留原始失败，后续成功不覆盖。
7. 按 04 填结果表、事件、时间和人工帮助。可选用量只收可绑定本次的原生字段，区分累计与增量；未知不填零，不推算伪精确费用，不读隐藏推理。
8. 生成时间戳目录、索引和哈希清单；若交付 ZIP，校验 CRC、成员及版本身份，注明是否实际包含输入和新文件。分享副本可脱敏，原件保持不变；完成后给用户具体核验结论和展示建议。

## 收集目录

按实际存在材料建立 `human_records/{{run_id}}/collection_<timestamp>/`：

```text
manifest.md
input/
planning/
data/
versions/                         # 各轮不可变版本，明确角色与时点
first_complete/                   # 可能已经受 auto-review 影响
review/round_ID/
final/
reproduction/attempt_ID/
verification/
logs/
figures/
probe/probe_ID/                    # 仅实际获准且发生
```

manifest 保留 case/attempt/session、源记录和版本/哈希、实际采集时间、P/A/H、展示理由与缺口。独立大数据引用需核实可访问；未带必要字节的包不称完整离线复现包。

最终交付：清单/哈希、截图索引、全部尝试与事件台账、Reviewer 轮次/问题明细、参考方法验证与差异，以及 `verification/case_results.md`。该结果表逐项覆盖 04 和母规范 8.2，分开记录“通道可用、证据完整、功能结果”。状态与缺口含义遵循证据矩阵。
