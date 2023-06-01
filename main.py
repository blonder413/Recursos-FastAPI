from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def inicio():
    return {"hello": "world"}


@app.get("/asincrono")
async def asincrono():
    return {"peticion": "¡soy asíncrono!"}