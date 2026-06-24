from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

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