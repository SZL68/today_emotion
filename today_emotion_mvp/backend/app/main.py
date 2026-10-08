from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .db import init_db
from .schemas import AnalyzeRequest
from .emotion_service import create_record, get_history


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="今天的情绪 API",
    version="1.0.0",
    description="情绪日记 + AI陪伴 MVP",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok", "service": "today-emotion"}


@app.post("/api/emotions/analyze")
async def analyze(req: AnalyzeRequest):
    if not req.content.strip():
        raise HTTPException(status_code=400, detail="记录内容不能为空")
    return await create_record(req.emotion, req.content.strip())


@app.get("/api/emotions/history")
def history():
    return get_history()
