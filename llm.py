import requests
import time
from database import get_recent_conversation


def get_llm_response(prompt):
    try:
        start_time = time.time()

        # Load recent Q&A
        past = get_recent_conversation(limit=5)
        messages = [{"role": "system", "content": "You are a helpful assistant with short memory. Try to recall past answers if possible."}]
        for q, r in past:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": r})

        # Add current prompt
        messages.append({"role": "user", "content": prompt})

        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "mistral",
                "messages": messages,
                "stream": False
            },
            timeout=30
        )

        response.raise_for_status()
        result = response.json()
        text = result.get("message", {}).get("content", "").strip()

        duration = int((time.time() - start_time) * 1000)
        return text, "success", duration

    except Exception as e:
        print(f"LLM error: {e}")
        return "Sorry, I had an error.", "error", 0