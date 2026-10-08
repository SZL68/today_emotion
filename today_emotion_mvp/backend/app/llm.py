import json
import httpx
from .config import settings


SYSTEM_PROMPT = """
你是“今天的情绪”的情绪日记助手。
你的职责是帮助用户整理和理解当下的情绪，而不是进行心理疾病诊断或医疗治疗。

请严格返回 JSON：
{
  "intensity": 0到100的整数,
  "tags": ["情绪标签1","情绪标签2","情绪标签3"],
  "summary": "用温和、具体、不夸张的语言总结用户今天的情绪和事件，100字以内",
  "advice": "给出1到3条非医疗性的、自我照顾性质的建议，120字以内"
}

不要声称用户患有任何疾病。
不要进行心理疾病诊断。
如果用户内容存在明显的自伤或伤害他人的表达，不要提供危险细节；summary保持简洁，并在advice中明确建议用户立即联系身边可信任的人以及当地紧急/危机支持资源。
"""


async def analyze_with_llm(emotion: str, content: str) -> dict:
    if not settings.llm_api_key or not settings.llm_model:
        raise RuntimeError("LLM未配置")

    url = settings.llm_base_url.rstrip("/") + "/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.llm_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": settings.llm_model,
        "temperature": 0.4,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"用户选择的今日情绪：{emotion}\n用户记录：{content}",
            },
        ],
    }

    async with httpx.AsyncClient(timeout=45) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

    raw = data["choices"][0]["message"]["content"]
    result = json.loads(raw)
    result["intensity"] = max(0, min(100, int(result["intensity"])))
    result["tags"] = [str(x) for x in result.get("tags", [])][:5]
    return result
