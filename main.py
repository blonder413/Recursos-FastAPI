from fastapi import FastAPI
from routers import user

app = FastAPI()

# user.router hace referencia al archivo user y a la instancia router
app.include_router(user.router)

@app.get("/")
def inicio():
    """
    Esta es la ruta inicial del proyecto
    """
    return {"hello": "world"}


@app.get("/asincrono")
async def asincrono():
    return {"peticion": "¡soy asíncrono!"}