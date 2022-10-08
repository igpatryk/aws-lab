from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def hello():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"status": "UP"}
