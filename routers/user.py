from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/usuario", 
                    responses={404: {"mensaje": "no encontrado"}},
                    tags=["usuario"])   # tags sirve para la documentación

class Usuario(BaseModel):
    id: int
    name: str
    user: str
    edad: int


lista_usuarios = [
    Usuario(id=1, name="blonder", user="blonder413", edad=413),
    Usuario(id=2, name="jill", user="jvalentine", edad=40),
]


@router.get("/lista-json")
def lista_json():
    return [
        {"name": "blonder", "user": "blonder413", "edad": 413},
        {"name": "jill", "user": "jvalentine", "edad": 40},
        {"name": "claire", "user": "credfield", "edad": 36}
        ]

@router.get('/', response_model=list)
def usuarios():
    # return Usuario(name="blonder", user="blonder413", edad=413)
    return lista_usuarios


@router.get('/{id}', response_model=Usuario)
def usuario(id: int):
    usuario = filter(lambda user: user.id == id, lista_usuarios)
    # return list(usuario)
    try:
        return list(usuario)[0]
    except:
        # raise HTTPException(status_code = 204)
        # raise HTTPException(status_code = 404, detail={"mensaje": "usuario no encontrado", "status": 404})
        raise HTTPException(status_code = 240, detail={"mensaje": "usuario no encontrado", "status": 240})  # Personalizado


@router.get('/', response_model=Usuario)
def usuario(id: int):
    # http://localhost:8000/usuario/?id=1
    usuario = filter(lambda user: user.id == id, lista_usuarios)
    # return list(usuario)
    try:
        return list(usuario)[0]
    except:
        return {"status": 404, "mensaje": "usuario no encontrado"}

@router.post("/", status_code=201)
async def usuario(usuario: Usuario):
    lista_usuarios.append(usuario)
    return lista_usuarios

@router.put("/")
async def usuario(usuario: Usuario):
    for i, v in enumerate(lista_usuarios):
        if v.id == usuario.id:
            lista_usuarios[i] = usuario

    return lista_usuarios

@router.delete("/{id}")
async def usuario(id: int):
    for i, v in enumerate(lista_usuarios):
        if v.id == id:
            del(lista_usuarios[i])

    return lista_usuarios
