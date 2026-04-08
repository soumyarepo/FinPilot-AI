    from fastapi import FastAPI
    from pydantic import BaseModel

    app = FastAPI(title="portfolio-service", version="0.1.0")

    class HealthResponse(BaseModel):
        status: str
        service: str

    @app.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok", service="portfolio-service")

    @app.get("/")
    def root() -> dict:
        return {
            "service": "portfolio-service",
            "description": "Portfolio holdings and valuation service."
        }

@app.get("/portfolio/{user_id}")
def portfolio(user_id: str) -> dict:
    return {
        "user_id": user_id,
        "holdings": [
            {"symbol": "NIFTYBEES", "quantity": 20, "value": 5120},
            {"symbol": "GOLDBEES", "quantity": 10, "value": 6500}
        ],
        "total_value": 11620
    }

