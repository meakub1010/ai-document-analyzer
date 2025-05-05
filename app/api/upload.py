from fastapi import APIRouter, UploadFile, File
from app.services.file_handler import save_upload_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    path = await save_upload_file(file)
    return {"filename": file.filename, "path": path}