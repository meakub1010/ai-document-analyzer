from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text_from_pdf, extract_from_image
from app.core.logger import logger
import uuid
import shutil

router = APIRouter()

@router.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    text = ''
    ext = file.filename.split(".")[-1].lower()
    logger.info(f"ext: {ext}")
    file_path = f"uploads/{file_id}.{ext}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if ext == "pdf":
        from app.services.ocr_service import extract_text_from_pdf
        text = extract_text_from_pdf(file_path)
        logger.info(f"text: {text}")
        logger.info("text conversion done successfully")
    elif ext in ["jpg", "jpeg", "png"]:
        from app.services.ocr_service import extract_from_image
        text = extract_from_image(image_path=file_path)
        logger.info(f"text: {text}")
        logger.info("text conversion done successfully")
    else:
        raise ValueError("Unsupported file type")
    
    text_path = f"uploads/{file_id}.txt"

    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return file_id