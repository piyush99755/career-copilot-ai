from app.services.ai_service import AIService
from app.services.vector_service import VectorService

ai_service = AIService()
vector_service = VectorService()

resume_chunk = """
Python FastAPI React PostgreSQL AWS
"""

embedding = ai_service.generate_embedding(resume_chunk)

vector_service.store_chunk(
    chunk_id="2",
    chunk_text=resume_chunk,
    embedding=embedding
)

question = "What backend technologies do I know?"

query_embedding = ai_service.generate_embedding(question)

result = vector_service.search_chunks(query_embedding)

print("\nRetrieved Documents:")

for doc in result["documents"][0]:
    print(doc)