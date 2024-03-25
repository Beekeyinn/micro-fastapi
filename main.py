import uvicorn
from fastapi import FastAPI, Request

from base import setup

app = FastAPI()


@app.get("/")
async def home(request: Request, name: str | None = None):
    return {"message": "Hello World", "request": request.query_params}


setup(app)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
