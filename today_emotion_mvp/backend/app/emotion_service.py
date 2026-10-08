from datetime import datetime
from .db import get_conn
from .llm import analyze_with_llm


FALLBACK = {
    "😊": (25, ["轻松", "愉快"]),
    "🙂": (40, ["平稳", "还不错"]),
    "😐": (50, ["平淡", "一般"]),
    "😔": (72, ["失落", "疲惫"]),
    "😭": (88, ["难过", "压力"]),
}


async def create_record(emotion: str, content: str):
    try:
        result = await analyze_with_llm(emotion, content)
    except Exception:
        intensity, tags = FALLBACK.get(emotion, (50, ["情绪"]))
        result = {
            "intensity": intensity,
            "tags": tags,
            "summary": "今天发生了一些让你产生情绪波动的事情。先把它记录下来，本身就是一次整理。",
            "advice": "先给自己一点缓冲时间；如果愿意，可以把注意力放回当下最能控制的一件小事。",
        }

    now = datetime.now().isoformat(timespec="seconds")
    conn = get_conn()
    cur = conn.execute(
        """INSERT INTO emotion_records
        (emotion, intensity, content, ai_summary, ai_advice, ai_tags, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            emotion,
            result["intensity"],
            content,
            result["summary"],
            result["advice"],
            "||".join(result.get("tags", [])),
            now,
        ),
    )
    conn.commit()
    record_id = cur.lastrowid
    conn.close()

    return {**result, "record_id": record_id}


def get_history():
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM emotion_records ORDER BY created_at DESC"
    ).fetchall()
    conn.close()

    records = []
    for row in rows:
        records.append({
            "id": row["id"],
            "emotion": row["emotion"],
            "intensity": row["intensity"],
            "content": row["content"],
            "summary": row["ai_summary"] or "",
            "advice": row["ai_advice"] or "",
            "tags": row["ai_tags"].split("||") if row["ai_tags"] else [],
            "created_at": row["created_at"],
        })

    # MVP：按实际记录日期计算连续天数
    dates = sorted({x["created_at"][:10] for x in records}, reverse=True)
    streak = 0
    if dates:
        from datetime import date, timedelta
        expected = date.today()
        for d in dates:
            current = date.fromisoformat(d)
            if current == expected:
                streak += 1
                expected -= timedelta(days=1)
            elif current < expected:
                break

    return {"streak": streak, "total": len(records), "records": records}
