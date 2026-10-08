from pydantic import BaseModel, Field
from typing import List


class AnalyzeRequest(BaseModel):
    emotion: str
    content: str = Field(min_length=1, max_length=5000)


class AnalyzeResponse(BaseModel):
    emotion: str
    intensity: int
    tags: List[str]
    summary: str
    advice: str
    record_id: int


class HistoryItem(BaseModel):
    id: int
    emotion: str
    intensity: int
    content: str
    summary: str
    advice: str
    tags: List[str]
    created_at: str


class HistoryResponse(BaseModel):
    streak: int
    total: int
    records: List[HistoryItem]
