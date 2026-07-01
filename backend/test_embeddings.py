from app.services.ai_service import AIService

ai_service = AIService()

texts = [
    "Python Developer",
    "FastAPI Backend Engineer",
    "Pizza Recipe"
]

for text in texts:
    embedding = ai_service.generate_embedding(text)

    print(f"\n{text}")
    print(len(embedding))
    print(embedding[:5])