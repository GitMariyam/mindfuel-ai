from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum
import json
from datetime import datetime

app = FastAPI()

import os
LOG_FILE = os.path.join(os.path.dirname(__file__), "user_logs.jsonl")


@app.post("/log")
async def log_user_event(request: Request):
    try:
        data = await request.json()
        data["logged_at"] = datetime.utcnow().isoformat()  # Add server timestamp

        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")  # Append as JSON line

        return JSONResponse(content={"message": "User event logged successfully."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# For AWS Lambda via Mangum
lambda_handler = Mangum(app)

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)


