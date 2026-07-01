from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime
)

from sqlalchemy.orm import declarative_base
from datetime import datetime
from app.database import Base


class Analysis(Base):

    __tablename__ = "analyses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role = Column(
        String
    )

    skills = Column(
        Text
    )

    difficulty = Column(
        String
    )

    market_demand = Column(
        String
    )

    match_score = Column(
        Integer
    )
    
class Resume(Base):
    __tablename__ = "resumes"
    
    id = Column(Integer, primary_key=True, index=True )
    
    filename = Column(String, nullable=False)
    
    content= Column(Text, nullable=False)
    
    uploaded_at= Column(DateTime, default=datetime.utcnow)
    
class ConversationMessage(Base):
    __tablename__ = "conversation_messages"
    
    id = Column(Integer, index=True, primary_key=True)
    
    conversation_id = Column(String,nullable=True)
    
    role = Column(String, nullable=False)
    
    content = Column(Text, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)