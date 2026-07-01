from fastapi import FastAPI, APIRouter, HTTPException
from app.schemas import CareerChatRequest, CareerChatResponse
from app.services.ai_service import AIService
from app.services.vector_service import VectorService

router = APIRouter()
ai_service = AIService()
vector_service = VectorService()


@router.post("/career-chat", response_model=CareerChatResponse)
def career_chat(request: CareerChatRequest):
    
    query_embedding = ai_service.generate_embedding(request.question)
    
    results = vector_service.search_chunks(query_embedding)
    
    documents = results["documents"][0]
    
    context = "\n".join(documents)
    
    answer = ai_service.answer_with_context(request.question, context)
    
    return CareerChatResponse(answer = answer)


    
    

