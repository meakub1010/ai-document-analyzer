from pdf2image import convert_from_path
import pytesseract
from app.core.logger import logger
from pdf2image.exceptions import PDFInfoNotInstalledError

from PIL import Image
from pathlib import Path

# since using python venv, making sure PATH for tesseract is correctly found
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def extract_text_from_pdf(file_path: str) -> str:
    logger.info(f"file_path:{file_path}")
    try:
        # poppler_path="/opt/homebrew/bin" is optional just to make sure poppler is found in the correct PATH
        images = convert_from_path(file_path, poppler_path="/opt/homebrew/bin")
    except PDFInfoNotInstalledError as e:
        raise RuntimeError('Poppler is not installed or not in PATH')    
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text

def extract_from_image(image_path: str) -> str:
    logger.info(f"image_path:{image_path}")
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image=image)
        return text
    except Exception as e:
        raise RuntimeError(f"OCR failed: {e}")