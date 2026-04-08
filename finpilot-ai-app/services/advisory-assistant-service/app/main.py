    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI(title="advisory-assistant-service", version="0.1.0")

    class HealthResponse(BaseModel):
        status: str
        service: str

    @app.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok", service="advisory-assistant-service")

    @app.get("/")
    def root() -> dict:
        return {
            "service": "advisory-assistant-service",
            "description": "Conversational advisory assistant service."
        }

from fastapi import Body

@app.post("/chat")
def chat(payload: dict = Body(...)) -> dict:
    message = payload.get("message", "")
    user_id = payload.get("user_id", "anonymous")
    return {
        "user_id": user_id,
        "message": message,
        "response": (
            "This is a starter advisory response. "
            "Replace this with intent routing, Redis session context, "
            "internal service enrichment, and optional LLM formatting."
        ),
    }

