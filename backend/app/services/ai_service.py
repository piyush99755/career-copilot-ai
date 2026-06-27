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