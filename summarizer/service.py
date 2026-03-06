from summarizer.prompt import build_analysis_prompt, bot
import requests
import os
from dotenv import load_dotenv


def summarize_text(text: str):

    print("ENV FILE LOADED:", os.getenv("OPENROUTER_API_KEY"))

    prompt = build_analysis_prompt(text)
    result = bot(prompt)
    return result


async def summarize_document(file):

    content = await file.read()
    text = content.decode("utf-8")
    return summarize_text(text)