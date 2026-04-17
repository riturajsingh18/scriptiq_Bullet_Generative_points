# ScriptIQ – AI Story Intelligence Platform

## Overview

ScriptIQ is an AI-powered storytelling analysis platform that evaluates short scripts and provides actionable insights on:

- Story summary
- Emotional tone and arc
- Engagement potential
- Improvement suggestions
- Cliffhanger detection

It helps creators, writers, and content teams understand whether their story will resonate with audiences — before publishing.

---

## Key Features

- Script summarization (3–4 lines)
- Emotional analysis (dominant emotions + arc)
- Engagement scoring (0–10)
- AI-powered improvement suggestions
- Cliffhanger identification
- Simple UI for quick usage

---

## Architecture

Frontend (Streamlit)
↓
Backend API (FastAPI)
↓
LLM Engine (OpenAI GPT)


---

## Tech Stack

- Python
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- OpenAI GPT-4o-mini (LLM)
- Requests (API calls)
- python-dotenv (env management)

---

## Project Structure

scriptiq/
│
├── app/
│ ├── main.py
│ ├── routes.py
│
├── services/
│ ├── llm_service.py
│ ├── analysis_service.py
│
├── ui/
│ └── streamlit_app.py
│
├── requirements.txt
├── .env

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/riturajsingh18/scriptiq_Bullet_Generative_points.git
cd scriptiq_Bullet_Generative_points
2. Install Dependencies
pip install -r requirements.txt
3. Add Environment Variable

Create a .env file:

OPENAI_API_KEY=your_openai_api_key
Run Locally
Start Backend
uvicorn app.main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

Start Frontend
streamlit run ui/streamlit_app.py
Live Deployment
Backend: Deployed on Render
Frontend: Deployed on Streamlit Cloud

Example:

API: https://scriptiq-backend.onrender.com
App: https://scriptiq.streamlit.app

Sample Input
Title: The Last Message

Scene:
Riya receives a message from her ex-boyfriend after five years.

Dialogue:
Riya: Why now?
Arjun: Because today I learned the truth.
Riya: What truth?
Arjun: That the accident wasn't your fault.
Sample Output
Summary of story
Emotional arc (confusion → tension → revelation)
Engagement score
Suggestions for improvement
Key suspense moment
Prompt Strategy
Role-based prompting ("storytelling expert")
Structured instructions
Multi-output generation in a single response
Limitations
Output depends on LLM interpretation (subjective)
No fine-tuned storytelling model
Limited context for very long scripts
Future Improvements
Multi-agent analysis (critic + improver)
RAG with screenplay datasets
User authentication and saved scripts
Payment integration (Stripe)
Advanced scoring models
Use Cases
Content creators (YouTube, Instagram)
Script writers
OTT content teams
Marketing storytelling teams
Author

Rituraj Kumar
Senior Data Scientist | AI Engineer

Vision

“Transform storytelling into a measurable, improvable intelligence system using AI.”


---
