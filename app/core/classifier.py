from transformers import pipeline


classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

CANDIDATE_LABELS = ["invoice", "legal", "resume", "medical", "financial", "other"]

def classify_text(text: str) -> str:
    result = classifier(text, CANDIDATE_LABELS)
    return result['labels'][0]