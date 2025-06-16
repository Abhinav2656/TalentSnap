import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_feedback(resume_text: str) -> str:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You're a career coach providing resume feedback"},
            {"role": "user", "content": f"Provide concise suggestions to improve this resume:\n\n{resume_text[:3000]}"}
        ],
        temperature=0.5,
        max_tokens=512
    )
    return response.choices[0].message.content or ""