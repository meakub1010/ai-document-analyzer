from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

class ClassificationResponse(BaseModel):
    category: str

class QARequest(BaseModel):
    document_id: str
    question: str

class QAResponse(BaseModel):
    answer: str
    confidence: float