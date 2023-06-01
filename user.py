from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    id: int
    name: str
    user: str
    edad: int


lista_usuarios = [
    Usuario(id=1, name="blonder", user="blonder413", edad=413),
    Usuario(id=2, name="jill", user="jvalentine", edad=40),
]


@app.get("/lista-json")
def lista_json():
    return [
        {"name": "blonder", "user": "blonder413", "edad": 413},
        {"name": "jill", "user": "jvalentine", "edad": 40},
        {"name": "claire", "user": "credfield", "edad": 36}
        ]

@app.get('/usuarios')
def usuarios():
    # return Usuario(name="blonder", user="blonder413", edad=413)
    return lista_usuarios


@app.get('/usuario/{id}')
def usuario(id: int):
    usuario = filter(lambda user: user.id == id, lista_usuarios)
    # return list(usuario)
    try:
        return list(usuario)[0]
    except:
        return {"status": 404, "mensaje": "usuario no encontrado"}


@app.get('/usuario/')
def usuario(id: int):
    # http://localhost:8000/usuario/?id=1
    usuario = filter(lambda user: user.id == id, lista_usuarios)
    # return list(usuario)
    try:
        return list(usuario)[0]
    except:
        return {"status": 404, "mensaje": "usuario no encontrado"}

@app.post("/usuario/")
async def usuario(usuario: Usuario):
    lista_usuarios.append(usuario)
    return lista_usuarios

@app.put("/usuario/")
async def usuario(usuario: Usuario):
    for i, v in enumerate(lista_usuarios):
        if v.id == usuario.id:
            lista_usuarios[i] = usuario

    return lista_usuarios

@app.delete("/usuario/{id}")
async def usuario(id: int):
    for i, v in enumerate(lista_usuarios):
        if v.id == id:
            del(lista_usuarios[i])

    return lista_usuarios
