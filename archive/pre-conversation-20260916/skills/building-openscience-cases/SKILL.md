---
name: building-openscience-cases
description: Prepare or update an OpenScience research case with native Plan first, runtime auto-review, Notebook execution evidence, Reproduction boundaries, and external evaluation under the preserved v0.2 checklist.
---

# 构建 OpenScience Case

从研究题目生成五份可执行准备材料。准备任务完成即交付；科学运行仅在用户明确要求或已有同等授权时开展。更新通用技能不自动启动 Case。

## 读取与决定

1. 读取 [source-manifest.json](references/source-manifest.json) 并核对 [母规范](references/OpenScience_Case运行Checklist_指标与文献_v0.2_20260910.md) 的 SHA-256。哈希不符时寻找原件，不能修改期望值掩盖变化。构建新包前完整读取原文，分段避免截断；完成前逐项核对 CP0–CP7 及第 8.2 节。
2. 读取 [运行契约](references/operating-contract.md)：这是已获用户确认的新默认，特别是原生 auto-review、版本语义、Reproduction 可得性及指定会话错误重启规则。原文不改，适配理由写入 04。
3. 按 [证据收集矩阵](references/evidence-collection.md) 为本题登记真实入口和可用性；术语按 [CONTEXT](references/CONTEXT.md)。历史探针结论只支持所测范围。

提取题目/链接、研究对象、实际输入与允许来源、必需输出、模型/环境、预算、case_root 和可选轨道。可查环境先查；只问尚缺且影响设计的条件。研究网页要读实际内容，不以既有输出当预设真理。按本题预设参考方法、字段/ID/容差、声明槽位、抽样和分母；无数值任务注明 N/A。GBM、PDAC、12 marker、60 单元格、历史模型和路径都不是通用默认。

## 生成五份材料

以 [case-template](assets/case-template/) 为起点，填完所有 `{{...}}`。模板是通用资产，生成的新 Case 才必须消除占位符。

```text
<case_root>/
  START_Run_Case_with_Codex.md
  01_OpenScience_Prompt.md
  02_Post_Run_Collection.md
  03_Human_Record_Sheet.md
  04_Checklist_Alignment_and_Evaluation.md
  设计依据/
    OpenScience_Case运行Checklist_指标与文献_v0.2_20260910.md
    source-manifest.json
    operating-contract.md
    CONTEXT.md
    evidence-collection.md
  run_NNN/
  human_records/run_NNN/
```

母规范按字节复制并核对源/目标哈希；其余三份共同参考也随包复制，使准备包离开技能目录仍可用。生成 manifest 记录各文件来源/版本。已有 Case 保留冻结文件，通过新尝试补充记录新决定；先查登记再选择未占用编号，不重复提交。

- **01**：英文科学问题、真实输入条件、必要交付和科学自检。计算任务明确用原生 Notebook 执行并保存输入、代码、参数/种子；脚本作为交付而非执行替代。非计算任务不强造 Notebook 依赖。外部评分、截图和参考答案留在外部。
- **START**：外部从 CP0 到 CP7 的操作路由，包含原生逐消息 Plan first、auto-review 生效核对、用户准确版本审批及运行中持续取证。
- **02**：外部整理现存证据，按 04 核验评价；事后不能重造初评、瞬时截图或修订前版本。
- **03**：中文短句，每步“做什么—保存什么—继续条件”；CP2/CP3 标记循环，不排成全任务初版之后的一次 review。
- **04**：本题科学判定、已知问题分母、Reviewer 评价、复现规则、母规范逐项适配和证据字段。无加权总分、无预填成功。

## 完成门槛

逐文件核验公开要求在 01 可定位，私有参考不进入执行/Reviewer 材料；START 的 Plan first 是原生逐消息动作；auto-review 执行前生效且新会话读回；03 的留证时序与契约一致；04 有适用分母和所有 CP/8.2 项的对应或 N/A 理由。主展示为 original captured inputs / end-to-end，checkpoint 单列；byte/content/scientific 与输出保留按实际字段填写。遇到 finalization / revision conflict 只按契约重开全新 Case session，不扩展到产品修复。

验证链接可达、母规范哈希未变、新包占位符填全、无旧 Case 参数泄漏。交付五份文件和简短启动说明，区分准备完成、通道已测、科学 Case 已完成；已批准的准备工作不重复请求确认。运行交给 [openscience-human-review](../openscience-human-review/SKILL.md)。
