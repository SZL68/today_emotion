from dataclasses import dataclass


@dataclass
class EmotionRecord:
    emotion: str
    intensity: int
    content: str
    ai_summary: str
    ai_advice: str
    ai_tags: str
    created_at: str
