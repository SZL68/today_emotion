# 今天的情绪 · MVP v1.0

定位：情绪日记 + AI陪伴，不做医疗诊断。

## 技术栈
- 微信小程序原生开发（WXML / WXSS / JS）
- Python + FastAPI
- SQLite
- OpenAI-compatible Chat Completions API（可配置为其他兼容服务）

## 目录
```text
today_emotion_mvp/
├─ backend/
│  ├─ app/
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  ├─ db.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  ├─ llm.py
│  │  ├─ emotion_service.py
│  │  └─ main.py
│  ├─ .env.example
│  └─ requirements.txt
└─ miniprogram/
   ├─ app.js
   ├─ app.json
   ├─ app.wxss
   ├─ utils/api.js
   └─ pages/
      ├─ home/
      ├─ report/
      └─ history/
```

## 1. 启动后端

Windows + conda：

```bash
conda create -n emotion python=3.11 -y
conda activate emotion
cd backend
pip install -r requirements.txt
copy .env.example .env
```

编辑 `.env`：

```env
LLM_BASE_URL=https://你的OpenAI兼容接口/v1
LLM_API_KEY=你的API_KEY
LLM_MODEL=你的模型名
```

然后：

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

浏览器访问：

```text
http://127.0.0.1:8000/docs
```

## 2. 微信小程序

使用微信开发者工具打开 `miniprogram/`。

开发阶段把 `utils/api.js` 中的 `BASE_URL` 改成你的电脑局域网 IP：

```js
const BASE_URL = 'http://192.168.x.x:8000'
```

手机真机调试时，手机和电脑需要在同一局域网。正式上线时再配置 HTTPS 合法域名。

## 3. 当前功能

- 首页：选择今日情绪 + 输入今日发生的事
- AI分析：生成主情绪、情绪强度、情绪标签、AI总结、非医疗性的自我照顾建议
- SQLite保存记录
- 历史页：查看历史记录与连续记录天数
- 后端 Swagger API 文档
- LLM异常时提供本地兜底分析，不影响基础流程

## 4. 下一阶段

V1.1 再增加：
- 情绪趋势图
- 情绪触发因素
- AI长期记忆
- RAG
- 用户登录
- 分享卡片
- 会员/额度系统
- 安全响应流程
