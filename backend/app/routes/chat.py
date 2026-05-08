from fastapi import APIRouter
from app.services.ollama_client import ask_llm
from app.observability.otel import tracer
from app.observability.logger import log_event
from app.observability.metrics import count_tokens, track_latency
import time

router = APIRouter()

@router.post("/chat")
def chat(req: dict):

    start = time.time()

    with tracer.start_as_current_span("chat-request"):

        prompt = req["prompt"]

        log_event("request_received", {"prompt": prompt})

        response = ask_llm(prompt)

        latency = track_latency(start)
        tokens = count_tokens(response)

        log_event("response_sent", {
            "response": response,
            "latency": latency,
            "tokens": tokens
        })

        return {
            "response": response,
            "latency": latency,
            "tokens": tokens
        }