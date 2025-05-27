from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum


app = FastAPI()

@app.get("/fact")
async def get_fact(request: Request):
        return JSONResponse(content={"fact": "This is a placeholder MindFuel tip from Lambda container!"})

# For AWS Lambda via Mangum
lambda_handler = Mangum(app)

# For local testing you can comment this section when running for SAM


if __name__ == "__main__":
	import uvicorn    
	uvicorn.run(app, host="0.0.0.0", port=8000)



