from fastapi import APIRouter, UploadFile, File
from app.services.file_handler import save_upload_file
from app.core.logger import logger

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    logger.info("upload endpoint hit")
    path = await save_upload_file(file)
    logger.info("file uploaded successfully!")
    return {"filename": file.filename, "path": path}