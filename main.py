from fastapi import FastAPI, HTTPException
from app.modelos import Inversion
from app.datos import inversiones
from typing import List
from fastapi import HTTPException


# Inicio de la app y comprobación de que la API funciona correctamente y mensaje de bienvenida
app = FastAPI(
    title="Portfolio de inversión con API",
    version="1.0",
    description="API en FastAPI para gestionar un portfolio de inversión en bolsa. " \
    "Incluye operaciones CRUD, documentación automática, logging y despliegue con Docker."
)

@app.get("/")
def inicio():
    return{"mensaje":"API para portfolio de inversión"}

# Endpoint para listar los movimientos
@app.get("/inversiones", response_model=List[Inversion])
def listar_inversiones():
    return inversiones

# Endpoint para listar los movimientos
@app.get("/inversiones/{id}", response_model=Inversion)
def obtener_inversion(id:int):
    for inversion in inversiones:
        if inversion.id == id:
            return inversion
    raise HTTPException(status_code=404, detail="Inversión no encontrada")
        

# Endpoint para crear nuevas inversiones a mi lista
@app.post("/inversiones", response_model=Inversion, status_code=201)
def crear_inversion(nueva: Inversion):
    # Si ya existe una inversión con ese ID
    if any(i.id == nueva.id for i in inversiones):
        raise HTTPException(status_code=400, detail="ID duplicado")

    # Si no, la añadimos
    inversiones.append(nueva)
    return nueva

# Endpoint para modificar un registro ya insertado con validación por ID
@app.put("/inversiones/{id}", response_model=Inversion)
def actualizar_inversion(id: int, datos_actualizados: Inversion):
    for indice, inversion in enumerate(inversiones):
        if inversion.id == id:
            inversiones[indice] = datos_actualizados
            return datos_actualizados
    raise HTTPException(status_code=404, detail="Inversión no encontrada")

