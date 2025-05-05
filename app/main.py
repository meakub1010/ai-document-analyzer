from fastapi import FastAPI
from app.api import upload
from app.core.logger import logger

app = FastAPI()
app.include_router(upload.router)

@app.get("/")
def read_root():
    logger.info("Root endpoint hit")
    return {"message": "Welcome to my FastAPI!"}
