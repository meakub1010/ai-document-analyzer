from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text_from_pdf
from app.core.logger import logger
import uuid
import shutil
import os

router = APIRouter()

@router.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4)
    file_path = f"/temp/{file_id}_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    os.remove(file_path)

    return {"text": text}