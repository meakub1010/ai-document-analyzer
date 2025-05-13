from fastapi import APIRouter
from app.models.schema import TextRequest, ClassificationResponse
from app.core.classifier import classify_text

router = APIRouter()

@router.post("/classify", response_model=ClassificationResponse)
async def classify_endpoint(request: TextRequest):
    category = classify_text(request.text)
    return 