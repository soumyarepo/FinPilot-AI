from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="notification-service", version="0.1.0")

class HealthResponse(BaseModel):
    status: str
    service: str

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="notification-service")

@app.get("/")
def root() -> dict:
    return {
        "service": "notification-service",
        "description": "Email and alert orchestration service."
    }

