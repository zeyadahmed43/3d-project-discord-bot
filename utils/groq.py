import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_idea(prompt_content):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt_content}],
        "temperature": 0.7,
        "max_tokens": 1024
    }

    try:
        start_time = time.time()
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=15
        )
        elapsed = time.time() - start_time

        if response.status_code != 200:
            print(f"❌ API Error: {response.status_code} - {response.text[:200]}")
            return f"⚠️ API Error: {response.status_code}", 0

        json_data = response.json()
        content = json_data["choices"][0]["message"]["content"]
        tokens_used = json_data.get("usage", {}).get("total_tokens", 0)

        print(f"✅ Received response in {elapsed:.2f}s")
        print(f"📄 Response: {content[:150]}{'...' if len(content) > 150 else ''}")
        print(f"🔢 Stats: Tokens used - {tokens_used}")

        return content, tokens_used

    except requests.exceptions.Timeout:
        print("❌ API Request timed out")
        return "⚠️ Request timed out. Please try again.", 0
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return f"⚠️ Error: {str(e)}", 0
