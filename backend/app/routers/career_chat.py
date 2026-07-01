from fastapi import FastAPI, APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import CareerChatRequest, CareerChatResponse
from app.services.ai_service import AIService
from app.services.vector_service import VectorService
from app.database import get_db
from app.models import ConversationMessage

router = APIRouter()
ai_service = AIService()
vector_service = VectorService()


@router.post("/career-chat", response_model=CareerChatResponse)
def career_chat(
    request: CareerChatRequest,
    db: Session = Depends(get_db)):
    
    user_message = ConversationMessage(
        role="user",
        content=request.question
    )

    db.add(user_message)
    db.commit()
    
    history = (
        db.query(ConversationMessage)
            .order_by(
                ConversationMessage.created_at.desc()
            )
            .limit(10)
            .all()
    )
    
    conversation_history = ""
    
    for message in reversed(history):
        conversation_history += (
        f"{message.role}: "
        f"{message.content}\n"
    )
    
    print(conversation_history)
    
    query_embedding = ai_service.generate_embedding(request.question)
    
    results = vector_service.search_chunks(query_embedding)
    
    documents = results["documents"][0]
    
    context = "\n".join(documents)
    
    answer = ai_service.answer_with_context(request.question, context, conversation_history)
    
    assistant_message = ConversationMessage(
        role="assistant",
        content=answer
    )

    db.add(assistant_message)
    db.commit()
    
    return CareerChatResponse(answer = answer)


    
    

