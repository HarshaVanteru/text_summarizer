import os

from fastapi import FastAPI
from summarizer.route import router as summarizer_router
from dotenv import load_dotenv

app = FastAPI(title="Text Analyzer API")


app.include_router(summarizer_router)


@app.get("/")
def root():
    return {"message": "Text Summarizer API running"}