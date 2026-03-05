from summarizer.prompt import build_analysis_prompt
import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")


def summarize_text(text: str):

    print("ENV FILE LOADED:", os.getenv("OPENROUTER_API_KEY"))

    prompt = build_analysis_prompt(text)

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "arcee-ai/trinity-large-preview:free",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]


async def summarize_document(file):

    content = await file.read()
    text = content.decode("utf-8")

    return summarize_text(text)