import json

from ai import ask_ai
from github_api import files, add_line_numbers, post_review

code = add_line_numbers(files[0]["patch"])

question = """你是一位代码审查员。请检查下面的代码，找出 bug 和安全问题。

每一行前面的数字是行号。

只能用 JSON 格式回答，不要输出任何其他文字。格式如下：
[
  {"line": 行号, "category": "bug 或 security", "title": "一句话说明问题", "suggestion": "怎么改"}
]

代码：
""" + code

answer = ask_ai(question)

print("===== DeepSeek 的原始回答 =====")
print(answer)

answer = answer.strip()
answer = answer.removeprefix("```json").removesuffix("```").strip()
issues = json.loads(answer)

print("===== 程序读懂之后 =====")
for issue in issues:
    print(f"第 {issue['line']} 行 [{issue['category']}]：{issue['title']}")
    print(f"    建议：{issue['suggestion']}")

filename = files[0]["filename"]
comments = []

for issue in issues:
    if issue["category"] == "security":
        icon = "🔒 安全问题"
    else:
        icon = "🐛 Bug"

    body = f"**{icon}**\n\n{issue['title']}\n\n**建议：** {issue['suggestion']}"

    comments.append({
        "path": filename,
        "line": issue["line"],
        "side": "RIGHT",
        "body": body,
    })

summary = f"🤖 AI 审查完毕，发现 {len(issues)} 个问题，请看代码旁边的留言。"
post_review(summary, comments)