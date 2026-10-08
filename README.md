# 🌙 Today Emotion - AI 情绪日记小程序


## 项目介绍

Today Emotion 是一个基于微信小程序 + FastAPI + 大语言模型（LLM）的 AI 情绪日记应用。

用户可以每天记录自己的情绪和发生的事情，AI 会帮助用户整理当天经历、分析情绪状态，并生成温和的反馈与建议。

本项目定位为 **AI 情绪陪伴与自我记录工具**，不涉及心理疾病诊断或医疗服务。


## 项目特点

- 📝 情绪记录
  - 用户选择当天情绪状态
  - 输入当天发生的事情

- 🤖 AI 情绪分析
  - 基于大语言模型理解用户输入
  - 生成情绪强度、情绪标签
  - 提供个性化总结和建议

- 📊 情绪历史记录
  - 保存用户历史情绪数据
  - 支持查看过去的记录

- 📱 微信小程序体验
  - 原生微信小程序开发
  - 支持手机真机测试


---

# 系统架构
             用户

              |
              |

      微信小程序前端

              |

          HTTP API

              |

          FastAPI后端

              |

    +----------------+

    |                |

   LLM API       SQLite

    |                |
AI情绪分析 历史记录保存



---

# 技术栈


## 前端

- 微信小程序
- WXML
- WXSS
- JavaScript


## 后端

- Python
- FastAPI
- SQLite


## AI

- Large Language Model API
- Prompt Engineering
- Structured Output


---

# 项目结构



today_emotion_mvp

├── backend

│ ├── app

│ │ ├── main.py # FastAPI入口

│ │ ├── emotion_service.py # 情绪业务逻辑

│ │ ├── llm.py # LLM调用封装

│ │ ├── config.py # 配置管理

│ │ ├── db.py # 数据库操作

│ │ ├── models.py # 数据模型

│ │ └── schemas.py # API数据结构

│ │

│ ├── requirements.txt

│ └── .env.example

├── miniprogram

│ ├── pages

│ │ ├── home # 情绪输入页面

│ │ ├── report # AI报告页面

│ │ └── history # 历史记录页面

│ │

│ ├── app.js

│ ├── app.json

│ └── app.wxss

└── README.md



---

# 功能流程


## 1. 用户记录情绪


用户选择：


😊 很好
🙂 还行
😐 一般
😔 有点累
😭 很糟



输入：


今天发生的事情...



---

## 2. AI分析


后端接收：

```json
{
    "emotion":"😔",
    "content":"今天面试失败了"
}

调用LLM生成：

{
    "intensity":75,

    "tags":[
        "失落",
        "压力"
    ],

    "summary":
    "今天经历了求职中的挫折，因此产生了明显的失落感。",

    "advice":
    "允许自己短暂调整，同时关注下一步可以行动的事情。"
}

3. 保存记录

SQLite保存：

用户情绪
情绪强度
用户输入
AI总结
AI建议
创建时间
快速开始
后端启动

进入backend目录：

cd backend

安装依赖：

pip install -r requirements.txt

配置环境变量：

创建：

.env

填写：

LLM_BASE_URL=your_api_url

LLM_API_KEY=your_api_key

LLM_MODEL=your_model

启动：

uvicorn app.main:app --reload --host 0.0.0.0

测试：

访问：

http://127.0.0.1:8000/docs
小程序运行

使用：

微信开发者工具

导入：

miniprogram

开发阶段：

修改：

app.js

apiBaseUrl

指向本地FastAPI地址。

例如：

apiBaseUrl:
'http://192.168.x.x:8000'
API接口
情绪分析

POST

/api/emotions/analyze

请求：

{
 "emotion":"🙂",
 "content":"今天完成了一件重要的事情"
}

返回：

{
 "emotion":"🙂",
 "intensity":40,
 "tags":[
    "开心"
 ],
 "summary":"...",
 "advice":"..."
}

历史记录

GET

/api/emotions/history

返回用户历史情绪记录。

项目演进
MVP版本

已完成：

情绪记录
LLM分析
AI反馈
历史保存
Future

计划：

情绪趋势分析
情绪日历
AI长期记忆
RAG增强历史理解
个性化情绪报告

注意事项

本项目用于：

情绪记录
自我反思
AI陪伴体验

不用于：

心理疾病诊断
医疗建议
