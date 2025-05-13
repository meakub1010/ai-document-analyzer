from fastapi import APIRouter, HTTPException
from app.models.schema import QARequest, QAResponse
from app.services.qa_service import answer_question
from app.core.logger import logger
from pathlib import Path
import os


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[4]  # goes to ai_doc_analyzer/
UPLOAD_DIR = BASE_DIR / "uploads"
logger.info(f"base dir: {BASE_DIR}")

@router.post("/qa", response_model=QAResponse)
def ask_question(payload: QARequest):
    logger.info(f"base dir: {BASE_DIR}")
    logger.info(f"payload: {payload}")
    # doc_path = f"uploads/{payload.document_id}.txt"
    # doc_path = os.path.join(os.getcwd(), "uploads", f"{payload.document_id}.txt")
    doc_path = UPLOAD_DIR / f"{payload.document_id}.txt"
    logger.info(f"doc_path: {doc_path}")

    print(f"doc_path: '{doc_path}'")
    print(f"File exists? {doc_path.exists()}")
    print(f"Current working dir: {Path.cwd()}")
    if not doc_path.exists():
        raise HTTPException(status_code=404, detail="Document not found")
    
    with doc_path.open("r", encoding="utf-8") as f:
        context = f.read()

    result = answer_question(payload.question, context)

    return QAResponse(**result)
