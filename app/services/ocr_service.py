from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(file_path: str) -> str:
    images = convert_from_path(file_path)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
