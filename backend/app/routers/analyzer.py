from fastapi import APIRouter

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

        ]

    }