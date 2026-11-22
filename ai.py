import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["AI_API_KEY"],
    base_url="https://token.quanxiyun.cloud/v1",
)

MODEL = "deepseek-v4.1-flash"


def ask_ai(prompt):
    """把 prompt（问题）交给 AI，回传 AI 的回答（文字）。"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(ask_ai("用一句话介绍你自己"))