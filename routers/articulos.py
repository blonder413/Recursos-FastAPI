from fastapi import FastAPI

app = FastAPI()

@app.get('articulos')
def articulos():
    return ["a1", "a2", "a3"]