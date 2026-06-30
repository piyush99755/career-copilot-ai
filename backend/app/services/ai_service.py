from ollama import chat
import json

class AIService:
    
    def extract_skills(self, text: str):
        
        prompt = f"""
        Extract technical skills from the following text.

        Return only JSON format.
        
        Text:

        {text}
        Do not include explanations.
        Do not include markdown.
        Do not include code fences.
        
        Format:
        
        {{
            "technical_skills" : []
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
        
        return json.loads(
                response["message"]["content"]
            )
        
        
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

        print(content)
        
        print(response["message"]["content"])

        roadmap_data = json.loads(content)
    
        if not roadmap_data.get("recommended_project"):
            roadmap_data["recommended_project"] = (
                f"Build a {role} portfolio project using "
                + ", ".join(missing_skills[:5])
          )
        
        
        return roadmap_data