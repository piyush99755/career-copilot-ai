from app.services.chunking_service import ChunkingService

chunk_service = ChunkingService()

resume_text = """
Software Engineering & AI Contributor

PROFESSIONAL SUMMARY

MSc Computational Science student with experience building full-stack applications using Python,
FastAPI, React, TypeScript and SQL. Strong foundation in algorithms, data structures, machine
learning, software engineering, API design, debugging and version control. Interested in AI
evaluation, software engineering challenges and technical problem solving.

TECHNICAL SKILLS

Python, TypeScript, JavaScript, SQL, FastAPI, React, PostgreSQL, REST APIs, Git, GitHub,
Docker, JWT Authentication, SQLAlchemy, AWS Fundamentals

PROJECT EXPERIENCE

Nail Art Booking Platform: Developed a full-stack application using FastAPI, React, PostgreSQL
and TypeScript. Implemented authentication, booking workflows, payment integration, API
endpoints, database modeling and deployment workflows.

EDUCATION

MSc Computational Science – Laurentian University (Expected 2028)

Relevant Coursework: Machine Learning, Data Structures, Mathematics, Computational Science

BSc Computer Games Development – University of Bedfordshire
"""

chunks = chunk_service.chunk_text(resume_text)
print(len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)