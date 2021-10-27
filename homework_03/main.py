from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    """
    Get Hello World.
    """
    return {"Hello": "World"}


@app.get("/ping/")
async def ping():
    """
    Get server status.
    """
    return {"message": "pong"}
