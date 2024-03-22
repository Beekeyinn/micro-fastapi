import uvicorn
from fastapi import FastAPI

from base import setup

app = FastAPI()
setup(app)


@app.get("/")
async def home():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
