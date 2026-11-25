from fastapi import FastAPI

from api.router import api_router


app = FastAPI(
    title="Maple Leaf Resort - User Service",
    version="1.0.0"
)


app.include_router(
    api_router,
    prefix="/api"
)


@app.get("/")
def root():

    return {
        "message": "User Service is running"
    }