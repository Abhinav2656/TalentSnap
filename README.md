# TalentSnap: AI-Powered Resume Analyzer & Job Matcher

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-green)](https://fastapi.tiangolo.com/)

TalentSnap is an intelligent platform that bridges the gap between job seekers and recruiters using advanced AI techniques. It automatically analyzes resumes, matches candidates to relevant job opportunities, and provides actionable feedback to improve application success rates.

## 🧩 Problem Statement

Both recruiters and job seekers face significant challenges in effectively matching skills to job requirements:

- Recruiters struggle to efficiently identify qualified candidates among numerous applications
- Job seekers often submit poorly optimized resumes that don't highlight relevant skills
- Talented individuals miss opportunities they're well-suited for due to keyword mismatches
- Manual resume analysis is time-consuming and prone to unconscious biases

TalentSnap solves these problems by leveraging NLP and AI to create a more efficient, accurate job matching ecosystem.

## 🎯 Key Features

- **Resume Parsing**: Extract key information (skills, education, work experience) from uploaded PDF resumes using NLP
- **Intelligent Job Matching**: Match resumes to relevant job descriptions using semantic similarity algorithms
- **Resume Scoring**: Generate comprehensive scores based on resume strength and relevance to target positions
- **Improvement Suggestions**: Provide actionable AI-driven recommendations to enhance resume effectiveness
- **Skills Analysis**: Visualize user's skill strengths and gaps using interactive data dashboards
- **Job Market Insights**: Offer data-driven insights on in-demand skills and industry trends

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend API** | FastAPI |
| **NLP/AI** | spaCy, Transformers (HuggingFace), Scikit-learn |
| **PDF Parsing** | PyMuPDF (`fitz`) |
| **Similarity Matching** | Sentence Transformers, TF-IDF |
| **Database** | PostgreSQL (SQLite for development) |
| **Frontend** | React.js / Streamlit |
| **Data Visualization** | Plotly / Matplotlib |
| **Deployment** | Docker, Render.com or Railway.app |
| **Version Control** | Git, GitHub |

## 📋 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment tool (recommended)
- PostgreSQL (optional for production)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/talentsnap.git
cd talentsnap
```
### 2. Set up virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 
