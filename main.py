import uvicorn
from base import handle_cors
from fastapi import FastAPI

app = FastAPI()
handle_cors(app)


@app.get("/")
async def home():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
