from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text_from_pdf
from app.core.logger import logger
import uuid
import shutil
import os

router = APIRouter()

@router.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"uploads/{file_id}.pdf"
    logger.info("ocr end point hit")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)
    logger.info("pdf to text conversion done successfully")
    text_path = f"uploads/{file_id}.txt"

    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return file_id