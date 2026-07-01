from app.services.vector_service import VectorService

vector_service = VectorService()

print(
    vector_service.get_all_chunks()
)