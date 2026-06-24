from fastapi import APIRouter
from app.data.resume_profile import USER_SKILLS
from app.utils.matcher import calculate_match
from app.database import SessionLocal
from app.models import Analysis
from app.schemas import JobRequest

router = APIRouter()

@router.post("/analyze")
def analyze_job(data: JobRequest):

    text = data.job_description.strip().lower()

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

        "typescript",

        "openai",

        "ai agents",

        "next.js"
    ]

    skills = []

    for skill in possible_skills:

        if skill in text:

            skills.append(skill)

    difficulty = "Beginner"

    if len(skills) >= 3:

        difficulty = "Intermediate"

    if len(skills) >= 6:

        difficulty = "Advanced"
        
    match_data = calculate_match(

    skills,

    USER_SKILLS

    )
    
    db = SessionLocal()

    analysis = Analysis(

            role="AI Full Stack Developer",

            skills=", ".join(skills),

            difficulty=difficulty,

            market_demand="High",

            match_score=match_data["match_score"]

        )

    db.add(analysis)

    db.commit()

    db.refresh(analysis)

    db.close()
            
            

    return {

        "role":

        "AI Full Stack Developer",

        "skills":

        skills,

        "difficulty":

        difficulty,

        "market_demand":

        "High",

        "recommended_learning": [

            "Docker",

            "AI integrations",

            "Deployment",

            "RAG basics"

        ],
        
        "match_score": match_data["match_score"],

        "matched_skills": match_data["matched_skills"],

        "missing_skills": match_data["missing_skills"],

    }
    
# history endpoint
@router.get('/history')
def get_history():
    
    db = SessionLocal()
    
    analyses = db.query(
        Analysis
    ).all()
    
    results = []
    
    for analysis in analyses:
        results.append({

            "id":

            analysis.id,

            "role":

            analysis.role,

            "skills":

            analysis.skills,

            "difficulty":

            analysis.difficulty,

            "market_demand":

            analysis.market_demand,

            "match_score":

            analysis.match_score

        })

    
    db.close()
    
    return results
        
    
