
import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPO"]


def add_line_numbers(patch):
    result = []
    line_no = 0

    for line in patch.split("\n"):
        if line.startswith("@@"):
            start = line.split(" ")[2]
            start = start[1:]
            start = start.split(",")[0]
            line_no = int(start)
            result.append(line)
        elif line.startswith("-"):
            result.append("    " + line)
        elif line.startswith("\\"):
            continue
        else:
            result.append(f"{line_no:>3} {line}")
            line_no = line_no + 1

    return "\n".join(result)


url = f"https://api.github.com/repos/{REPO}/pulls/1/files"
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(url, headers=headers)
files = response.json()

for f in files:
    print(f"===== {f['filename']}（{f['status']}）=====")
    print(add_line_numbers(f["patch"]))


def post_review(summary, comments):
    review_url = f"https://api.github.com/repos/{REPO}/pulls/1/reviews"
    data = {
        "body": summary,
        "event": "COMMENT",
        "comments": comments,
    }
    response = requests.post(review_url, headers=headers, json=data)
    print("GitHub 回应：", response.status_code)
    if response.status_code >= 400:
        print(response.text)

