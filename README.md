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

