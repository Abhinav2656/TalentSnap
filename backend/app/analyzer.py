import spacy
import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def analyze_resume(text: str) -> dict:
    doc = nlp(text)
    
    # Improved skills extraction
    skills = []
    for token in doc:
        # Add nouns and proper nouns (common in skills)
        if token.pos_ in ["NOUN", "PROPN"] and token.is_alpha:
            skills.append(token.text)
            
        # Add compound nouns (like "machine learning")
        if token.dep_ == "compound" and token.head.pos_ in ["NOUN", "PROPN"]:
            skills.append(f"{token.text} {token.head.text}")
    
    return {"skills": list(set(skills)), "text": text}

def match_jobs(resume_skills: list) -> list:
    print(f"Resume skills: {resume_skills}")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'jobs.json')
    
    try:
        with open(json_path) as f:
            jobs = json.load(f)
    except FileNotFoundError:
        return []
    
    if not resume_skills or not jobs:
        return []
    
    # Create skills matrix
    job_texts = [" ".join(job['keywords']) for job in jobs]
    vectorizer = TfidfVectorizer()
    
    # Combine resume skills and job texts
    all_texts = [" ".join(resume_skills)] + job_texts
    matrix = vectorizer.fit_transform(all_texts)
    
    # Convert to array format
    matrix_dense = matrix.toarray()
    
    # Calculate similarity
    cosine_sim = cosine_similarity([matrix_dense[0]], matrix_dense[1:])
    matches = []
    
    for i, score in enumerate(cosine_sim[0]):
        if score > 0.1:  # Threshold
            matches.append({
                "title": jobs[i]['title'],
                "company": jobs[i]['company'],
                "match_score": float(score),
                "required_skills": jobs[i]['keywords']
            })
    
    return sorted(matches, key=lambda x: x['match_score'], reverse=True)