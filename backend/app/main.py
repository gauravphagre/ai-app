from app.observability.telemetry import setup_telemetry
from fastapi import FastAPI


app = FastAPI()

setup_telemetry(app)

@app.get("/")
def home():
    return {"status": "ok"}