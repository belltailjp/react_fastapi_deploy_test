from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="../frontend/build/", html=True))

@app.get("/hello")
def hello():
    return {"Hello": "World"}

