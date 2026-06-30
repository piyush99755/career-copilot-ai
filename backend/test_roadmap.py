from app.services.ai_service import AIService


ai_service = AIService()

result = ai_service.generate_learning_roadmap(
    matched_skills=[
        "python",
        "fastapi",
        "postgresql"
    ],
    missing_skills=[
        "aws",
        "docker"
    ],
    role="AI Full Stack Developer"
)

print(result)
print(type(result))