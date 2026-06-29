from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from pypdf import PdfReader
from io import BytesIO
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ResumeResponse, ResumeMatchResponse, ResumeMatchRequest
from app.models import Resume
from app.utils.matcher import normalize_skills, calculate_match
from app.services.ai_service import AIService


router = APIRouter()

ai_service = AIService()

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
    
     
        
@router.post(
    '/resume-match',
    response_model= ResumeMatchResponse
)
def match_resume(
    request: ResumeMatchRequest,
    db: Session = Depends(get_db)
):
    # Get latest updated resume..
    latest_resume = (
        db.query(Resume).
        order_by(Resume.
        uploaded_at.desc()).
        first()
    )
    
    if not latest_resume:
        raise HTTPException(status_code=404, detail="No Resume Found!!!")
    
    # Extract skills
    
    resume_skills = ai_service.extract_skills(latest_resume.content)
    r_skills = resume_skills['technical_skills']
    r_skills = normalize_skills(r_skills)
    
    job_skills = ai_service.extract_skills(request.job_description)
    j_skills = job_skills['technical_skills']
    j_skills = normalize_skills(j_skills)
    
    match_data = calculate_match(r_skills, j_skills)
    
    return ResumeMatchResponse(
    match_score=match_data["match_score"],
    matched_skills=match_data["matched_skills"],
    missing_skills=match_data["missing_skills"]
)
