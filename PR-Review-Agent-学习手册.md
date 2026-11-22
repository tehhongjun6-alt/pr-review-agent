# 🤖 PR Review Agent 学习手册（零基础版）

> **最终目标**：在 GitHub 开一个 Pull Request（PR），几分钟后，AI 自动读你改了什么，找出 bug、安全问题、写得不好的地方，然后在那几行代码旁边留言，告诉你怎么改。

---

## 📍 我的进度

完成一课就把 `[ ]` 改成 `[x]`。

- [ ] 第 0 课：准备工具
- [ ] 第 1 课：Python 最基础的部分
- [ ] 第 2 课：用 Python 调用 AI
- [ ] 第 3 课：Git 和 GitHub，开出第一个 PR
- [ ] 第 4 课：用程序读取 PR 改了什么
- [ ] 第 5 课：让 AI 审查代码
- [ ] 第 6 课：把评论贴回 GitHub
- [ ] 第 7 课：GitHub Actions，让一切自动运行

**我用的 AI 供应商**：DeepSeek（模型 `deepseek-flash`）

---

## 🧭 整个项目的思路（先看懂这张图）

把 agent 想成**一个自动改作业的助教**：

```
 你开了一个 PR
      │
      ▼
 ① 铃响了  ── GitHub 通知："有新作业！"          （第 7 课）
      │
      ▼
 ② 拿作业  ── 程序去 GitHub 拿改动的代码（diff）   （第 4 课）
      │
      ▼
 ③ 请老师看 ── 把代码交给 AI，请它找问题          （第 2、5 课）
      │
      ▼
 ④ 写评语  ── 把 AI 的意见贴回 GitHub 那一行旁边   （第 6 课）
```

第 1 课和第 3 课是基本功：第 1 课学 Python（写助教的语言），第 3 课学 GitHub（作业交在哪里）。

### 最后的项目文件长这样

```
pr-review-agent/
├── .env                  ← 放密码（API key），绝对不上传
├── .gitignore            ← 告诉 Git 哪些文件不要上传
├── requirements.txt      ← 列出要安装的工具包
├── ai.py                 ← 负责"问 AI"              （第 2 课）
├── github_api.py         ← 负责"跟 GitHub 沟通"     （第 4、6 课）
├── review.py             ← 主程序，把一切串起来      （第 5、6 课）
├── sample/
│   └── shop.py           ← 故意写错的练习代码        （第 3 课）
└── .github/workflows/
    └── review.yml        ← 自动运行的设定            （第 7 课）
```

---

## 📘 学习方法

1. **代码自己打，不要复制粘贴。** 打的过程会让你注意到每个符号。
2. **出错是正常的。** 把完整的错误信息贴给 AI 助手（或我），一起看懂它。
3. **每课的练习要做。** 做不出来没关系，但要试过。
4. **每课最后有"完成检查"**，全部打勾才进入下一课。

---

# 第 0 课：准备工具

## 🎯 目标
电脑上装好所有需要的工具。

## 🧰 工具清单

| 工具 | 是什么 | 比喻 | 状态 |
|---|---|---|---|
| Python | 一种编程语言 | 助教说的"语言" | ✅ 已装（3.14） |
| VS Code | 写代码的软件 | 写作业的"本子" | ✅ 已装 |
| Git | 记录代码每次修改的工具 | 游戏的"存档" | ✅ 已装（2.55） |
| GitHub 账号 | 放代码的网站 | 网上的"作业柜" | ✅ 已有 |
| AI API key | 使用 AI 的"会员卡" | 请老师的"门票" | ✅ 已有 |

## ✋ 动手

### 步骤 1：给 VS Code 装 Python 插件
1. 打开 VS Code
2. 按 `Ctrl + Shift + X` 打开扩展（Extensions）
3. 搜索 **Python**，安装发布者为 **Microsoft** 的那个

### 步骤 2：告诉 Git 你是谁
Git 每次存档都会记下"谁存的"。在 VS Code 按 `` Ctrl + ` ``（数字 1 左边那个键）打开**终端**，输入（换成你自己的名字和 GitHub 用的邮箱）：

```powershell
git config --global user.name "你的名字"
```

```powershell
git config --global user.email "你的GitHub邮箱"
```

### 步骤 3：认识"终端"
终端（Terminal）就是**用打字的方式命令电脑做事**。以后很多步骤都在这里输入命令。试试：

```powershell
python --version
```

看到 `Python 3.14.x` 就成功了。

## ✅ 完成检查
- [ ] VS Code 装好 Python 插件
- [ ] 设定了 git 名字和邮箱
- [ ] 会在 VS Code 里打开终端，并成功运行 `python --version`

---

# 第 1 课：Python 最基础的部分

## 🎯 目标
看得懂、改得动简单的 Python 代码。**只学这个项目会用到的部分**，不贪多。

## ✋ 准备
1. 在"文档（Documents）"里新建一个文件夹 `python-practice`
2. VS Code → File → Open Folder → 选这个文件夹
3. 新建文件 `lesson1.py`，代码写在这里
4. 运行方法：在终端输入 `python lesson1.py`，或点右上角的 ▶️ 按钮

---

### 1.1 `print`：让电脑说话

```python
print("你好，世界")
print(1 + 2)
```

`print(...)` 会把括号里的东西显示出来。文字要加引号 `"..."`，数字不用。

---

### 1.2 变量：贴了名字的盒子

```python
name = "小明"
age = 20
print(name)
print(age + 1)
```

**比喻**：`name = "小明"` 就是拿一个盒子，贴上标签 `name`，里面放进 `"小明"`。之后说 `name`，电脑就会去打开这个盒子。

> ⚠️ `=` 在编程里不是"等于"，而是"放进去"。

---

### 1.3 f-string：把变量塞进句子里

```python
name = "小明"
age = 20
print(f"我叫{name}，今年{age}岁")
```

引号前面加 `f`，大括号 `{}` 里的变量就会被换成它的值。**这个项目会大量用到它**。

---

### 1.4 列表（list）：一排盒子

```python
fruits = ["苹果", "香蕉", "榴莲"]
print(fruits[0])        # 苹果（从 0 开始数！）
print(len(fruits))      # 3，len = 有几个
fruits.append("芒果")   # 加一个到最后
print(fruits)
```

`#` 后面的字是**注释**，写给人看的，电脑会跳过。

---

### 1.5 字典（dict）：有标签的抽屉柜

```python
student = {
    "name": "小明",
    "age": 20,
    "city": "吉隆坡",
}
print(student["name"])  # 小明
student["age"] = 21     # 修改
print(student)
```

**比喻**：列表用"第几格"找东西，字典用"标签名"找东西。

> 💡 **为什么重要**：GitHub 和 AI 回给我们的资料，几乎都是"列表里装字典"的形式。

---

### 1.6 if：做选择

```python
score = 75
if score >= 80:
    print("优秀")
elif score >= 50:
    print("及格")
else:
    print("不及格")
```

> ⚠️ **缩进很重要！** `if` 下面那行前面要有 4 个空格（按一次 Tab）。Python 靠缩进知道"哪些代码属于这个 if"。

---

### 1.7 for：重复做

```python
fruits = ["苹果", "香蕉", "榴莲"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")
```

意思是："把 `fruits` 里的东西一个一个拿出来，每次叫它 `fruit`，然后执行下面的代码"。

---

### 1.8 函数（function）：自己做的小机器

```python
def greet(name):
    message = f"你好，{name}！"
    return message

print(greet("小明"))
print(greet("阿华"))
```

- `def` = 定义一台机器
- `name` = 放进机器的原料
- `return` = 机器吐出来的成品

**比喻**：榨汁机。放进苹果，出来苹果汁；放进橙，出来橙汁。写一次，用很多次。

---

### 1.9 import：借用别人做好的工具

```python
import json
```

Python 自带很多工具包，`import` 就是"把工具箱拿出来"。别人做的工具包要先安装（用 `pip install`，第 2 课会教）。

---

### 1.10 JSON：程序之间传话的格式

JSON 长得跟字典很像，但它是**一串文字**。程序之间（例如你的程序和 GitHub）都用 JSON 传资料。

```python
import json

text = '{"name": "小明", "age": 20}'   # 这是一串文字
data = json.loads(text)                # 把文字变成字典
print(data["name"])                    # 小明

back = json.dumps(data, ensure_ascii=False)  # 把字典变回文字
print(back)
```

- `json.loads`：文字 → 字典（load **s**tring）
- `json.dumps`：字典 → 文字（dump **s**tring）

> 💡 第 5 课会让 AI 用 JSON 格式回答，我们再用 `json.loads` 把它变成字典。

---

## 🏋️ 练习

新建 `exercise1.py`，写一个程序：

1. 建一个**列表**，里面放 3 个**字典**，每个字典代表一个问题：`{"line": 行号, "type": "bug" 或 "security", "msg": 说明}`
2. 用 `for` 把每个问题拿出来
3. 用 `if`：如果 type 是 `"security"`，前面印 `🔒`；否则印 `🐛`
4. 用 f-string 印出：`🔒 第 12 行：密码写死在代码里`

（这其实就是第 6 课"贴评论"的迷你版！）

## ✅ 完成检查
- [ ] 能解释变量、列表、字典的分别
- [ ] 知道缩进为什么重要
- [ ] 会写一个有 `return` 的函数
- [ ] 知道 `json.loads` 是做什么的
- [ ] 练习做完了

---

# 第 2 课：用 Python 调用 AI

## 🎯 目标
写出第一个会和 AI 对话的程序，并把它包装成一个函数 `ask_ai()`，以后所有课都用它。

## 💡 概念

### 什么是 API？
**比喻：餐厅点餐。**
- 你（程序）不能走进厨房（AI 公司的服务器）
- 你把菜单（请求）交给服务员（API）
- 服务员把菜（回答）端回来

### 什么是 API key？
**会员卡号**。AI 公司靠它知道是谁在用、该向谁收钱。

> 🚨 **API key = 钱。** 绝对不能：
> - 写在代码里
> - 上传到 GitHub（有机器人专门扫描偷 key）
> - 发给别人
>
> 正确做法：放在 `.env` 文件，并让 Git 忽略它（下面会教）。

### 什么是 pip？
Python 的"应用商店"。`pip install 工具名` 就能安装别人做好的工具包。

## ✋ 动手

### 步骤 1：建立项目文件夹
在"文档"里新建文件夹 `pr-review-agent`，用 VS Code 打开它。

> 第 3 课会把这个文件夹连到 GitHub。

### 步骤 2：建立 `.env` 放 key
新建文件 `.env`（注意前面有一点），内容：

```
AI_API_KEY=把你的DeepSeek key贴在这里
```

> DeepSeek key 在 platform.deepseek.com → API Keys 里建立，通常是 `sk-` 开头。等号两边不要有空格，key 也不用加引号。

### 步骤 3：建立 `.gitignore` 保护 key
新建文件 `.gitignore`，内容：

```
.env
__pycache__/
```

意思是"Git 请当作没看见这些文件"，这样 `.env` 就永远不会被上传。

### 步骤 4：安装工具包
新建 `requirements.txt`（工具包清单）：

```
requests
python-dotenv
openai
```

> 💡 **咦，用 DeepSeek 为什么要装 `openai`？** DeepSeek 故意把 API 做成跟 OpenAI 一样的格式，所以可以直接借用 OpenAI 做好的工具包，只要把"餐厅地址"改成 DeepSeek 的就行。这种做法叫"兼容"，很多 AI 公司都这样做。

| 工具包 | 用来做什么 |
|---|---|
| `requests` | 跟网站沟通（第 4 课用来跟 GitHub 沟通） |
| `python-dotenv` | 读取 `.env` 文件 |
| `openai` | 跟 DeepSeek 沟通 |

然后在终端运行：

```powershell
pip install -r requirements.txt
```

### 步骤 5：写 `ai.py`

```python
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                        # 把 .env 里的内容读进来

# 建立一个"客户端"：告诉它会员卡号（key）和餐厅地址（DeepSeek）
client = OpenAI(
    api_key=os.environ["AI_API_KEY"],
    base_url="https://api.deepseek.com",
)

MODEL = "deepseek-flash"   # 便宜、快。想要更强可以换成 "deepseek-v4-pro"


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
    # 直接运行 ai.py 时才会执行这里，用来测试
    print(ask_ai("用一句话介绍你自己"))
```

### 🔍 代码解读

| 代码 | 意思 |
|---|---|
| `OpenAI(api_key=..., base_url=...)` | 准备好"点餐工具"：带上会员卡，地址设成 DeepSeek |
| `messages=[...]` | 对话内容，是一个**列表**，里面每句话是一个**字典**（第 1 课学的！） |
| `"role": "user"` | 这句话是"用户"说的。另外还有 `"system"`（给 AI 的背景设定）和 `"assistant"`（AI 说的） |
| `response.choices[0].message.content` | AI 回来的资料包了好几层，这一串就是一层一层打开，拿出最里面的文字 |
| `MODEL` | 用哪一个模型。写成变量放在最上面，以后想换只改一个地方 |

> 💡 **`deepseek-flash` 还是 `deepseek-v4-pro`？** 学习阶段用 `flash` 就够了，又便宜又快。第 5 课如果觉得 AI 找问题不够准，可以换成 `pro` 比较看看。

> 💡 **为什么要包装成 `ask_ai()`？** 以后其他文件只要写 `ask_ai("...")` 就好，不用管背后是哪家 AI。哪天想换 AI，只改这一个文件。

### 步骤 6：运行

```powershell
python ai.py
```

看到 AI 的自我介绍，就成功了 🎉

## 🐞 常见错误

| 错误信息 | 原因 | 解决 |
|---|---|---|
| `KeyError: 'AI_API_KEY'` | 找不到 key | 检查 `.env` 名字、位置是否在项目文件夹里 |
| `ModuleNotFoundError` | 工具包没装 | 运行 `pip install -r requirements.txt` |
| `401` / `Unauthorized` | key 错了 | 重新复制 key，注意前后不要有空格 |
| `402` / `Insufficient Balance` | DeepSeek 账户没钱了 | 到 platform.deepseek.com 充值 |
| `429` | 请求太频繁 | 等一下再试 |
| `Model Not Exist` | 模型名字打错或已经改名 | 检查 `MODEL`，对照 DeepSeek 官方文档 |

## 🏋️ 练习
修改 `if __name__ == "__main__":` 下面的代码，问 AI：`"这段代码有什么问题？ def add(a, b): return a - b"`，看它能不能发现问题。

## ✅ 完成检查
- [ ] 能用自己的话解释 API 和 API key
- [ ] `.env` 和 `.gitignore` 都建好了
- [ ] `python ai.py` 成功拿到 AI 的回答
- [ ] 练习：AI 找出了 `a - b` 的问题

---

# 第 3 课：Git 和 GitHub，开出第一个 PR

## 🎯 目标
理解 commit、branch、push、PR，并亲手开出一个 PR，里面放**故意写错的代码**，给之后的 AI 审查用。

## 💡 概念（游戏比喻）

| 名词 | 意思 | 比喻 |
|---|---|---|
| **Repository（repo）** | 一个项目的所有代码和历史 | 一个游戏存档文件夹 |
| **Commit** | 存一次档，并写下这次改了什么 | 游戏存档点 |
| **Branch** | 从某个存档分出来的另一条路线 | 平行世界 |
| **main** | 主路线，正式版本 | 正史 |
| **Push** | 把电脑里的存档上传到 GitHub | 上传到云端 |
| **Pull Request（PR）** | "我在平行世界改好了，请检查后合并进正史" | 交作业请老师批改 |
| **Diff** | 这次改了哪些地方（红色删除、绿色新增） | 作业里用红笔标出的修改 |

**PR 就是 review 发生的地方**，我们的 AI 助教就在这里留言。

## ✋ 动手

### 步骤 1：在 GitHub 建立 repo
1. 打开 github.com → 右上角 **+** → **New repository**
2. Repository name：`pr-review-agent`
3. 选 **Public**（公开的 repo，GitHub Actions 完全免费）
4. **不要**勾选 "Add a README"
5. 点 **Create repository**

### 步骤 2：把电脑的文件夹连上 GitHub
在 VS Code 终端（确认是在 `pr-review-agent` 文件夹）逐行运行，`你的用户名` 换成你的 GitHub 用户名：

```powershell
git init
```

```powershell
git add .
```

```powershell
git commit -m "第一次存档：ai.py"
```

```powershell
git branch -M main
```

```powershell
git remote add origin https://github.com/你的用户名/pr-review-agent.git
```

```powershell
git push -u origin main
```

第一次 push 会弹出窗口要你登入 GitHub，按指示登入即可。

> ✅ 去 GitHub 网页刷新，应该看到 `ai.py`、`.gitignore`、`requirements.txt`，**但没有 `.env`**。如果看到 `.env`，立刻告诉我！

### 步骤 3：开一条新的 branch（平行世界）

```powershell
git checkout -b test-bugs
```

### 步骤 4：写一份"故意出错"的代码
新建文件夹 `sample`，在里面建 `shop.py`：

```python
ADMIN_PASSWORD = "admin123"


def average_price(prices):
    return sum(prices) / len(prices)


def find_user(db, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)


def apply_discount(price, percent):
    return price - price * percent / 10
```

这份代码里藏了 4 个问题（先别看答案，之后看 AI 能不能找到）：

<details>
<summary>点这里看答案</summary>

1. 🔒 密码直接写在代码里
2. 🐛 `prices` 是空列表时会除以 0，程序崩溃
3. 🔒 SQL 注入：用户输入直接拼进 SQL
4. 🐛 折扣算错：应该除以 100，不是 10

</details>

### 步骤 5：存档、上传、开 PR

```powershell
git add .
```

```powershell
git commit -m "新增 shop.py"
```

```powershell
git push -u origin test-bugs
```

然后打开 GitHub 的 repo 页面，会看到黄色提示 **"Compare & pull request"**，点它 → 点 **Create pull request**。

🎉 你的第一个 PR 完成了！记下 PR 的**编号**（标题旁边的 `#1`）。

> 🚫 **不要按 "Merge pull request"！** 这个 PR 是给 AI 练习审查用的"靶子"，要一直开着，第 4 到第 6 课都会用到它。

### 步骤 6：看看 diff
在 PR 页面点 **Files changed**，绿色的就是新增的代码。这就是之后 AI 要看的东西。

## 🏋️ 练习
在 `test-bugs` branch 再修改 `shop.py`（例如加一行注释），commit 并 push，然后回 PR 页面，看看 PR 是不是自动更新了。

## ✅ 完成检查
- [ ] 能解释 commit、branch、PR 的分别
- [ ] GitHub 上有 `pr-review-agent` repo，**没有 `.env`**
- [ ] 开出了一个 PR，里面有 `sample/shop.py`
- [ ] 记下了 PR 编号

---

# 第 4 课：用程序读取 PR 改了什么

## 🎯 目标
写程序向 GitHub 拿 PR 的 diff，并给每一行加上**行号**（之后贴评论需要知道是哪一行）。

## 💡 概念

### GitHub API
跟第 2 课一样是"点餐"，只是这次的餐厅是 GitHub。我们可以请它"给我 PR #1 改了哪些文件"。

### GitHub Token
GitHub 的"会员卡"，让程序可以代表你读取 PR、留言。

### 看懂 diff 的格式
GitHub 给我们的 diff 长这样：

```
@@ -0,0 +1,5 @@
+ADMIN_PASSWORD = "admin123"
+
+
+def average_price(prices):
+    return sum(prices) / len(prices)
```

| 符号 | 意思 |
|---|---|
| `@@ -0,0 +1,5 @@` | 区块标题。`+1,5` 意思是"新文件从第 1 行开始，共 5 行" |
| `+` 开头 | 新增的行 |
| `-` 开头 | 删掉的行 |
| 空格开头 | 没改的行（给你看上下文） |

> ⚠️ **最容易搞混的地方**：diff 里不会直接写"这是文件的第几行"，要我们自己从 `@@` 标题开始数。GitHub 留言时要的是**新文件的行号**。

## ✋ 动手

### 步骤 0：切回 main branch

```powershell
git checkout main
```

**为什么？** 从这一课开始写的是 **agent 本身的代码**（`github_api.py`、`review.py`），它们要放在**主路线 main** 上。

`test-bugs` 只放"给 AI 审查的练习代码"。如果把 agent 的代码也写在 `test-bugs`，就会混进 PR #1 里，变成 AI 在审查自己。

> 💡 切到 main 之后，左边文件列表里的 `sample` 文件夹会**消失**，这是正常的：`shop.py` 只存在于 `test-bugs` 那个平行世界。`.env` 不会消失，因为 Git 不管它。

### 步骤 1：建立 GitHub Token
1. GitHub 右上角头像 → **Settings**
2. 左边最下面 **Developer settings** → **Personal access tokens** → **Fine-grained tokens**
3. **Generate new token**
4. Token name：`pr-review-agent`；Expiration：30 天
5. Repository access：**Only select repositories** → 选 `pr-review-agent`
6. Permissions → Repository permissions：
   - **Contents**：Read-only
   - **Pull requests**：Read and write
7. 点 **Generate token**，复制它（只会显示一次！）

在 `.env` 加两行：

```
AI_API_KEY=你的AI key
GITHUB_TOKEN=刚复制的token
GITHUB_REPO=你的用户名/pr-review-agent
```

### 步骤 2：写 `github_api.py`

```python
import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPO"]
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def get_pr_files(pr_number):
    """向 GitHub 拿某个 PR 改了哪些文件。回传一个列表，每个文件是一个字典。"""
    url = f"https://api.github.com/repos/{REPO}/pulls/{pr_number}/files"
    response = requests.get(url, headers=HEADERS, params={"per_page": 100})
    response.raise_for_status()   # 如果出错（例如 404），在这里停下并显示错误
    return response.json()


def number_patch(patch):
    """
    给 diff 的每一行加上"新文件的行号"。
    回传两样东西：
      1. 加了行号的 diff 文字（给 AI 看）
      2. 可以留言的行号集合（之后用来检查 AI 说的行号对不对）
    """
    output = []
    valid_lines = set()
    line_no = 0

    for line in patch.split("\n"):
        if line.startswith("@@"):
            # 从 "@@ -0,0 +1,5 @@" 里找出 +号后面的数字，就是起始行号
            line_no = int(re.search(r"\+(\d+)", line).group(1))
            output.append(line)
        elif line.startswith("-"):
            # 删掉的行在新文件里不存在，没有行号
            output.append(f"      {line}")
        elif line.startswith("\\"):
            # "\ No newline at end of file" 这种提示，跳过
            continue
        else:
            # 新增的行（+）或没改的行（空格），都在新文件里
            output.append(f"{line_no:>5} {line}")
            valid_lines.add(line_no)
            line_no += 1

    return "\n".join(output), valid_lines


if __name__ == "__main__":
    files = get_pr_files(1)   # ← 换成你的 PR 编号
    for f in files:
        print(f"===== {f['filename']}（{f['status']}）=====")
        if "patch" in f:
            text, lines = number_patch(f["patch"])
            print(text)
            print(f"可以留言的行：{sorted(lines)}")
```

### 步骤 3：运行

```powershell
python github_api.py
```

你应该看到 `sample/shop.py` 的内容，每一行前面都有行号。

## 🔍 代码解读重点
- `requests.get(...)`：向 GitHub 发请求
- `response.json()`：把 GitHub 回的 JSON 文字变成 Python 列表（第 1 课学的！）
- `f["patch"]`：每个文件字典里，`patch` 就是 diff 文字
- `if "patch" in f`：图片等文件没有 diff，要跳过
- `set()`：集合，像列表但不会重复，检查"某个数字在不在里面"很快

## 🐞 常见错误

| 错误 | 原因 |
|---|---|
| `404 Not Found` | `GITHUB_REPO` 写错，或 PR 编号不对，或 token 没选这个 repo |
| `401 Unauthorized` | token 错了或过期 |
| `KeyError: 'GITHUB_TOKEN'` | `.env` 没加这一行 |

## 🏋️ 练习
1. 修改 `shop.py`，**删掉**一行、**修改**一行，push 后再运行，看看 `-` 开头的行是不是没有行号。
2. 回答：为什么删掉的行不能留言？

## ✅ 完成检查
- [ ] 建好 GitHub token，放进 `.env`
- [ ] 看得懂 `@@`、`+`、`-` 的意思
- [ ] `python github_api.py` 印出带行号的 diff

---

# 第 5 课：让 AI 审查代码

## 🎯 目标
把 diff 交给 AI，请它按固定格式（JSON）列出问题，然后在自己电脑上印出来。

## 💡 概念

### Prompt（提示词）= 给 AI 的工作说明书
AI 做得好不好，很大部分取决于说明书写得清不清楚。好的说明书要包含：

1. **角色**：你是谁
2. **任务**：要做什么
3. **判断标准**：什么算 bug、什么算安全问题
4. **证据要求**：必须说出"什么情况下会出错"（避免 AI 乱猜）
5. **输出格式**：用什么格式回答

### 为什么要 AI 用 JSON 回答？
如果 AI 用一般文字回答，程序看不懂"哪个文件、第几行"。用 JSON，程序就能用 `json.loads` 变成字典，准确知道每个问题在哪一行。

### 为什么要检查行号？
AI 偶尔会说错行号。如果把错的行号交给 GitHub，GitHub 会拒绝整个留言。所以我们用第 4 课的 `valid_lines` 过滤一遍。

## ✋ 动手

### 写 `review.py`

```python
import json
import sys

from ai import ask_ai
from github_api import get_pr_files, number_patch

FENCE = "`" * 3   # 三个反引号，用变量表示，避免跟 Markdown 格式冲突

PROMPT = """你是一位资深的代码审查员。请审查下面这个 Pull Request 的改动。

## 你要找三类问题
- bug：代码在某些输入或情况下会出错、崩溃或算错。例如：除以零、没检查空值、算式写错。
- security：外部输入流到危险的地方，或敏感资料外泄。例如：SQL 注入、密码写死在代码里、没有权限检查。
- quality：能运行，但难读、难维护或效率差。例如：重复代码、命名不清楚。

## 规则
1. 每个问题都必须写出 failure_scenario：具体什么输入或情况会导致什么后果。说不出来的，就不要报告。
2. 只能针对前面有行号的行留言（删掉的行没有行号，不能留言）。
3. 只报告真正的问题，最多 10 个。没有问题就回答 []。
4. suggestion 是用来"整行替换"那一行的修正代码，要保留原本的缩进。不确定怎么改就留空字符串。
5. 说明用简体中文。

## 输出格式
只输出一个 JSON 数组，不要输出任何其他文字。格式如下：
[
  {
    "path": "文件路径",
    "line": 行号（数字）,
    "category": "bug 或 security 或 quality",
    "severity": "high 或 medium 或 low",
    "title": "一句话标题",
    "explanation": "为什么这是问题",
    "failure_scenario": "什么情况下会出错、后果是什么",
    "suggestion": "修正后的代码"
  }
]

## 以下是改动（每行前面的数字是新文件的行号）
"""


def build_diff_text(files):
    """把所有文件的 diff 合成一大段文字，并记录每个文件可以留言的行号。"""
    parts = []
    valid = {}   # 例如 {"sample/shop.py": {1, 2, 3, ...}}
    for f in files:
        if "patch" not in f:
            continue
        text, lines = number_patch(f["patch"])
        valid[f["filename"]] = lines
        parts.append(f"### 文件：{f['filename']}\n{text}")
    return "\n\n".join(parts), valid


def parse_json(answer):
    """把 AI 的回答变成 Python 列表。AI 有时会用 ```json ... ``` 包起来，先去掉。"""
    text = answer.strip()
    if text.startswith(FENCE):
        text = text.split("\n", 1)[1]      # 去掉第一行 ```json
        text = text.rsplit(FENCE, 1)[0]    # 去掉最后的 ```
    return json.loads(text)


def review(pr_number):
    files = get_pr_files(pr_number)
    diff_text, valid = build_diff_text(files)
    if not diff_text:
        return []

    answer = ask_ai(PROMPT + diff_text)
    issues = parse_json(answer)

    # 只保留行号正确的问题
    good = []
    for issue in issues:
        allowed = valid.get(issue.get("path"), set())
        if issue.get("line") in allowed:
            good.append(issue)
        else:
            print(f"⚠️ 丢掉一个行号不对的问题：{issue.get('path')} 第 {issue.get('line')} 行")
    return good


if __name__ == "__main__":
    pr_number = int(sys.argv[1])   # 从命令行拿 PR 编号
    issues = review(pr_number)
    icons = {"bug": "🐛", "security": "🔒", "quality": "✏️"}
    print(f"\n共找到 {len(issues)} 个问题：\n")
    for i in issues:
        icon = icons.get(i["category"], "❓")
        print(f"{icon} [{i['severity']}] {i['path']} 第 {i['line']} 行：{i['title']}")
        print(f"   为什么：{i['explanation']}")
        print(f"   出错情况：{i['failure_scenario']}")
        if i.get("suggestion"):
            print(f"   建议改成：{i['suggestion']}")
        print()
```

### 运行（把 1 换成你的 PR 编号）

```powershell
python review.py 1
```

对照第 3 课的答案：AI 找到了几个？

## 🔍 代码解读重点
- `from ai import ask_ai`：借用第 2 课写好的函数
- `sys.argv[1]`：运行时 `python review.py 1` 里的那个 `1`
- `valid.get(path, set())`：找不到这个文件就当作空集合，不会出错
- `parse_json`：AI 的回答不一定完全听话，要做一点清理

## 🐞 常见错误

| 错误 | 原因 | 解决 |
|---|---|---|
| `json.decoder.JSONDecodeError` | AI 回答不是纯 JSON | 先 `print(answer)` 看看它回了什么，再调整 prompt |
| 一个问题都没有 | 行号全被过滤 | 印出 AI 原始回答，检查 `path` 是否跟文件名一致 |
| `IndexError: list index out of range` | 运行时忘了写 PR 编号 | 用 `python review.py 1` |
| `UnicodeEncodeError: 'gbk' codec can't encode` | 中文版 Windows 的终端印不出 emoji（🐛🔒） | 见附录 C 第 5 点 |

## 🏋️ 练习
1. 运行 3 次，结果一样吗？（AI 每次回答可能有点不同，这是正常的）
2. 修改 PROMPT 规则第 3 点，把"最多 10 个"改成"最多 2 个，只报最严重的"，看看结果有什么变化。
3. 想一想：如果把"必须写出 failure_scenario"这条规则删掉，可能会发生什么？

## ✅ 完成检查
- [ ] 能说出一个好 prompt 的 5 个部分
- [ ] `python review.py 编号` 成功印出问题清单
- [ ] AI 至少找到第 3 课藏的 4 个问题中的 3 个

---

# 第 6 课：把评论贴回 GitHub

## 🎯 目标
把 AI 找到的问题，变成 GitHub PR 上**那一行旁边的留言**，还附带"一键采纳修改"按钮。

## 💡 概念

### GitHub Review
GitHub 允许一次提交一个"review"，里面可以有：
- 一段**总结**（显示在 PR 对话里）
- 很多条**行内评论**（显示在代码那一行旁边）

### Suggestion 区块：一键采纳
如果评论里有这样一个区块：

````
```suggestion
修正后的代码
```
````

GitHub 会显示 **"Commit suggestion"** 按钮，作者按一下就能直接采纳修改。

## ✋ 动手

### 步骤 1：在 `github_api.py` 最后加一个函数
（加在 `if __name__ == "__main__":` 的**上面**）

```python
def post_review(pr_number, summary, comments):
    """在 PR 上提交一个 review：一段总结 + 多条行内评论。"""
    url = f"https://api.github.com/repos/{REPO}/pulls/{pr_number}/reviews"
    data = {
        "body": summary,
        "event": "COMMENT",      # 只留言，不批准也不拒绝
        "comments": comments,
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code >= 400:
        print(response.text)     # 出错时印出 GitHub 说了什么
    response.raise_for_status()
```

### 步骤 2：修改 `review.py`

在最上面的 import 改成：

```python
from github_api import get_pr_files, number_patch, post_review
```

在 `review()` 函数**下面**加两个新函数：

```python
ICONS = {"bug": "🐛 Bug", "security": "🔒 安全问题", "quality": "✏️ 代码质量"}
SEVERITY = {"high": "🔴 高", "medium": "🟠 中", "low": "🟢 低"}


def format_comment(issue):
    """把一个问题字典，变成 GitHub 评论的文字（Markdown 格式）。"""
    kind = ICONS.get(issue["category"], issue["category"])
    level = SEVERITY.get(issue["severity"], issue["severity"])
    body = (
        f"**{kind}｜严重度 {level}**\n\n"
        f"**{issue['title']}**\n\n"
        f"{issue['explanation']}\n\n"
        f"**会出错的情况：** {issue['failure_scenario']}"
    )
    if issue.get("suggestion"):
        body += f"\n\n**建议修改：**\n{FENCE}suggestion\n{issue['suggestion']}\n{FENCE}"
    return body


def post_issues(pr_number, issues):
    if not issues:
        summary = "🤖 AI 审查完毕：没有发现明显问题 👍"
    else:
        summary = f"🤖 AI 审查完毕：发现 {len(issues)} 个问题，请看代码旁边的留言。"

    comments = []
    for issue in issues:
        comments.append({
            "path": issue["path"],
            "line": issue["line"],
            "side": "RIGHT",           # RIGHT = 新版本那一边
            "body": format_comment(issue),
        })
    post_review(pr_number, summary, comments)
    print(f"✅ 已在 PR #{pr_number} 留下 {len(comments)} 条评论")
```

把最下面的 `if __name__ == "__main__":` 整段换成：

```python
if __name__ == "__main__":
    pr_number = int(sys.argv[1])
    issues = review(pr_number)
    post_issues(pr_number, issues)
```

### 步骤 3：运行

```powershell
python review.py 1
```

去 GitHub 的 PR 页面 → **Files changed**，你应该看到 AI 的留言出现在代码旁边 🎉

## 🐞 常见错误

| 错误 | 原因 |
|---|---|
| `422 Unprocessable Entity` + `"line must be part of the diff"` | 行号不在 diff 里（检查过滤有没有生效） |
| `403 Forbidden` | token 没有 Pull requests 的 **Read and write** 权限 |

## 🏋️ 练习
1. 在 GitHub 上点一个 **Commit suggestion**，看看代码是不是真的被改了。
2. 修改 `format_comment`，在每条评论最后加一行小字：`_由 AI 自动产生，仅供参考_`

## ✅ 完成检查
- [ ] PR 上出现 AI 的总结和行内留言
- [ ] 至少一条留言有 "Commit suggestion" 按钮
- [ ] 理解 `format_comment` 是怎样把字典变成留言文字的

---

# 第 7 课：GitHub Actions，让一切自动运行

## 🎯 目标
不用再自己运行 `python review.py`：**开 PR 或 push 新代码，AI 就自动来审查**。

## 💡 概念

### GitHub Actions
**比喻：GitHub 免费借你一台电脑，你写一张"任务卡"，告诉它什么时候做什么事。**

我们的任务卡写的是：
> **当**有 PR 开启或更新，**就**：拿代码 → 装 Python → 装工具包 → 运行 `review.py`

### Secrets
GitHub 那台电脑上没有你的 `.env`（我们故意不上传）。所以要把 key 存在 GitHub 的**保险箱（Secrets）**，任务卡运行时再拿出来用。

> 💡 GitHub Token 不用自己放：Actions 运行时会自动给一个临时的 `GITHUB_TOKEN`。

## ✋ 动手

### 步骤 1：把 AI key 放进 GitHub Secrets
1. GitHub repo 页面 → **Settings**
2. 左边 **Secrets and variables** → **Actions**
3. **New repository secret**
4. Name：`AI_API_KEY`；Secret：贴上你的 AI key
5. **Add secret**

### 步骤 2：写任务卡
切回 main branch：

```powershell
git checkout main
```

新建文件 `.github/workflows/review.yml`（注意文件夹名字有一点，`workflows` 有 s）：

```yaml
name: AI Code Review

# 什么时候运行：PR 开启、有新的 push、重新开启时
on:
  pull_request:
    types: [opened, synchronize, reopened]

# 给这个任务的权限：可以读代码、可以在 PR 留言
permissions:
  contents: read
  pull-requests: write

jobs:
  review:
    runs-on: ubuntu-latest          # 用 GitHub 的 Linux 电脑
    steps:
      - name: 拿代码
        uses: actions/checkout@v4

      - name: 安装 Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: 安装工具包
        run: pip install -r requirements.txt

      - name: AI 审查
        run: python review.py ${{ github.event.pull_request.number }}
        env:
          AI_API_KEY: ${{ secrets.AI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_REPO: ${{ github.repository }}
```

> ⚠️ YAML 文件靠**空格缩进**，不能用 Tab，每层两个空格。

### 步骤 3：上传到 main

```powershell
git add .
```

```powershell
git commit -m "加入 AI 自动审查"
```

```powershell
git push
```

### 步骤 4：测试
1. 开一条新 branch：`git checkout -b test-auto`
2. 在 `sample` 里新建一个有问题的文件（自己发挥！）
3. commit、push，在 GitHub 开 PR
4. 在 PR 页面下方会看到黄色的 **"Some checks haven't completed yet"**
5. 等一两分钟，AI 的留言就出现了 🎉🎉🎉

想看运行过程：repo 页面上方 **Actions** 分页 → 点进那次运行 → 可以看到每一步的输出。

## 🐞 常见错误

| 情况 | 原因 |
|---|---|
| Actions 分页没有任何运行 | `review.yml` 位置或名字错了，或没有 push 到 main |
| `KeyError: 'AI_API_KEY'` | Secret 名字打错（大小写也要一样） |
| `403` 留言失败 | `permissions` 那段漏了或缩进错了 |
| 别人 fork 你的 repo 开 PR，审查失败 | 安全设计：fork 来的 PR 拿不到你的 Secrets（防止别人偷 key） |

## 🏋️ 练习
1. 在已经开着的 PR 里再 push 一次，看看 AI 是不是又审查了一遍。
2. 想一想：每次 push 都审查一次，可能有什么缺点？（提示：钱、重复留言）

## ✅ 完成检查
- [ ] `AI_API_KEY` 放进 GitHub Secrets
- [ ] 开新 PR 后，AI 自动留言
- [ ] 会在 Actions 分页看运行记录
- [ ] 🏆 **恭喜！基础版 PR Review Agent 完成！**

---

# 🚀 之后可以升级的方向

| 升级 | 解决什么问题 | 难度 |
|---|---|---|
| 不重复留言 | 每次 push 都会留一堆一样的评论 | ⭐⭐ |
| 跳过太大的 PR / 不审查图片、锁定文件 | 省钱、避免 AI 看不完 | ⭐⭐ |
| 把整个文件（不只 diff）给 AI 看 | AI 更懂上下文，找得更准 | ⭐⭐⭐ |
| 第二轮 AI 验证 | 减少误报 | ⭐⭐⭐ |
| 加入 linter / Semgrep | 用规则工具抓确定的问题 | ⭐⭐⭐ |
| 在 PR 里打 `/review` 才运行 | 让人决定什么时候审查 | ⭐⭐⭐ |
| 读取项目的规则文件（例如团队写代码的规定） | 按团队标准审查 | ⭐⭐⭐⭐ |

---

# 📖 附录 A：名词表

| 名词 | 一句话解释 |
|---|---|
| Agent | 能自己完成一连串步骤的 AI 程序 |
| API | 程序跟程序沟通的"点餐窗口" |
| API key / Token | 使用 API 的"会员卡"，等于钱和权限，要保密 |
| Repository（repo） | 一个项目的代码和全部历史 |
| Commit | 存一次档 |
| Branch | 平行世界，在这里改不影响 main |
| Push | 把存档上传到 GitHub |
| Pull Request（PR） | 请别人检查并合并你的修改 |
| Diff | 改动的内容（新增、删除） |
| JSON | 程序之间传资料的文字格式 |
| Prompt | 给 AI 的工作说明书 |
| GitHub Actions | GitHub 借你的自动运行电脑 |
| Secrets | GitHub 上放密码的保险箱 |
| Linter | 检查代码风格和简单错误的工具，每种语言有自己的 |
| Semgrep | 跨语言的安全问题扫描工具 |

# 📖 附录 B：常用命令速查

| 想做什么 | 命令 |
|---|---|
| 运行 Python 文件 | `python 文件名.py` |
| 安装工具包 | `pip install -r requirements.txt` |
| 看现在在哪条 branch、改了什么 | `git status` |
| 开新 branch 并切过去 | `git checkout -b 名字` |
| 切换 branch | `git checkout 名字` |
| 准备存档（全部文件） | `git add .` |
| 存档 | `git commit -m "说明"` |
| 上传 | `git push` |
| 第一次上传新 branch | `git push -u origin 名字` |

# 📖 附录 C：遇到问题怎么办

1. **先看错误信息的最后一行**，通常最重要
2. 把**完整的**错误信息复制下来（不要只截一半）
3. 说清楚：你在做第几课第几步、运行了什么命令
4. 贴给 AI 助手一起看
5. **看到 `UnicodeEncodeError: 'gbk' codec ...`**：中文版 Windows 的终端默认编码印不出 emoji。在终端先运行下面这行，再运行你的程序（只对当前终端窗口有效）：

   ```powershell
   $env:PYTHONUTF8 = "1"
   ```

> 🚨 贴错误信息之前，确认里面**没有你的 API key 或 token**。
