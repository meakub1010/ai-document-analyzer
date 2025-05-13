from transformers import pipeline
from app.core.logger import logger

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question: str, context: str) -> dict:
    logger.info(f"answer_question: {question}")
    result = qa_pipeline({"context": context,
                         "question": question
                         })
    
    return {
        "answer": result["answer"],
        "confidence": result["score"]
    }