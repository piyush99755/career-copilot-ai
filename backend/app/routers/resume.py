from fastapi import APIRouter, UploadFile, File, Depends
from pypdf import PdfReader
from io import BytesIO
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ResumeResponse
from app.models import Resume


router = APIRouter()

@router.post(
    '/upload-resume',
    response_model=ResumeResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session=Depends(get_db)
):
        
    contents = await file.read()
    
    pdf = PdfReader(BytesIO(contents))
    
    text=""
    
    for page in pdf.pages:
        text += page.extract_text()
        
    resume = Resume(
        filename= file.filename,
        content= text
    )
    
    db.add(resume)
    db.commit()
    db.refresh(resume)
    
    return resume
    
     
        
