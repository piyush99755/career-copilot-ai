from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from io import BytesIO

router = APIRouter()

@router.post('/upload-resume')
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    
    pdf = PdfReader(BytesIO(contents))
    
    text=""
    
    for page in pdf.pages:
        text += page.extract_text()
        
        
    return {
        "filename": file.filename,
        "text": text
        
    }