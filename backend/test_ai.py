from app.services.ai_service import AIService
from app.utils.matcher import normalize_skills

ai = AIService()

result = ai.extract_skills(
    """
    Looking for a Python developer with
    FastAPI, PostgreSQL, AWS and Docker.
    """
)

skills = result["technical_skills"]

normalized = normalize_skills(skills)

print(normalized)