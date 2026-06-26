KNOWN_SKILLS = [
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


def extract_skills(text: str):

    text = text.strip().lower()

    skills = []

    for skill in KNOWN_SKILLS:

        if skill in text:

            skills.append(skill)

    return skills


def calculate_match(candidate_skills, required_skills):

    matched = []

    missing = []

    for skill in required_skills:

        if skill in candidate_skills:

            matched.append(skill)

        else:

            missing.append(skill)

    score = 0

    if len(required_skills) > 0:

        score = round(

            len(matched)

            / len(required_skills)

            * 100

        )

    return {

        "match_score": score,

        "matched_skills": matched,

        "missing_skills": missing

    }