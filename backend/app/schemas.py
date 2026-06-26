from pydantic import BaseModel
from datetime import datetime


class JobRequest(BaseModel):
    job_description: str
    
class ResumeResponse(BaseModel):
    id: int
    filename: str
    content: str
    uploaded_at: datetime
    
    class config:
        from_attributes = True

class ResumeMatchRequest(BaseModel):
    job_description:str
    
class ResumeMatchResponse(BaseModel):
    match_score: int
    matched_skills: list[str]
    missing_skills: list[str]   