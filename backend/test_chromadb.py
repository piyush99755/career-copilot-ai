from app.services.ai_service import AIService
from app.services.vector_service import VectorService

ai_service = AIService()
vector_service = VectorService()

text = """
Python FastAPI Developer
"""

embeddings = ai_service.generate_embedding(text)

vector_service.store_chunk(
    chunk_id="1",
    chunk_text=text,
    embedding=embeddings
    
    
)
print("Stored successfully")

print(
    f"Total chunks: {vector_service.count_chunks()}"
)