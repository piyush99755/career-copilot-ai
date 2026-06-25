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
    