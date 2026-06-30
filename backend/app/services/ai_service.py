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
        prompt = f"""
        Create a 4-week learning roadmap.
        Do not include explanations.
        Do not include markdown.
        Do not include code fences.
        Return ONLY raw JSON.

        Role:
        {role}

        Matched Skills:
        {matched_skills}

        Missing Skills:
        {missing_skills}

        Return ONLY valid JSON.

        Format:

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

        return json.loads(content)
        
        
        