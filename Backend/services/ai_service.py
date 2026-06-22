import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text):
    prompt = f"""
You are an expert ATS resume reviewer.

Analyze this resume and return:

1. ATS Score (0-100)
2. Strengths
3. Weaknesses
4. Missing Skills
5. Improvement Suggestions

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text