from fastapi import FastAPI, UploadFile, File
from .parser import extract_text
from .analyzer import analyze_resume, match_jobs
from .groq_client import get_feedback

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    # Extract text from PDF
    text = extract_text(await file.read())
    
    # Analyze resume
    analysis = analyze_resume(text)
    
    # Get AI feedback
    feedback = get_feedback(text)
    
    # Match jobs
    matched_jobs = match_jobs(analysis['skills'])
    
    return {
        "analysis": analysis,
        "feedback": feedback,
        "matched_jobs": matched_jobs
    }