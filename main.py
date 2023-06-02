from fastapi import FastAPI
from routers import user
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# user.router hace referencia al archivo user y a la instancia router
app.include_router(user.router)

# exponer recursos estáticos
app.mount("/estatico", StaticFiles(directory="static"), name="ruta_static")
# app.mount("/estatico", StaticFiles(directory="static/images"), name="ruta_static")

@app.get("/")
def inicio():
    """
    Esta es la ruta inicial del proyecto
    """
    return {"hello": "world"}


@app.get("/asincrono")
async def asincrono():
    return {"peticion": "¡soy asíncrono!"}