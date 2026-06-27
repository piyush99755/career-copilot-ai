from app.utils.matcher import normalize_skills

skills = [
    "Python",
    " python ",
    "FASTAPI",
    "Docker",
    "docker"
]

print(normalize_skills(skills))