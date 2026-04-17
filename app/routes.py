from fastapi import APIRouter
from app.services.analysis_service import analyze_script
#from services.analysis_service import analyze_script

router = APIRouter()

@router.get("/")
def home():
    return {"message": "ScriptIQ API is running 🚀"}

@router.post("/analyze")
def analyze(data: dict):
    script = data.get("script", "")
    result = analyze_script(script)
    return {"result": result}