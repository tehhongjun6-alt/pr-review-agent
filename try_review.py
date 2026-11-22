from ai import ask_ai
from github_api import files

code = files[0]["patch"]

question = "请帮我检查下面这段代码，找出 bug 和安全问题，用简体中文回答：\n\n" + code

answer = ask_ai(question)

print("===== DeepSeek 的审查结果 =====")
print(answer)