from fastapi import FastAPI
from core.orchestrator import run_async_job

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run")
async def run_job():
    result = await run_async_job()
    return result