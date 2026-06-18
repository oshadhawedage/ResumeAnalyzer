from fastapi import FastAPI, UploadFile, File
import os

from utils.pdf_parser import extract_text_from_pdf

app = FastAPI()

UPLOAD_DIR = "uploads"

# create uploads folder if not exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Resume Analyzer API is running"}



@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # save file

    with open(file_path, "wb") as buffer:

        buffer.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)    

    return {

        "filename": file.filename,
        "extracted_text": extracted_text

    }