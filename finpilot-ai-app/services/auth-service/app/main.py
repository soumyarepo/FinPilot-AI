from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="auth-service", version="0.1.0")

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="auth-service")

@app.get("/")
def root() -> dict:
    return {
        "service": "auth-service",
        "description": "Authentication and JWT service."
    }

