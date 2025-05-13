from fastapi import APIRouter
from app.models.schema import TextRequest, SummaryResponse
from app.core.summarizer import summarize_text


router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize_endpoint(request: TextRequest):
    summary = summarize_text(request.text)
    return SummaryResponse(summary=summary)