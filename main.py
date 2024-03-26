import uvicorn
from fastapi import FastAPI

from base import setup
from routers.users import user_router

app = FastAPI()
setup(app)
app.include_router(user_router, prefix="/api/v1/users")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
