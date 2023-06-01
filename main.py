from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def inicio():
    """
    Esta es la ruta inicial del proyecto
    """
    return {"hello": "world"}


@app.get("/asincrono")
async def asincrono():
    return {"peticion": "¡soy asíncrono!"}