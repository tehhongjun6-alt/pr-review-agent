# 🤖 PR Review Agent 学习手册（零基础版）

> **最终目标**：在 GitHub 开一个 Pull Request（PR），几分钟后，AI 自动读你改了什么，找出 bug、安全问题、写得不好的地方，然后在那几行代码旁边留言，告诉你怎么改。

---

## 📍 我的进度

完成一课就把 `[ ]` 改成 `[x]`。

- [x] 第 0 课：准备工具
- [x] 第 1 课：Python 最基础的部分
- [x] 第 2 课：用 Python 调用 AI
- [x] 第 3 课：Git 和 GitHub，开出第一个 PR
- [x] 第 4 课：用程序读取 PR 改了什么
- [x] 第 5 课：让 AI 审查代码
- [x] 第 6 课：把评论贴回 GitHub
- [x] 第 7 课：GitHub Actions，让一切自动运行
- [ ] 第 8 课：Tool Use，变成真正的 agent
- [ ] 第 9 课：不会挂掉
- [ ] 第 10 课：不重复留言
- [ ] 第 11 课：测试题 + 成绩单
- [ ] 第 12 课：减少误报

**我用的 AI 供应商**：DeepSeek（经过中转站，模型 `deepseek-v4.1-flash`）

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

# 🧭 第 8–12 课总览：从「能用」到「合格中上」

> 📌 从第 8 课开始，代码**以你实际的文件为准**：`ai.py`、`github_api.py`（里面有 `add_line_numbers`、`post_review`）、`try_review.py`。前面第 5–7 课手册里的 `review.py`、`number_patch` 是旧名字，不用管。

| 课 | 做什么 | 解决什么 | 难度 |
|---|---|---|---|
| 8 | Tool Use + 3 道安全门 | AI 看得到上下文，又不会乱查 | ⭐⭐⭐ |
| 9 | 不会挂掉 | 一个小错误就整个停掉 | ⭐⭐ |
| 10 | 不重复留言 | 每次 push 都多一套留言 | ⭐⭐ |
| 11 | 测试题 + 成绩单 | 证明它真的有用 | ⭐⭐⭐ |
| 12 | 减少误报 | AI 乱报不存在的 bug | ⭐⭐⭐ |

### 🌳 从第 8 课开始照团队规矩

每一课都这样做：

```
1. git checkout main → git pull                 （拿最新的正式版）
2. git checkout -b lesson-X                     （开新草稿本）
3. 写代码 → git add → git commit → git push -u origin lesson-X
4. 在 GitHub 开 PR：lesson-X → main
5. 🤖 你自己做的 AI 审查员会自动来审查你的新代码！
6. 看完留言、没问题 → 按 Merge → 回到第 1 步做下一课
```

> 💡 第一次 push 新 branch 要用 `git push -u origin lesson-X`，之后同一个 branch 只要 `git push`。
> ⚠️ PR #1（test-bugs）**还是不要 merge**，它是练习材料。

### 💰 关于花费

每次 PR 有 push，GitHub 就会自动跑一次审查（会用 DeepSeek 额度）。第 11 课的考试一次会问 AI 大约 12–40 次。都不贵，但心里要有数。

---

# 第 8 课：Tool Use，变成真正的 agent

## 🎯 目标
不再只把 diff 塞给 AI，而是**给 AI 两个工具，让它自己决定要查什么**。

## 💡 为什么
只看 diff，AI 看不到上下文。例如 PR 用了 `calculate_price()`，但这个函数写在别的文件，AI 就看不到它，可能漏掉 bug，或者**乱猜**（幻觉）。把整个项目都给 AI 又太浪费 token。

## 🕵️ 比喻：侦探 + 助手

AI 是**侦探**，坐在办公室里**不能出门**（AI 不能自己读你电脑的文件）。你的程序是**助手**，帮它跑腿。

```
侦探（AI）：「calculate_price 在哪里？」     → 说：我要用 search_code
助手（程序）：去搜 → 「在 utils/price.py 第 20 行」
侦探：「把那个文件拿给我」                   → 说：我要用 read_file
助手：去读 → 交回内容
侦探：「看完了，第 22 行没处理负数！」        → 输出 JSON 答案 ✅
```

⚠️ 重点：**AI 自己不执行工具**，它只是**说**「我想用这个工具」，真正去做的是**你的程序**。

## 🛡️ 3 道安全门（防止幻觉、防止乱查）

| 安全门 | 做法 | 防什么 |
|---|---|---|
| ① 次数限制 | 最多 5 轮工具，到了就要交答案 | 越查越远、花太多钱 |
| ② 大小限制 | `read_file` 一次最多 100 行；`search_code` 最多 20 个结果；不能读 `.env` 和项目外的文件 | 记忆塞爆、偷看密码 |
| ③ 行号检查 | AI 说「第 X 行」，程序检查这一行**真的在改动里**，不在就丢掉 | 行号乱写、挑旧代码的毛病 |

> 💡 **永远不要 100% 相信 AI 的输出，要让程序去检查它。**

---

## 8.1 开新 branch

```powershell
git checkout main
```
```powershell
git pull
```
```powershell
git checkout -b lesson-8
```

- `git pull`：把 GitHub 上最新的版本拉下来
- `git checkout -b lesson-8`：**新开**一个叫 `lesson-8` 的 branch 并切过去（`-b` = 新开；没有 `-b` = 切换到已经存在的）

✅ 检查：VS Code 左下角显示 `lesson-8`，或 `git branch` 看到 `* lesson-8`。

---

## 8.2 先测试：中转站支不支持 Tool Use？

不是每个 AI 服务都支持 Tool Use。如果你的中转站不支持，后面都做不了，所以**先花一点点额度测试**。

新建 `test_tools.py`：

```python
from ai import client, MODEL

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询某个城市现在的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名字"},
                },
                "required": ["city"],
            },
        },
    },
]

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "吉隆坡现在天气怎样？"}],
    tools=tools,
)

message = response.choices[0].message
print("AI 想用工具吗？", message.tool_calls)
print("AI 的文字回答：", message.content)
```

运行：

```powershell
python test_tools.py
```

**看结果：**

| 看到 | 意思 |
|---|---|
| `AI 想用工具吗？ [ChatCompletionMessageToolCall(... name='get_weather', arguments='{"city": "吉隆坡"}' ...)]` | ✅ **支持！** 继续 8.3 |
| `AI 想用工具吗？ None`，然后 AI 用文字回答（例如「我无法查询天气」） | ❌ 不支持，或者这个模型不支持。先停下来，问 AI 助手怎么办（可能要换模型名字或换官方 API） |
| 出现错误（400 之类） | ❌ 把错误贴给 AI 助手（不要贴 key） |

> 💡 注意：这里**没有**真的天气工具！AI 只是**说**它想用 `get_weather`，并且自己从问题里找出参数 `city = 吉隆坡`。这就是 Tool Use 的核心。

---

## 8.3 写两个工具：新建 `tools.py`

```python
import os

PROJECT_DIR = os.path.abspath(".")
MAX_LINES = 100
MAX_RESULTS = 20
SKIP_FOLDERS = [".git", "__pycache__", "venv", ".venv", "node_modules"]


def is_safe(path):
    full = os.path.abspath(path)
    if not full.startswith(PROJECT_DIR + os.sep):
        return False
    if os.path.basename(full) == ".env":
        return False
    for part in full.split(os.sep):
        if part in SKIP_FOLDERS:
            return False
    return True


def read_file(path, start=1, end=None):
    if not is_safe(path):
        return "错误：不能读这个文件"
    if not os.path.isfile(path):
        return "错误：找不到这个文件"

    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    if start < 1:
        start = 1
    if end is None or end > start + MAX_LINES - 1:
        end = start + MAX_LINES - 1
    if end > len(lines):
        end = len(lines)

    result = []
    for no in range(start, end + 1):
        result.append(f"{no:>4} {lines[no - 1].rstrip()}")

    if not result:
        return "（这个范围没有内容）"
    return "\n".join(result)


def search_code(keyword):
    results = []
    for folder, subfolders, filenames in os.walk("."):
        subfolders[:] = [d for d in subfolders if d not in SKIP_FOLDERS]
        for name in filenames:
            if name == ".env":
                continue
            path = os.path.join(folder, name)[2:].replace("\\", "/")
            try:
                with open(path, encoding="utf-8") as f:
                    for no, line in enumerate(f, start=1):
                        if keyword in line:
                            results.append(f"{path}:{no}: {line.strip()}")
                            if len(results) >= MAX_RESULTS:
                                return "\n".join(results) + "\n（结果太多，只显示前 20 个）"
            except UnicodeDecodeError:
                continue

    if not results:
        return "找不到"
    return "\n".join(results)
```

### 📖 逐段解释

**`is_safe`：安全检查员 🛡️（安全门 ②）**
- `os.path.abspath(path)`：把路径变成完整的地址，例如 `C:\Users\...\pr-review-agent\ai.py`
- 不在项目文件夹里面的 → ❌（防止 AI 读 `../../别的东西`）
- 文件名是 `.env` → ❌（**密码绝对不给 AI 看**）
- 在 `.git`、`venv` 这些文件夹里的 → ❌

**`read_file`：读文件 📄**
- 先过安全检查，再检查文件存不存在
- 一次最多读 `MAX_LINES`（100）行，防止一下子塞太多（安全门 ②）
- 每一行前面加上行号，AI 才说得出「第几行」

**`search_code`：搜索 🔍**
- `os.walk(".")`：一个一个文件夹走进去，看每个文件
- `subfolders[:] = ...`：告诉它**不要走进** `.git` 这些文件夹
- 一行一行看，有 `keyword` 就记下「文件:行号: 内容」
- 最多 20 个结果（安全门 ②）
- `except UnicodeDecodeError: continue`：遇到图片这种不是文字的文件，**跳过**，不要报错

### ✅ 测试一下

在 `tools.py` **最下面**暂时加：

```python
if __name__ == "__main__":
    print(read_file("ai.py", 1, 10))
    print("-----")
    print(search_code("def "))
    print("-----")
    print(read_file(".env"))
```

```powershell
python tools.py
```

应该看到：`ai.py` 前 10 行（有行号）→ 项目里所有 `def` 的位置 → `错误：不能读这个文件` ✅（`.env` 被挡住了！）

> 这个测试不用 AI，**不花钱**。看完可以留着，下一步会把它移到最下面。

---

## 8.4 向 AI 介绍工具：`TOOLS` + `run_tool`

AI 不会看你的 Python 代码，它只看**说明书**：工具叫什么、做什么、要什么参数。

在 `tools.py` 里，**`if __name__ == "__main__":` 的上面**加：

```python
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "读取项目里某个文件的内容。一次最多 100 行。",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "文件路径，例如 sample/shop.py"},
                    "start": {"type": "integer", "description": "从第几行开始，默认 1"},
                    "end": {"type": "integer", "description": "读到第几行"},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_code",
            "description": "在整个项目里搜索一个词，例如函数名字。会回传：文件:行号: 那一行的内容",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "要搜索的词，例如 def calculate_price"},
                },
                "required": ["keyword"],
            },
        },
    },
]


def run_tool(name, args):
    if name == "read_file":
        return read_file(args["path"], args.get("start", 1), args.get("end"))
    if name == "search_code":
        return search_code(args["keyword"])
    return "错误：没有这个工具"
```

### 📖 解释

| 部分 | 意思 |
|---|---|
| `name` | 工具名字，AI 要用时会说这个名字 |
| `description` | **最重要！** AI 靠这句话决定什么时候用这个工具，要写清楚 |
| `properties` | 有哪些参数，每个是什么类型（`string` 文字、`integer` 整数） |
| `required` | 哪些参数**一定要给** |
| `run_tool` | 🔀 **接线员**：AI 说「我要用 read_file」，它就去叫真正的 `read_file` 函数 |

> 💡 `args.get("start", 1)`：AI 没给 start，就用 1（跟第 7 课的 `os.environ.get` 一样道理）。

---

## 8.5 对话循环：在 `ai.py` 加 `ask_ai_with_tools`

这是整个 agent 的**心脏** ❤️

**① `ai.py` 最上面**，把 import 改成这样（多了 `import json` 和最后一行）：

```python
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools import TOOLS, run_tool
```

**② `MODEL = ...` 那一行下面**加：

```python
MAX_ROUNDS = 5
```

**③ `ask_ai` 函数下面、`if __name__ == "__main__":` 上面**，加：

```python
def ask_ai_with_tools(prompt):
    """跟 ask_ai 一样，但 AI 可以先用工具查资料，查完再回答。"""
    messages = [
        {"role": "user", "content": prompt},
    ]

    for round_no in range(MAX_ROUNDS):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
        )
        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

        messages.append(message)

        for call in message.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments)
            print(f"🔧 第 {round_no + 1} 轮：AI 使用工具 {name} {args}")
            result = run_tool(name, args)
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            })

    messages.append({
        "role": "user",
        "content": "工具次数用完了。请根据目前看到的资料，直接给出最后的答案。",
    })
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="none",
    )
    return response.choices[0].message.content
```

### 📖 逐段解释

**`messages`：对话记录 📜**
AI **没有记忆**，每一轮都要把**整段对话**交回给它，它才知道之前发生了什么。所以用一个列表，一直往后面加。

**`for round_no in range(MAX_ROUNDS)`：最多 5 轮（安全门 ①）**

每一轮：
1. 把对话记录 + 工具说明书（`tools=TOOLS`）交给 AI
2. `if not message.tool_calls: return ...` → AI **没有要用工具** = 它已经想好答案了，**直接回传**，结束 ✅
3. AI 要用工具 → 先把 AI 这句话加进记录（`messages.append(message)`）
4. AI 一次可能要用好几个工具，所以 `for call in ...` 一个一个处理：
   - `json.loads(call.function.arguments)`：AI 给的参数是 JSON 文字，变成 Python 字典
   - `run_tool(...)`：**助手去跑腿** 🏃
   - 把结果用 `"role": "tool"` 加进记录，`tool_call_id` 告诉 AI「这是你刚才那个要求的结果」
5. 回到第 1 步，带着新资料再问 AI

**5 轮用完还没答案？**
加一句「工具次数用完了，直接回答」，并设定 `tool_choice="none"` = **这次不准再用工具**，逼它交答案。

### 🔁 图解

```
第 1 轮：程序 → AI：问题 + 工具说明书
         AI → 程序：「我要 search_code("def calculate_price")」
         程序：执行 → 把结果加进记录
第 2 轮：程序 → AI：问题 + 第 1 轮的全部记录
         AI → 程序：「我要 read_file("utils/price.py", 20, 40)」
         程序：执行 → 加进记录
第 3 轮：程序 → AI：全部记录
         AI → 程序：没有要用工具，直接给 JSON 答案 → 结束 ✅
```

---

## 8.6 接进 `try_review.py` + 行号检查（安全门 ③）

### ① `github_api.py`：加一个「哪些行号可以留言」的函数

在 `add_line_numbers` 函数**下面**加：

```python
def get_valid_lines(patch):
    valid = set()
    line_no = 0

    for line in patch.split("\n"):
        if line.startswith("@@"):
            start = line.split(" ")[2]
            start = start[1:]
            start = start.split(",")[0]
            line_no = int(start)
        elif line.startswith("-") or line.startswith("\\"):
            continue
        else:
            valid.add(line_no)
            line_no = line_no + 1

    return valid
```

跟 `add_line_numbers` 几乎一样的逻辑，但不是印出来，而是把**有行号的行**收集进一个 `set`（集合，像一袋号码牌 🎟️）。之后 AI 说「第 X 行」，就看 X 在不在袋子里。

### ② `try_review.py` 改 4 个地方

**(a) 最上面两行 import 改成：**

```python
from ai import ask_ai_with_tools
from github_api import files, add_line_numbers, get_valid_lines, post_review
```

（`import json` 留着）

**(b) 整个 `question = """..."""` 换成：**

```python
question = """你是一位代码审查员。请检查下面这个 PR 的改动，找出 bug 和安全问题。

每一行前面的数字是行号。
每个文件前面有「===== 文件：xxx =====」，path 要填那个文件名。

你有两个工具可以用：
- search_code：在项目里搜索一个词（例如函数名字），看它在哪里
- read_file：读取项目里某个文件
如果改动用到了别的地方定义的函数或变量，而你需要看它怎么写才能判断，就用工具去查。
不需要的话，就不要用。

注意：只能对改动里有行号的行提出问题。

只能用 JSON 格式回答，不要输出任何其他文字。格式如下：
[
    {"path": "文件名", "line": 行号, "category": "bug 或 security", "title": "一句话说明问题", "suggestion": "怎么改"}
]
如果没有问题，就回答 []

代码：
""" + code
```

**(c) `answer = ask_ai(question)` 改成：**

```python
answer = ask_ai_with_tools(question)
```

**(d) 在 `issues = json.loads(answer)` 的下面**，加上行号检查：

```python
valid = {}
for f in files:
    if "patch" in f:
        valid[f["filename"]] = get_valid_lines(f["patch"])

good_issues = []
for issue in issues:
    path = issue["path"]
    line = int(issue["line"])
    if path in valid and line in valid[path]:
        issue["line"] = line
        good_issues.append(issue)
    else:
        print(f"⚠️ 丢掉：{path} 第 {line} 行不在这次的改动里")
issues = good_issues
```

- `valid`：每个文件一袋号码牌，例如 `{"sample/shop.py": {1, 2, 3, ..., 14}}`
- `int(issue["line"])`：AI 有时候把行号写成文字 `"9"`，`int` 把它变成数字 `9`
- 文件和行号都对 → 放进 `good_issues`；不对 → 印出来、丢掉

---

## 8.7 Push + 开 PR，让 agent 审查第 8 课的代码 🔁

```powershell
git add .
```
```powershell
git status
```
👀 应该看到：`tools.py`、`test_tools.py`、`ai.py`、`github_api.py`、`try_review.py`。**没有 `.env`**。

```powershell
git commit -m "第 8 课：Tool Use"
```
```powershell
git push -u origin lesson-8
```

然后：
1. 打开 GitHub 的 repo，按黄色横幅的 **Compare & pull request**
2. 确认是 `base: main` ← `compare: lesson-8`
3. 按 **Create pull request**
4. 去 **Actions** 看它跑，展开 **Run python try_review.py**，找 🔧 那几行：**AI 自己决定用了哪些工具！**
5. 回到 PR 看 AI 对你代码的留言

### 🤔 看留言的心态
AI 可能会挑你代码的毛病。**看一看，想一想它说得对不对**，这就是 code review 的意义。
- 说得对 → 改代码，再 push，AI 会再审查一次
- 说得不对（误报）→ 记下来，第 12 课就是解决这个问题
- 看完 → 按 **Merge pull request** ✅

> ⚠️ 有可能 AI 说了一个 `test_tools.py` 或其他文件的问题，你看不懂，可以贴给 AI 助手一起看。

## ✅ 第 8 课完成标准
- [ ] `test_tools.py` 证明中转站支持 Tool Use
- [ ] `python tools.py` 读得到文件、挡得住 `.env`
- [ ] Actions 记录里看到 🔧 AI 使用工具（AI 觉得不需要的话也可能不用，这是正常的）
- [ ] lesson-8 PR merge 进 main

## 🆘 常见问题
| 问题 | 解决 |
|---|---|
| `ImportError: cannot import name 'TOOLS'` | `tools.py` 有没有存档？`TOOLS` 拼写（全大写）？ |
| `KeyError: 'path'` | AI 的 JSON 少了 path，再跑一次；第 9 课会让程序更耐打 |
| 400 错误，提到 `reasoning_content` | 某些「思考型」模型的工具循环需要特别处理，贴错误给 AI 助手 |
| 🔧 一直用工具到第 5 轮 | 正常，安全门 ① 在保护你，它会被逼着交答案 |

---

# 第 9 课：不会挂掉

## 🎯 目标
现在只要**一个小地方出错**，整个程序就停掉，而且**没有人知道**。这一课让它：
1. AI 回答格式坏了 → **再问一次**
2. 图片、文档、太大的文件 → **跳过**
3. 真的失败了 → **在 PR 留言说「审查失败」**，不会默默消失

## 9.0 开新 branch

```powershell
git checkout main
```
```powershell
git pull
```
```powershell
git checkout -b lesson-9
```

---

## 9.1 `github_api.py`：清理 + 出错要大声说

**① 删掉**这段（第 4 课留下的「印出全部文件」，遇到图片会报错 `KeyError: 'patch'`）：

```python
for f in files:
    print(f"===== {f['filename']}（{f['status']}）=====")
    print(add_line_numbers(f["patch"]))
```

**② 拿文件的地方**，改成这样：

```python
url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}/files?per_page=100"
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(url, headers=headers)
response.raise_for_status()
files = response.json()
```

- `?per_page=100`：GitHub 默认一次只给 **30 个**文件，改成最多 100 个
- `response.raise_for_status()`：如果 GitHub 回应 4xx/5xx（例如 token 过期），**马上报错停下**，而不是带着错误资料继续跑，最后出现一个看不懂的错误

**③ `post_review` 最后**加一行（跟 `if` 同一层，4 个空格）：

```python
    if response.status_code >= 400:
        print(response.text)
    response.raise_for_status()
```

之前贴留言失败（例如 422），程序只是印出来，GitHub Actions 还是显示 ✅ 绿色。现在失败会变 ❌ 红色，你才知道出事了。

---

## 9.2 AI 格式坏了就再问一次：新建 `review_core.py`

```python
import json


def parse_json(answer):
    """从 AI 的回答里找出 [ ... ]，变成 Python 的列表。找不到就报错 ValueError。"""
    start = answer.find("[")
    end = answer.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("回答里找不到 [ ]")
    return json.loads(answer[start:end + 1])
```

比第 5 课的 `removeprefix("```json")` **更耐打**：不管 AI 在 JSON 前后加了什么废话，都只拿**第一个 `[` 到最后一个 `]`** 中间的部分。
- `find`：从左边找；`rfind`：从**右**边找（r = right）
- 找不到 → `raise ValueError`：主动报错

然后在 `try_review.py`：

**① 最上面**加：

```python
from review_core import parse_json
```

**② 把这 3 行：**

```python
answer = answer.strip()
answer = answer.removeprefix("```json").removesuffix("```").strip()
issues = json.loads(answer)
```

**换成：**

```python
try:
    issues = parse_json(answer)
except ValueError:
    print("⚠️ AI 的回答格式不对，再问一次")
    answer = ask_ai_with_tools(question + "\n\n上次你的回答格式不对。这次只能输出 JSON 数组，第一个字必须是 [")
    print(answer)
    issues = parse_json(answer)
```

### 📖 `try` / `except`：新概念！
```
try:          ← 「试试看做这件事」
    ...
except 错误类型:   ← 「如果出现这种错误，不要整个停掉，改做这个」
    ...
```
第二次还是失败 → 就让它报错停下（再问也没用了）。

> 💡 `json.loads` 失败时的错误 `JSONDecodeError` 也算一种 `ValueError`，所以一个 `except ValueError` 两种都接得住。

---

## 9.3 跳过不用审查的文件

`try_review.py` 最上面（import 下面）加：

```python
import sys

SKIP_ENDINGS = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".lock", ".md")
MAX_PATCH_LINES = 400
```

（`import sys` 放在最上面跟其他 import 一起）

然后把**整个「串起所有文件」的 for 循环**，还有 8.6 加的 `valid = {}` 那段 for 循环，**合并换成**：

```python
code = ""
valid = {}
skipped = []

for f in files:
    name = f["filename"]
    if "patch" not in f or f["status"] == "removed" or name.endswith(SKIP_ENDINGS):
        skipped.append(name)
        continue
    if len(f["patch"].split("\n")) > MAX_PATCH_LINES:
        skipped.append(name + "（改动太大）")
        continue
    code = code + f"\n===== 文件：{name} =====\n" + add_line_numbers(f["patch"]) + "\n"
    valid[name] = get_valid_lines(f["patch"])

if skipped:
    print("⏭️ 跳过这些文件：", skipped)

if code == "":
    print("没有需要审查的代码，结束。")
    sys.exit()
```

> ⚠️ 记得**删掉** 8.6 在 `issues = ...` 下面加的那段 `valid = {}` + `for f in files:`（现在 `valid` 在上面就做好了）。`good_issues` 那段**留着**。

### 📖 解释
| 跳过 | 为什么 |
|---|---|
| 没有 `patch` | 图片之类，GitHub 不给 diff |
| `status == "removed"` | 删掉的文件，没有新代码可以审查 |
| `.endswith(SKIP_ENDINGS)` | 图片、PDF、锁定文件、Markdown 文档，不是代码 |
| 超过 400 行 | 太大，AI 看不完又贵（安全门 ②的延伸） |
| `sys.exit()` | 全部都跳过了 → 直接结束，不浪费钱问 AI |

> 💡 `endswith` 可以接一个 tuple `( ... )`，意思是「以其中**任何一个**结尾」。

---

## 9.4 真的失败了 → 在 PR 留言

打开 `.github/workflows/review.yml`：

**① `permissions:` 加一行：**

```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

**② 最下面加一个新步骤**（跟 `- run: python try_review.py` 同一层，6 个空格开头）：

```yaml
      - name: 审查失败时留言
        if: failure()
        run: gh pr comment ${{ github.event.pull_request.number }} --body "🤖 AI 审查失败了，请到 Actions 看错误记录。"
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 📖 解释
- `if: failure()`：**只有前面有步骤失败**才做这一步（平常不会做）
- `gh`：GitHub 官方的命令行工具，GitHub 的电脑已经装好了
- `gh pr comment 编号 --body "..."`：在 PR 留一则普通留言
- `issues: write`：PR 的普通留言，在 GitHub 内部算是 issue 留言，所以要这个权限

---

## 9.5 Push + 开 PR

```powershell
git add .
```
```powershell
git status
```
```powershell
git commit -m "第 9 课：不会挂掉"
```
```powershell
git push -u origin lesson-9
```

在 GitHub 开 PR（lesson-9 → main），看 Actions：
- 记录里应该看到 `⏭️ 跳过这些文件` 吗？这次没有改 .md 或图片，所以**可能没有**，正常
- 留言正常出现 ✅ → Merge

## ✅ 第 9 课完成标准
- [ ] 遇到图片不会 `KeyError`
- [ ] AI 格式坏了会再问一次
- [ ] 失败时 Actions 变红，PR 出现「审查失败」留言
- [ ] lesson-9 merge 进 main

---

# 第 10 课：不重复留言

## 🎯 目标
现在每 push 一次，同一个问题就多一则留言，PR 越来越乱。这一课：**以前留过的，就不要再留。**

## 💡 怎么知道哪些是「我留的」？
在每则 AI 留言最后，偷偷加一个**隐形记号**：

```
<!-- ai-review -->
```

这是 HTML 的「注解」，GitHub 显示留言时**看不到**，但程序读得到。
> 🏷️ 比喻：在自己的作业纸背面签一个小名，别人看不到，自己认得出。

下次运行时：
1. 先去 GitHub 拿这个 PR **全部旧留言**
2. 找出有记号的 → 记下「哪个文件、哪一行」
3. 新问题如果在**同一个文件同一行** → 跳过

## 10.0 开新 branch

```powershell
git checkout main
```
```powershell
git pull
```
```powershell
git checkout -b lesson-10
```

## 10.1 `github_api.py` 最下面加

```python
MARKER = "<!-- ai-review -->"


def get_old_comment_lines():
    comments_url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}/comments?per_page=100"
    response = requests.get(comments_url, headers=headers)
    response.raise_for_status()

    old = set()
    for c in response.json():
        if MARKER in c["body"]:
            old.add((c["path"], c["line"]))
    return old
```

- `/pulls/{编号}/comments`：拿这个 PR 所有**代码旁边的留言**
- `if MARKER in c["body"]`：只看**有记号**的（人写的留言不算）
- `(c["path"], c["line"])`：两个东西用括号包起来 = 一个 **tuple**（一对），例如 `("sample/shop.py", 5)`

## 10.2 `try_review.py` 改 3 个地方

**① import 那一行**改成：

```python
from github_api import files, add_line_numbers, get_valid_lines, post_review, get_old_comment_lines, MARKER
```

**② 「贴评语」部分**：在 `comments = []` **上面**加一行，在 `for issue in issues:` **里面最前面**加跳过：

```python
old = get_old_comment_lines()
comments = []

for issue in issues:
    if (issue["path"], issue["line"]) in old:
        print(f"⏭️ 第 {issue['line']} 行以前留过言了，跳过")
        continue

    if issue["category"] == "security":
```

（下面的 `icon`、`body` 照旧）

**`body` 那一行**最后加上记号：

```python
    body = f"**{icon}**\n\n{issue['title']}\n\n**建议：** {issue['suggestion']}\n\n{MARKER}"
```

**③ 最后两行**（`summary = ...` 和 `post_review(...)`）换成：

```python
if comments:
    summary = f"🤖 AI 审查完毕，发现 {len(comments)} 个新问题，请看代码旁边的留言。"
    post_review(summary, comments)
else:
    print("没有新问题，这次不留言。")
```

没有新问题 → **完全不留言**，不刷屏。

## 10.3 测试

```powershell
git add .
```
```powershell
git commit -m "第 10 课：不重复留言"
```
```powershell
git push -u origin lesson-10
```

开 PR（lesson-10 → main），等 AI 留言。然后**再按一次门铃**：

```powershell
git commit --allow-empty -m "测试不重复"
```
```powershell
git push
```

第二次的 Actions 记录应该看到 `⏭️ 第 X 行以前留过言了，跳过` 或 `没有新问题，这次不留言。` ✅

> ⚠️ **已知限制**：如果你在问题**上面**加了几行代码，问题的行号会往下移，程序会以为是新问题，再留一次。顶级产品会比对问题内容，不只比对行号。现在先接受这个限制。
> 💡 第 10 课之前留下的旧留言没有记号，所以**不会**被认出来，这是正常的。

## ✅ 第 10 课完成标准
- [ ] 第二次 push，同一行不会再留言
- [ ] lesson-10 merge 进 main

---

# 第 11 课：测试题 + 成绩单 📊

## 🎯 目标
到现在为止，我们只用 `shop.py` 测过。它**真的准吗**？会不会漏？会不会乱报？
这一课做一份**考卷**：12 题，10 题有 bug，2 题是**正确的代码**（用来抓误报）。跑完得到一张成绩单：

```
✅ 抓到：8 / 10
❌ 漏掉：2
🚨 误报：1
```

> 💡 **面试最加分的就是这个**：你不只做出东西，还能**用数字证明**它有用。以后改 prompt、换模型，跑一次考试就知道变好还是变坏。

## 11.0 开新 branch

```powershell
git checkout main
```
```powershell
git pull
```
```powershell
git checkout -b lesson-11
```

## 11.1 整理：把「审查的核心」搬进 `review_core.py`

考试程序也要用**一模一样**的审查流程。但 `try_review.py` 一 import 就会跑（去 GitHub 拿 PR），没办法借用。
所以把「问 AI → 读懂 JSON → 检查行号」搬进 `review_core.py` 的一个函数 `review_code(code, valid)`，两边都叫它。

> 🍳 比喻：把厨师的**招牌菜做法**写成食谱，餐厅（try_review）和考试（run_eval）用同一本食谱。

**`review_core.py` 整个换成：**

```python
import json

from ai import ask_ai_with_tools


def build_question(code):
    return """你是一位代码审查员。请检查下面这个 PR 的改动，找出 bug 和安全问题。

每一行前面的数字是行号。
每个文件前面有「===== 文件：xxx =====」，path 要填那个文件名。

你有两个工具可以用：
- search_code：在项目里搜索一个词（例如函数名字），看它在哪里
- read_file：读取项目里某个文件
如果改动用到了别的地方定义的函数或变量，而你需要看它怎么写才能判断，就用工具去查。
不需要的话，就不要用。

注意：只能对改动里有行号的行提出问题。

只能用 JSON 格式回答，不要输出任何其他文字。格式如下：
[
    {"path": "文件名", "line": 行号, "category": "bug 或 security", "title": "一句话说明问题", "suggestion": "怎么改"}
]
如果没有问题，就回答 []

代码：
""" + code


def parse_json(answer):
    """从 AI 的回答里找出 [ ... ]，变成 Python 的列表。找不到就报错 ValueError。"""
    start = answer.find("[")
    end = answer.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("回答里找不到 [ ]")
    return json.loads(answer[start:end + 1])


def review_code(code, valid):
    """完整的审查流程：问 AI → 读懂 JSON → 丢掉不在改动里的。回传问题列表。"""
    question = build_question(code)
    answer = ask_ai_with_tools(question)

    print("===== DeepSeek 的原始回答 =====")
    print(answer)

    try:
        issues = parse_json(answer)
    except ValueError:
        print("⚠️ AI 的回答格式不对，再问一次")
        answer = ask_ai_with_tools(question + "\n\n上次你的回答格式不对。这次只能输出 JSON 数组，第一个字必须是 [")
        print(answer)
        issues = parse_json(answer)

    good_issues = []
    for issue in issues:
        path = issue["path"]
        line = int(issue["line"])
        if path in valid and line in valid[path]:
            issue["line"] = line
            good_issues.append(issue)
        else:
            print(f"⚠️ 丢掉：{path} 第 {line} 行不在这次的改动里")

    return good_issues
```

**`try_review.py` 整个换成**（变短很多！）：

```python
import sys

from github_api import files, add_line_numbers, get_valid_lines, post_review, get_old_comment_lines, MARKER
from review_core import review_code

SKIP_ENDINGS = (".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".lock", ".md")
SKIP_FOLDERS = ("evals/",)
MAX_PATCH_LINES = 400

code = ""
valid = {}
skipped = []

for f in files:
    name = f["filename"]
    if "patch" not in f or f["status"] == "removed" or name.endswith(SKIP_ENDINGS) or name.startswith(SKIP_FOLDERS):
        skipped.append(name)
        continue
    if len(f["patch"].split("\n")) > MAX_PATCH_LINES:
        skipped.append(name + "（改动太大）")
        continue
    code = code + f"\n===== 文件：{name} =====\n" + add_line_numbers(f["patch"]) + "\n"
    valid[name] = get_valid_lines(f["patch"])

if skipped:
    print("⏭️ 跳过这些文件：", skipped)

if code == "":
    print("没有需要审查的代码，结束。")
    sys.exit()

issues = review_code(code, valid)

print("===== 程序读懂之后 =====")
for issue in issues:
    print(f"第 {issue['line']} 行 [{issue['category']}]：{issue['title']}")
    print(f"    建议：{issue['suggestion']}")

old = get_old_comment_lines()
comments = []

for issue in issues:
    if (issue["path"], issue["line"]) in old:
        print(f"⏭️ 第 {issue['line']} 行以前留过言了，跳过")
        continue

    if issue["category"] == "security":
        icon = "🔒 安全问题"
    else:
        icon = "🐛 Bug"

    body = f"**{icon}**\n\n{issue['title']}\n\n**建议：** {issue['suggestion']}\n\n{MARKER}"

    comments.append({
        "path": issue["path"],
        "line": issue["line"],
        "side": "RIGHT",
        "body": body,
    })

if comments:
    summary = f"🤖 AI 审查完毕，发现 {len(comments)} 个新问题，请看代码旁边的留言。"
    post_review(summary, comments)
else:
    print("没有新问题，这次不留言。")
```

> 💡 新增的 `SKIP_FOLDERS = ("evals/",)`：考卷里**故意写错**的代码不要被 PR 审查（不然 AI 会在考卷上留一堆言 😅）。注意 `("evals/",)` 最后有一个**逗号**，只有一个东西的 tuple 一定要有逗号。

---

## 11.2 出考卷：新建 `evals/cases/` 文件夹，放 12 个文件

在 VS Code 新建文件时直接打 `evals/cases/01_off_by_one.py`，文件夹会自动建好。
⚠️ **每一行的位置很重要**（答案是用行号对的），空行也要照抄。

**`evals/cases/01_off_by_one.py`**（第 2 行：多跑一次，超出范围）
```python
def print_all(items):
    for i in range(len(items) + 1):
        print(items[i])
```

**`evals/cases/02_divide_zero.py`**（第 3 行：空列表会除以零）
```python
def average(scores):
    total = sum(scores)
    return total / len(scores)
```

**`evals/cases/03_sql_injection.py`**（第 2 行：SQL 注入）
```python
def login(db, username, password):
    sql = "SELECT * FROM users WHERE name = '" + username + "' AND pw = '" + password + "'"
    return db.execute(sql)
```

**`evals/cases/04_command_injection.py`**（第 5 行：命令注入）
```python
import os


def ping(host):
    os.system("ping -c 1 " + host)
```

**`evals/cases/05_hardcoded_password.py`**（第 3 行：密码写死）
```python
import requests

DB_PASSWORD = "SuperSecret2024"


def connect():
    return requests.post("https://db.example.com/login", data={"password": DB_PASSWORD})
```

**`evals/cases/06_eval_input.py`**（第 3 行：`eval` 执行用户输入）
```python
def calculator():
    expression = input("请输入算式：")
    result = eval(expression)
    print(result)
```

**`evals/cases/07_mutable_default.py`**（第 1 行：默认值用列表，会被共用）
```python
def add_item(item, cart=[]):
    cart.append(item)
    return cart
```

**`evals/cases/08_none_check.py`**（第 10 行：找不到用户时是 None，会报错）
```python
def find_user(users, user_id):
    for u in users:
        if u["id"] == user_id:
            return u
    return None


def get_name(users, user_id):
    user = find_user(users, user_id)
    return user["name"]
```

**`evals/cases/09_wrong_return.py`**（第 3 行：回传错变量）
```python
def total_price(price, quantity):
    total = price * quantity
    return price
```

**`evals/cases/10_path_traversal.py`**（第 2 行：用户可以用 `../` 读任何文件）
```python
def download(filename):
    with open("uploads/" + filename, "rb") as f:
        return f.read()
```

**`evals/cases/11_clean_max.py`**（✅ 正确的代码，不应该报任何问题）
```python
def largest(numbers):
    if not numbers:
        return None
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest
```

**`evals/cases/12_clean_greet.py`**（✅ 正确的代码）
```python
def greet(name):
    name = name.strip()
    if name == "":
        return "你好！"
    return f"你好，{name}！"
```

**答案卷 `evals/answers.json`**：每题的 bug 在第几行（`[]` = 没有 bug）

```json
{
    "01_off_by_one.py": [2],
    "02_divide_zero.py": [3],
    "03_sql_injection.py": [2],
    "04_command_injection.py": [5],
    "05_hardcoded_password.py": [3],
    "06_eval_input.py": [3],
    "07_mutable_default.py": [1],
    "08_none_check.py": [10],
    "09_wrong_return.py": [3],
    "10_path_traversal.py": [2],
    "11_clean_max.py": [],
    "12_clean_greet.py": []
}
```

---

## 11.3 改考卷的程序：新建 `run_eval.py`

```python
import json

from review_core import review_code

CASES_FOLDER = "evals/cases"

with open("evals/answers.json", encoding="utf-8") as f:
    answers = json.load(f)

caught = 0
missed = 0
false_alarms = 0
total_bugs = 0
report = []

for name, expected in answers.items():
    path = f"{CASES_FOLDER}/{name}"
    with open(path, encoding="utf-8") as f:
        lines = f.read().rstrip("\n").split("\n")

    # 假装整个文件都是新加的：每一行都有行号，前面加 +
    code = f"\n===== 文件：{path} =====\n"
    valid = {path: {}}
    for no, text in enumerate(lines, start=1):
        code = code + f"{no:>3} +{text}\n"
        valid[path][no] = text

    print(f"\n######## 正在考：{name} ########")
    try:
        issues = review_code(code, valid)
    except ValueError:
        print("⚠️ AI 回答两次都不是 JSON，这题算 0 分")
        issues = []

    found = []
    for issue in issues:
        found.append(issue["line"])

    # 每一个真的 bug：AI 有没有在附近（差 1 行以内）说到？
    for bug_line in expected:
        total_bugs = total_bugs + 1
        hit = False
        for x in found:
            if abs(x - bug_line) <= 1:
                hit = True
        if hit:
            caught = caught + 1
        else:
            missed = missed + 1

    # AI 说的每一个问题：是不是真的 bug 附近？不是的话就是误报
    for x in found:
        real = False
        for bug_line in expected:
            if abs(x - bug_line) <= 1:
                real = True
        if not real:
            false_alarms = false_alarms + 1

    report.append(f"{name:<28} 答案：{str(expected):<8} AI 说：{found}")

print("\n\n================ 📊 成绩单 ================")
for r in report:
    print(r)
print("-------------------------------------------")
print(f"✅ 抓到：{caught} / {total_bugs}")
print(f"❌ 漏掉：{missed}")
print(f"🚨 误报：{false_alarms}")
```

### 📖 解释
| 部分 | 意思 |
|---|---|
| `json.load(f)` | 读答案卷（`load` 读文件；第 5 课的 `loads` 读文字，s = string） |
| `.items()` | 字典一对一对拿出来：题目名字 + 答案 |
| 「假装整个文件都是新加的」 | 考卷不是 PR，没有 diff，所以自己做一个：每行加行号和 `+` |
| `valid = {path: {}}` + `valid[path][no] = text` | 每一行都可以留言（第 12 课会用到 `text`） |
| `abs(x - bug_line) <= 1` | `abs` = 绝对值。AI 说的行号**差 1 行以内**都算对（例如 bug 在第 9 行，AI 说第 10 行，也算抓到） |
| 误报 | AI 说的问题**不在任何一个 bug 附近** = 乱报 |
| `f"{name:<28}"` | 靠左对齐、占 28 格，让成绩单排整齐 |

---

## 11.4 考试！

```powershell
$env:PYTHONUTF8 = "1"
```
```powershell
python run_eval.py
```

> 💰 会问 AI 12 次以上（AI 用工具的话更多），大概 1–3 分钟。

把成绩记在这里 👇（每次改 prompt 或换模型，就再考一次，加一行）

| 日期 | 版本 | 抓到 | 漏掉 | 误报 | 备注 |
|---|---|---|---|---|---|
| | 第 11 课 | / 10 | | | 第一次考试 |
| | | | | | |

> 💡 同一份考卷，每次考的分数可能**不太一样**（AI 有随机性）。认真比较的话，考 2–3 次取平均。

## 11.5 Push + 开 PR

```powershell
git add .
```
```powershell
git commit -m "第 11 课：测试题和成绩单"
```
```powershell
git push -u origin lesson-11
```

开 PR → Actions 记录应该看到 `⏭️ 跳过这些文件： ['evals/cases/01_off_by_one.py', ...]` ✅（考卷没有被审查）→ Merge

## ✅ 第 11 课完成标准
- [ ] `python run_eval.py` 印出成绩单
- [ ] 成绩记进上面的表格
- [ ] PR 审查跳过 `evals/`
- [ ] lesson-11 merge 进 main

---

# 第 12 课：减少误报 🎯

## 🎯 目标
AI 有时候会**编造**问题（幻觉），或者把「写法不好看」也当成 bug。被乱报几次，团队就不再相信这个 agent 了。
这一课加两道新的安全门：

| 安全门 | 做法 | 比喻 |
|---|---|---|
| ④ 要求证据 | AI 必须**照抄那一行原文**，程序比对是不是真的一样 | 🧾 警察说你闯红灯，要拿出照片 |
| ⑤ 第二轮复查 | 另一次 AI 当「严格的检查员」，逐个问：这个问题**真的存在吗**？只回答 是/否 | 👨‍⚖️ 第二位法官再看一次 |

然后**再考一次**，比较第 11 课的成绩。

## 12.0 开新 branch

```powershell
git checkout main
```
```powershell
git pull
```
```powershell
git checkout -b lesson-12
```

## 12.1 `github_api.py`：号码牌袋子 → 记下每一行的内容

`get_valid_lines` 改 2 个地方：

```python
def get_valid_lines(patch):
    valid = {}                        # ← 原本是 set()，改成 {}（字典）
    line_no = 0

    for line in patch.split("\n"):
        if line.startswith("@@"):
            start = line.split(" ")[2]
            start = start[1:]
            start = start.split(",")[0]
            line_no = int(start)
        elif line.startswith("-") or line.startswith("\\"):
            continue
        else:
            valid[line_no] = line[1:]  # ← 原本是 valid.add(line_no)
            line_no = line_no + 1

    return valid
```

以前只记「哪些行号可以留言」，现在还记下「**那一行写什么**」，例如 `{5: "    return sum(prices) / len(prices)"}`。
- `line[1:]`：去掉最前面的 `+` 或空格
- `line_no in valid` 对字典一样有效（看的是左边的 key），所以其他代码**不用改**

## 12.2 `review_core.py`：加证据检查 + 复查

**① 第一行 import 改成：**

```python
from ai import ask_ai, ask_ai_with_tools
```

**② `build_question` 里**，把 `注意：只能对改动里有行号的行提出问题。` 这一行，还有 JSON 格式那一行，换成：

```
注意：
- 只能对改动里有行号的行提出问题。
- 只报告你确定会出错或有安全风险的问题。不确定的、只是写法不好看的，都不要报告。
- code 要照抄那一行的原文，当作证据。

只能用 JSON 格式回答，不要输出任何其他文字。格式如下：
[
    {"path": "文件名", "line": 行号, "code": "那一行的原文", "category": "bug 或 security", "title": "一句话说明问题", "suggestion": "怎么改"}
]
```

（多了 `"code"`，还有「不确定就不要报告」）

**③ `parse_json` 下面**加两个新函数：

```python
def has_evidence(quote, real_line):
    """AI 引用的原文，是不是真的出现在那一行？（不管空格）"""
    quote = "".join(quote.split())
    real_line = "".join(real_line.split())
    return quote != "" and quote in real_line


def build_verify_question(code, issue):
    return f"""你是一位严格的资深工程师，专门检查别人的审查意见有没有说错。

下面是一段代码，以及另一位审查员提出的问题。
请判断：这个问题在这段代码里真的存在吗？只根据代码本身判断，不要猜测。

只能回答一个字：是 或 否

代码：
{code}

审查员说：{issue['path']} 第 {issue['line']} 行
问题：{issue['title']}
"""
```

- `"".join(quote.split())`：把**所有空格去掉**再比，AI 抄的时候少一个空格也不算错
- `quote in real_line`：AI 抄的那段，是不是**真的出现在**那一行里
- `quote != ""`：AI 没给证据 → 不算数

**④ `review_code` 下半部分**：把 `good_issues = []` 开始到 `return good_issues` 整段，换成：

```python
    good_issues = []
    for issue in issues:
        path = issue["path"]
        line = int(issue["line"])
        if path not in valid or line not in valid[path]:
            print(f"⚠️ 丢掉：{path} 第 {line} 行不在这次的改动里")
            continue
        if not has_evidence(issue.get("code", ""), valid[path][line]):
            print(f"⚠️ 丢掉：{path} 第 {line} 行，AI 引用的原文对不上")
            continue
        issue["line"] = line
        good_issues.append(issue)

    confirmed = []
    for issue in good_issues:
        reply = ask_ai(build_verify_question(code, issue))
        if reply.strip().startswith("是"):
            confirmed.append(issue)
        else:
            print(f"🧐 复查不通过，丢掉：第 {issue['line']} 行 {issue['title']}")

    return confirmed
```

### 📖 解释
- 三道检查**一道一道过**：行号在改动里？→ 证据对得上？→ 复查说「是」？全部通过才留下
- `issue.get("code", "")`：AI 忘了给 code → 当作空的 → 证据不足，丢掉
- 复查用 `ask_ai`（**不用工具**），比较便宜、比较快
- `reply.strip().startswith("是")`：回答**以「是」开头**才算通过

> 💰 复查会让**每个问题多问 AI 一次**。花费多一点，换来更少乱报。这就是真实世界的取舍（trade-off）。

## 12.3 再考一次，比较成绩

```powershell
python run_eval.py
```

`run_eval.py` **不用改**，因为它用的就是 `review_code`。第 11 课的 `valid[path][no] = text` 就是为了这一刻准备的。

把成绩加进第 11 课的表格，比较一下：

| 你会看到 | 意思 |
|---|---|
| 误报 ⬇️，抓到差不多 | 🎉 完美，安全门有效 |
| 误报 ⬇️，抓到也 ⬇️ | 复查太严格，错杀了真的 bug。可以试着改 `build_verify_question` 的语气（例如去掉「严格」） |
| 都没变 | 本来误报就很少，或者需要更难的考题 |

> 💡 这就是工程师的日常：**改一个东西 → 考试 → 看数字 → 决定要不要留**。不是凭感觉。

## 12.4 Push + 开 PR → Merge

```powershell
git add .
```
```powershell
git commit -m "第 12 课：证据检查和第二轮复查"
```
```powershell
git push -u origin lesson-12
```

开 PR，Actions 记录里可以看到 `🧐 复查不通过` 或 `AI 引用的原文对不上`（如果有的话）。看完 → Merge 🎉

## ✅ 第 12 课完成标准
- [ ] 成绩表有第 11、12 课两行可以比较
- [ ] lesson-12 merge 进 main

---

# 🎓 毕业：你的 agent 现在会……

| 能力 | 哪一课 |
|---|---|
| 🤖 有 PR 就自动审查，不用人手 | 7 |
| 🔍 自己用工具查上下文 | 8 |
| 🛡️ 5 道安全门：次数、大小、行号、证据、复查 | 8、12 |
| 💪 格式坏了会重试，失败会通知 | 9 |
| ⏭️ 跳过图片、文档、太大的文件 | 9 |
| 🧹 不重复留言 | 10 |
| 📊 有考卷和成绩单，用数字证明准确度 | 11 |

👉 这就是一个「**合格中上**」的 code review agent。面试时可以说：
> 「我做了一个 PR 审查 agent，用 GitHub Actions 自动触发，DeepSeek 透过 Tool Use 自己查上下文。我用 12 题的测试集衡量，加了证据检查和第二轮复查之后，误报从 X 降到 Y，抓到率维持在 Z/10。」

**有数字的故事，比什么都有说服力。**

---

# 🚀 之后可以升级的方向

| 升级 | 解决什么问题 | 难度 |
|---|---|---|
| 考卷加到 30 题、更多语言 | 成绩更可信 | ⭐⭐ |
| 比对问题内容来去重（不只比行号） | 加了代码、行号移动后还会重复留言 | ⭐⭐⭐ |
| 加入 linter / Semgrep | 用规则工具抓确定的问题，AI 专心抓逻辑问题 | ⭐⭐⭐ |
| 在 PR 里打 `/review` 才运行 | 让人决定什么时候审查，省钱 | ⭐⭐⭐ |
| 大 PR 分批审查 | 现在超过 400 行的文件直接跳过 | ⭐⭐⭐ |
| 读取项目的规则文件（团队写代码的规定） | 按团队标准审查 | ⭐⭐⭐⭐ |
| 人点 👎 的留言记下来，改进 prompt | 越用越准 | ⭐⭐⭐⭐ |

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
| Tool Use | 让 AI 说「我想用这个工具」，由程序去执行，再把结果交回 AI |
| 对话循环 | AI 要工具 → 程序执行 → 交回 → 重复，直到 AI 给出答案 |
| 幻觉 | AI 很有自信地说出不存在或错误的东西 |
| 误报 | AI 说有 bug，但其实没有 |
| Eval（测试集） | 一份有标准答案的考卷，用来给 AI 打分 |
| try / except | 「试试看，出错了就改做别的」，不让程序整个停掉 |

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
