    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI(title="recommendation-service", version="0.1.0")

    class HealthResponse(BaseModel):
        status: str
        service: str

    @app.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok", service="recommendation-service")

    @app.get("/")
    def root() -> dict:
        return {
            "service": "recommendation-service",
            "description": "AI recommendation and risk scoring service."
        }

@app.get("/recommendations/{user_id}")
def recommendations(user_id: str) -> dict:
    return {
        "user_id": user_id,
        "risk_profile": "moderate",
        "allocation": {"equity": 60, "debt": 30, "gold": 10},
        "note": "Starter response. Replace with model-backed inference."
    }

