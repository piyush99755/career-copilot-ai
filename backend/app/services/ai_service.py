from ollama import chat, embeddings
import json

class AIService:
    def extract_skills(self, text: str):

        prompt = f"""
            Extract technical skills from the following text.

            Return ONLY valid JSON.

            Text:
            {text}

            Rules:
            - Do not include explanations.
            - Do not include markdown.
            - Do not include code fences.
            - Return only JSON.

            Format:

            {{
                "technical_skills": []
            }}
            """

        response = chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        content = response["message"]["content"]

        print("\n===== SKILL EXTRACTION RESPONSE =====")
        print(content)
        print("=====================================\n")

        try:
            start = content.find("{")
            end = content.rfind("}") + 1

            if start == -1 or end == 0:
                raise ValueError("No JSON found in model response")

            json_text = content[start:end]

            skills_data = json.loads(json_text)

            if "technical_skills" not in skills_data:
                skills_data = {"technical_skills": []}

            return skills_data

        except Exception as e:
            print(f"Skill extraction error: {e}")

            return {
                "technical_skills": []
            }
        
        
        
    def generate_learning_roadmap(
        self, 
        matched_skills: list[str],
        missing_skills: list[str],
        role: str
    ):
        if len(missing_skills) > 10:
            missing_skills = missing_skills[:5]
        
        prompt = f"""
            Create a practical learning roadmap for this role.

            Role:
            {role}

            Matched Skills:
            {matched_skills}

            Missing Skills:
            {missing_skills}

            STRICT RULES:

            - Generate EXACTLY 4 weeks.
            - Use ONLY these roadmap keys:
            week_1, week_2, week_3, week_4
            - Do NOT create week_5 or later.
            - Use ONLY skills from Missing Skills and related technologies.
            - Do NOT introduce unrelated frameworks or technologies.
            - Each week must contain 2-4 actionable learning tasks.
            - Tasks must start with action verbs such as:
            Build, Create, Implement, Deploy, Integrate, Learn, Configure, Develop.
            - Do NOT return skill names by themselves.
            - Do NOT include explanations.
            - Do NOT include markdown.
            - Do NOT include code fences.
            - Return ONLY valid JSON.
            - recommended_project must never be empty.
            - recommended_project must be specific.
            - recommended_project must include technologies from Missing Skills.
            - The roadmap should gradually progress from fundamentals to a portfolio-ready project.
            
            CONTENT RULES:

            CONTENT RULES:

            - Generate actionable tasks, not skill names.
            - Assume the user already knows basic programming.
            - Avoid beginner tutorials unless necessary.
            - Use matched skills as strengths.
            - Prioritize missing skills.

            - If the role contains AI, ML, LLM, GenAI, AI Engineer, AI Developer, AI SaaS Developer, or Machine Learning, allocate at least 50% of roadmap tasks to AI-specific skills such as LLM integration, RAG, vector databases, LangChain, Ollama, prompt engineering, and AI agent development.

            - At least 90% of roadmap tasks should focus on missing skills.
            - Every missing skill must appear at least once in either the roadmap or recommended_project.
            - Do not generate tasks unrelated to the missing skills list.
            - Do not spend roadmap time teaching matched skills.
            - Tasks should be portfolio-oriented and job-focused.
            - Avoid tasks such as "Learn basics", "Understand fundamentals", or "Develop understanding".
            - Prefer building tasks over studying tasks.
            - Every task should produce code, a feature, or a deployable artifact.
            - Assume the user already has programming experience.
            - Use real technologies only.
            - Do not invent technology names.
            - Prefer ChromaDB, Pinecone, Weaviate, Qdrant, FAISS, PostgreSQL pgvector.
            - Avoid vague tasks such as:
                "Ensure deployment works",
                "Optimize system",
                "Finalize project",
                "Learn concepts".
            - Every task must create a feature, API, deployment, integration, or production-ready component.
                        
            PROJECT RULES:

            - recommended_project must be portfolio-ready.
            - recommended_project must include at least 5 missing skills.
            - recommended_project must explicitly mention the technologies used.
            - recommended_project must solve a real-world business problem.
            - recommended_project title must be 8-20 words long.
            - recommended_project must align with the target role.
            - Prefer AI, SaaS, cloud-native, agentic AI, or full-stack projects.
            - Do not generate generic CRUD, blog, todo, calculator, or authentication-only projects.
            - recommended_project must include:
                frontend,
                backend,
                database,
                deployment,
                and AI functionality.

            - recommended_project must describe the business problem being solved.

            BAD:

            {{
            "week_1": [
                "python",
                "fastapi"
            ]
            }}

            GOOD:

            {{
            "week_1": [
                "Learn Python fundamentals",
                "Build a FastAPI CRUD API",
                "Create PostgreSQL database models"
            ]
            }}

            REQUIRED JSON FORMAT:

            {{
            "roadmap": {{
                "week_1": [],
                "week_2": [],
                "week_3": [],
                "week_4": []
            }},
            "recommended_project": ""
            }}
            """
        
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                    
                }
                
                
            ]
        ) 
        content = response["message"]["content"]

        print("\n===== ROADMAP RESPONSE =====")
        print(content)
        print("===========================\n")

        try:

            first_json_start = content.find("{")

            brace_count = 0
            json_end = 0

            for i in range(first_json_start, len(content)):
                if content[i] == "{":
                    brace_count += 1
                elif content[i] == "}":
                    brace_count -= 1

                    if brace_count == 0:
                        json_end = i + 1
                        break

            json_text = content[first_json_start:json_end]

            roadmap_data = json.loads(json_text)

        except Exception as e:

            print(f"Roadmap parsing error: {e}")

            roadmap_data = {
                "roadmap": {
                    "week_1": [],
                    "week_2": [],
                    "week_3": [],
                    "week_4": []
                },
                "recommended_project": ""
            }
    
        if not roadmap_data.get("recommended_project"):
            roadmap_data["recommended_project"] = (
                f"Build a {role} portfolio project using "
                + ", ".join(missing_skills[:5])
          )
        
        
        return roadmap_data
    
    
    def generate_embedding(self, text:str):
        response = embeddings(
            model="nomic-embed-text",
            prompt=text
        )
        
        return response["embedding"]
    
    def answer_with_context(
        self,
        question: str,
        context: str
    ):
        prompt = f"""
        Use ONLY the provided context.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
        
        response = chat(
            model="llama3.2",
            messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
            
        )
        
        return response["message"]["content"]
