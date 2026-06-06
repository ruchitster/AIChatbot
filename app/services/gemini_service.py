import time
import requests
from app.core.config import GEMINI_API_KEY

GEMINI_MODEL = "gemini-2.5-flash"


def call_gemini(prompt: str):

    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent"
        f"?key={GEMINI_API_KEY}"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    for attempt in range(3):

        try:
            response = requests.post(url, json=payload, timeout=30)

            data = response.json()

            print("\nSTATUS CODE:", response.status_code)
            print("\nGEMINI RAW RESPONSE:", data)

            # ❌ Handle API error properly
            if "error" in data:
                time.sleep(2)
                continue

            # ✅ SAFE extraction of response text
            return data["candidates"][0]["content"]["parts"][0]["text"]

        except Exception as e:
            print("EXCEPTION:", str(e))
            time.sleep(2)

    return "Gemini unavailable after multiple retries."