Smart Document Analyzer

meakub@MacBookPro ai-document-analyzer % mkdir ai-document-analyzer && cd ai-document-analyzer

meakub@MacBookPro ai-document-analyzer % vim requirements.txt;                                


meakub@MacBookPro ai-document-analyzer % python3 -m venv venv                                 


meakub@MacBookPro ai-document-analyzer % vim .gitignore                                       

pip3 install fastapi uvicorn python-multipart aiofiles

-- fastapi => web framework to build REST api using python
-- uvicorn => light weight ASGI server used to run FastAPI app
-- command: uvicorn app.main:app --reload
-- python-multi-part => required to handle form data upload
-- aiofiles => used to asynchronously read/write files 

pip3 install python-dotenv

- help python app to read environment variables

pip3 install uvicorn

-- web server help run your app

Run command: 

install tesseract OCR
(venv) meakub@MacBookPro ai-document-analyzer % brew install tesseract

(venv) meakub@MacBookPro ai-document-analyzer % pip3 install pytesseract pdf2image


Working with VENV might cause some PATH issues. 

Make sure poppler has been added to the PATH or pass as params like below
convert_from_path(file_path, poppler_path="/opt/homebrew/bin")

Similarly apply PATH for tesseract like below
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

AI Model Integration

Install hugging face transformers

pip3 install transformers 

Install pytorch

 pip3 install torch --index-url https://download.pytorch.org/whl/cpu

 Since transformers library needs pytorch or TensorFlow as dependency

