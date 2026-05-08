from app.observability.telemetry import setup_telemetry
from fastapi import FastAPI
from app.routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

setup_telemetry(app)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"status": "ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)