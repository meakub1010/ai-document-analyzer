from fastapi import APIRouter, UploadFile, File
from app.services.file_handler import save_uploa_file

router = APIRouter()

async def upload_file(file: UploadFile = File(...)):
    path = await save_uploa_file(file)
    return {"filename": file.filename, "path": path}