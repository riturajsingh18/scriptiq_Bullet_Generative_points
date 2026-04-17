from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="ScriptIQ API")

app.include_router(router)