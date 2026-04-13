from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/sync-endpoint")
def sync_task():
    time.sleep(1)
    return {"message": "Sync Task Completed"}

@app.get("/async-endpoint")
async def async_task():
    await asyncio.sleep(1)
    return {"message": "Async Task Completed"}