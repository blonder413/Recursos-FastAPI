# Crear entorno virtual
```
sudo apt install python3.10-venv
python3 -m venv .venv
```
# Activar entorno virtual
```
source .venv/bin/activate
```

# Instalar
```
pip install fastapi
```

# Instalamos el servidor [uvicorn](https://www.uvicorn.org/)
```
pip install uvicorn
```

# Correr el servidor
Para correr el servidor nombramos el archivo, le agregamos dos puntos y seguido el nombre de la instancia de FastAPI
```
uvicorn main:app --reload
```

# Documentación
Automáticamente se crea documentación con Swagger
```
http://127.0.0.1:8000/docs
```

También está disponible la documentación con redoc
```
http://127.0.0.1:8000/redoc
```

# Métodos HTTP
- POST: Para crear datos
- GET: Para leer datos
- PUT: Para actualizar datos
- PATCH: Para actualizar un solo campo
- DELETE: Para eliminar datos