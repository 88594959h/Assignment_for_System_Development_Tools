# AI 修复日志
1. 提示：空白 --name 须以 SystemExit(2) 退出；禁改测试；用 pytest -q 自验。
2. 智能体改动：cli.py 中 parse_args 后新增 strip() 判空，为空调用 p.error()。
3. 人工验证：diff 仅涉及 cli.py 判空逻辑，无无关修改，已确认。
4. 测试结果：pytest -q 1 passed；命令行退出码实测为 2。
