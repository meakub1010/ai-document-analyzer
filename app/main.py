from fastapi import FastAPI
from app.api import upload
from app.core.logger import logger
from app.api.v1.endpoints import ocr, summarize, classify, qa


app = FastAPI()
app.include_router(upload.router)
app.include_router(ocr.router, prefix="/api/v1", tags=["OCR"])
app.include_router(summarize.router, prefix="/api/v1", tags=["summarize"])
app.include_router(classify.router, prefix="/api/v1", tags=["classify"])
app.include_router(qa.router, prefix="/api/v1", tags=["qa"])

@app.get("/")
def read_root():
    logger.info("Root endpoint hit")
    return {"message": "Welcome to my FastAPI!"}
