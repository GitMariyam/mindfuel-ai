from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum
import httpx
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
LOGGER_URL = os.getenv("LOGGER_SERVICE_URL", "http://localhost:8001/log")

@app.get("/fact")
async def get_fact(request: Request):
    log_payload = {
        "event": "fact_requested",
        "client_host": request.client.host
    }

    try:
        timeout = httpx.Timeout(5.0, connect=2.0)
        async with httpx.AsyncClient(timeout=timeout) as client:
           response =  await client.post(LOGGER_URL, json=log_payload)
           logger.info(f"Sent log to logger_service: status {response.status_code}")
    except Exception as e:
        logger.warning(f"Logging service failed: {e}")

    return JSONResponse(content={"fact": "This is a placeholder MindFuel tip from Lambda container!"})

lambda_handler = Mangum(app)

# print("🔥 ai_service received a request") this was added to troublshoot

if __name__ == "__main__":
    import uvicorn    
    uvicorn.run(app, host="0.0.0.0", port=8000)
