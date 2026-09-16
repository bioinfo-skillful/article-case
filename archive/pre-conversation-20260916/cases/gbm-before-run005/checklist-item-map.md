# Original checklist item mapping

All states start pending. Marker-specific CP6 examples are replaced by the GBM summary fields and six claim groups in 04. Evidence paths are prospective destinations, not claims of existence.

| Item | Preserved original requirement | GBM evidence destination | Status |
|---|---|---|---|
| CP0-1 | 冻结完整初始提示词、交付要求、参数、环境、预算及终止规则；记录其是否明示建议方法，不事后把方法提示从输入中删去。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-2 | 若有用户文件，保存原件、版本/来源、SHA-256，数据字典有则保存。无文件填“初始输入文件：N/A，仅提示词”，不要求预先生成 CSV、代码或种子文件。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-3 | 冻结后续数据生成/获取规则：谁生成、允许来源、结构、模拟参数与随机性要求；任务不涉及数据则相关项 N/A。若种子等未预指定，记录其将在何时确定，不根据结果反复挑选。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-4 | 冻结作者侧“建议流程”和第 3 节初版计划评价规则；明确哪些要求已在提示词公开、哪些仅用于作者评价/后续流程对齐。隐藏偏好不作为初版计划错误。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-5 | 冻结作者参考实现及其独立验证方法；已有固定输入时可预先计算参考值。仅提示词且数据待生成时，先冻结参考方法，后在确切数据冻结后计算参考值并记时点。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-6 | 参考代码、参考数值、作者问题清单不给执行 agent 或内部 Reviewer。计划修改可以提供方法建议；若意外暴露参考答案，登记暴露范围及对应尝试。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-7 | 冻结输出字段、ID 对齐、容差、结论规则和声明槽位。Case 01 使用第 4 节模板；其他 case 在观察结果前替换为自己的规则。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-8 | 冻结第 6 节复现边界：生成材料、是否包含数据再生成、原会话/旧数值可见性、环境依赖操作与人工补救上限；登记是否启用独立错误探针。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP0-9 | 开启可获得的执行、时间与用量记录；建立全部尝试台账，调试重跑不覆盖旧记录。 | run_001/cp0-freeze.json; human_records/run_001/preflight.json; 01/04/START | pending |
| CP1-1 | 发送完整任务，并明确 plan-first：先交付计划，等待人工批准后再开展实质分析。记录批准前允许的输入检查/元数据查看范围；不把已执行分析后整理的方法说明当作初版计划。 | human_records/run_001/planning/; figures/index.jsonl | pending |
| CP1-2 | 在任何人工反馈前保存第一版计划 `plan_v1` 的全文、版本、时间、实际可访问上下文。缺显式计划如实记缺失；若提前执行，保留记录并记流程偏离。 | human_records/run_001/planning/; figures/index.jsonl | pending |
| CP1-3 | 用第 3 节表独立评价 plan_v1；先冻结评价，再向 agent 反馈。后续修正不得回填改善初版判定。 | human_records/run_001/planning/; figures/index.jsonl | pending |
| CP1-4 | 人工对照预定建议流程审阅、修改；保存每条反馈、逐版计划、差异和理由，区分纠正科学错误、补充遗漏、统一流程及表达调整。 | human_records/run_001/planning/; figures/index.jsonl | pending |
| CP1-5 | 保存最终人工批准事件、批准人、批准计划版本 `plan_approved` 及其与建议流程的对应。无修改也记录批准及人工审阅时间。 | human_records/run_001/planning/; figures/index.jsonl | pending |
| CP1-6 | 批准后启动分析。执行中确需改变科学流程时，记录原因、重新审批及受影响步骤；禁止为维持“一致”而隐去合理偏离。 | human_records/run_001/planning/; figures/index.jsonl | pending |
| CP2-1 | 对运行中新生成/获取的数据，首次用于分析时保存确切字节、SHA-256、来源、生成代码/命令、实际参数、种子与环境；核验其是否符合任务和批准计划。 | human_records/run_001/initial/; events.jsonl | pending |
| CP2-2 | 数据后续变化形成新版本，记录原因及受影响重跑。数据生成不合要求是正确性问题；在错误数据上算得正确不能使案例整体通过。 | human_records/run_001/initial/; events.jsonl | pending |
| CP2-3 | 保存实际执行代码、命令/Notebook 单元顺序、开始/结束时间、退出状态、stdout/stderr 或产品等价记录。 | human_records/run_001/initial/; events.jsonl | pending |
| CP2-4 | 保存审核前初始结果表、图、报告及校验和；分别标识数据生成、分析执行与文件整理动作。 | human_records/run_001/initial/; events.jsonl | pending |
| CP2-5 | 对照批准计划记录实际设计、方法、参数、输出及偏离；保存依赖安装、报错、重试和变更原因。 | human_records/run_001/initial/; events.jsonl | pending |
| CP2-6 | 若产品仅在审核后暴露产物，注明初始快照不可得，不事后重建一个“初始版本”。 | human_records/run_001/initial/; events.jsonl | pending |
| CP3-1 | 保存检查触发方式、时间、模型、提示词和实际可访问文件/上下文；记录是否能看到批准计划。 | human_records/run_001/review/; verification/ | pending |
| CP3-2 | 保存每条 finding 原文、ID/人工编号、所指产物确切版本、依据与状态；区分实质问题、建议、证据不足。 | human_records/run_001/review/; verification/ | pending |
| CP3-3 | 保存修改前后代码/数据/表/图/报告的版本及修改者；数值或数据变化必须保存对应重跑。 | human_records/run_001/review/; verification/ | pending |
| CP3-4 | 保存复核及终止原因；无 finding、无修改、超限、报错均如实登记。 | human_records/run_001/review/; verification/ | pending |
| CP3-5 | 作者在不向内部 Reviewer 提供答案的条件下核实 finding、初始问题、修复及新引入错误；采用第 5 节核心质量表。若作者向执行系统反馈问题，另记人工科学帮助及其效果归属。 | human_records/run_001/review/; verification/ | pending |
| CP4-1 | 按第 4 节检查并冻结五类交付物（其他 case 使用预定清单），记录 artifact 版本和校验和。 | human_records/run_001/final/; verification/ | pending |
| CP4-2 | 核对最终数据版本、输入校验和、批准计划、实际执行代码和交付脚本之间的关系；事后整理脚本须标记来源并核查等价关系，不能替代缺失执行记录。 | human_records/run_001/final/; verification/ | pending |
| CP4-3 | 作者用已验证的参考实现核对数据/任务符合性、方法、结构、数值及图表；对初始和最终版本分别记录可获得的核验结果。 | human_records/run_001/final/; verification/ | pending |
| CP4-4 | 逐项填写固定声明槽位的存在、可定位、支持判定；定位到错误代码不等于声明正确。 | human_records/run_001/final/; verification/ | pending |
| CP4-5 | 指定 Reproduction 目标 `results.csv` 的确切版本及生成输入；不使用会变化的“最新文件”。 | human_records/run_001/final/; verification/ | pending |
| CP5-1 | 按 CP0 冻结的第 6 节边界保存请求、目标版本、允许材料清单、环境和上下文条件。 | human_records/run_001/reproduction/attempt_001/boundary.json | pending |
| CP5-2 | 保存产品识别的输入、代码、参数、依赖与缺口；逐项标 P/A/H，人工补齐前后的状态都保留。 | human_records/run_001/reproduction/attempt_001/boundary.json | pending |
| CP5-3 | 使用新进程/内核及独立输出目录；记录是否继承会话、项目记忆或未保存变量，旧结果数值是否可访问。 | human_records/run_001/reproduction/attempt_001/boundary.json | pending |
| CP5-4 | 记录同机器同环境、同机器新环境或异机；实际不能隔离时写清限制，不能统称独立或跨环境复现。 | human_records/run_001/reproduction/attempt_001/boundary.json | pending |
| CP5-5 | 逐次记录直接重放/代码重建、自动依赖处理和人工补救，不用后一次成功覆盖首次失败。 | human_records/run_001/reproduction/attempt_001/boundary.json | pending |
| CP6-1 | 保存从已冻结分析输入到新结果的真实执行证据、实际代码、退出状态及新文件校验和；若声称包括数据再生成，另核验生成步骤。 | human_records/run_001/reproduction/attempt_001/; verification/ | pending |
| CP6-2 | 对 Case 01 核对 12 个 marker 集合、唯一性、行数及各组实际分析样本量；重复/缺失 ID 单列失败。 | human_records/run_001/reproduction/attempt_001/; verification/ | pending |
| CP6-3 | 五个数值字段分别比较并报告 x/12，辅以总计 x/60；缺失、非有限数值、超容差数量分别登记。 | human_records/run_001/reproduction/attempt_001/; verification/ | pending |
| CP6-4 | 保存逐字段差异、最大绝对误差、非零参考值的相对误差及 12 项校正后结论标记比较。 | human_records/run_001/reproduction/attempt_001/; verification/ | pending |
| CP6-5 | 保存每次复现的执行路径、帮助情况、时间、用量、终止原因和未解决缺口。 | human_records/run_001/reproduction/attempt_001/; verification/ | pending |
| CP7-1 | 保存全部 case、尝试及展示选择的台账；按案例展示结果，不用单元格数扩充样本量。 | human_records/run_001/collection/; verification/case_results.md | pending |
| CP7-2 | 正文图表引用具体文件和版本；最终结果表含 P/A/H 来源及 missing/unavailable/N/A。 | human_records/run_001/collection/; verification/case_results.md | pending |
| CP7-3 | 保留 plan_v1、初版评价、人工反馈、批准计划及后续偏离，正文明确人工审批/对齐条件。 | human_records/run_001/collection/; verification/case_results.md | pending |
| CP7-4 | 正常运行与可选错误探针分别封存；若无 benchmark，正文按案例证据范围表述。 | human_records/run_001/collection/; verification/case_results.md | pending |
| CP7-5 | 清除凭证后检查证据包仍保留必要方法信息；留出未验证贡献和失败模式，不据完整人工材料包推断产品内置能力完整。 | human_records/run_001/collection/; verification/case_results.md | pending |
