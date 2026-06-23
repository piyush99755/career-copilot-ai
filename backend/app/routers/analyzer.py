from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze_job(data: dict):
    text = data.get("job_description", "").lower()
    
    skills = []
    
    possible_skills = [
        "python",
        "react",
        "fastapi",
        "aws",
        "docker",
        "postgresql",
        "langchain",
        "langgraph",
        "javascript",
        "typescript"
    ]
    
    for skill in possible_skills:
        if skill in text:
            skills.append(skill)
       
    return {
        "role": "AI Developer",
        "skills": skills
    }     
    
    