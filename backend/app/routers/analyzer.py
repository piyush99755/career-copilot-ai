from fastapi import APIRouter
from app.data.resume_profile import USER_SKILLS
from app.utils.matcher import calculate_match

router = APIRouter()

@router.post("/analyze")
def analyze_job(data: dict):

    text = data.get(
        "job_description",
        ""
    ).lower()

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