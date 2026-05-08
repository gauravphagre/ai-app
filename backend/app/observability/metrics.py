import time

def count_tokens(text: str):
    return len(text.split())

def track_latency(start_time: float):
    return time.time() - start_time