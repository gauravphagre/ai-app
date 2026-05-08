import time
from prometheus_client import generate_latest

def count_tokens(text: str):
    return len(text.split())

def track_latency(start_time: float):
    return time.time() - start_time

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")