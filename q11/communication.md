# 协作材料改写（缺陷：空姓名仍输出问候语）

## Issue（重写）
**环境**：Windows 11，Git Bash，greetlab-20260101 0.1.0，Python 3.x（具体小版本待确认）
**复现命令**：`sdt-greet --name " "`
**期望结果**：将只含空白的姓名视为无效输入，向 stderr 打印错误与用法，以退出码 2 结束。
**实际结果**：stdout 输出 `Hello, !`，退出码 0。
**影响范围**：是否影响 Linux/macOS 待确认（该逻辑与平台无关，初步判断为跨平台缺陷，待确认）。

## 提交信息（重写）
Reject blank --name in sdt-greet CLI

问题：--name 传入纯空白字符串时仍输出 "Hello, !" 并以 0 退出，
无效输入未被拦截，调用方脚本无法感知错误。
方案：解析参数后检查 name.strip()，为空时调用 parser.error()，
打印用法至 stderr 并以 SystemExit(2) 退出；正常输入行为不变。
测试：新增 test_blank_name_exits_2，本地 pytest 全部通过。

## 评审意见（重写）
**[Blocking]** `cli.py` 的 `main()` 未校验 `--name` 内容，`" "`
可穿透并输出 `Hello, !`、以 0 退出。风险：自动化脚本依据退出码
判断成功，空姓名会被当作有效数据污染下游日志与流程。建议动作：
在 `parse_args()` 后对 `name.strip()` 判空，为空时调用
`parser.error("...")`（自动退出码 2），并补充边界测试后再合并。
