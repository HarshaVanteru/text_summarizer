from fastapi import APIRouter, Form, File, UploadFile, HTTPException

from .prompt import allowed_files
from .service import summarize_text,summarize_document

router = APIRouter(prefix="/Summarizer", tags=["Summarizer"])

@router.post("/analyze",status_code=200)
async def analyze_text(text:str = Form(None),file:UploadFile = File(None)):
    if not text and not file:
        raise HTTPException(status_code=400,detail="provide text or document")
    if text:
        result = summarize_text(text)
        return result
    file = allowed_files(file)
    if not file:
        raise HTTPException(status_code=400,detail="provide pdf,txt,docx files only")
    result = await summarize_document(file)
    return result


