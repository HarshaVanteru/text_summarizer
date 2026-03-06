import requests
import os
from dotenv import load_dotenv
from fastapi import File

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
def build_analysis_prompt(text: str):
    return f"""
    Analyze the following text.

    Provide:
    1. A short summary
    2. Action items
    3. Key decisions

    Text:
    {text}
    """

def bot(prompt:str):
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

def allowed_files(file:File):
    allowed_extensions = ["txt", "pdf", "docx"]

    filename = file.filename.split(".")[-1]

    if filename not in allowed_extensions:
        return {"error": "Unsupported file type"}
    return file