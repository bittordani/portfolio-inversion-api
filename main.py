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
        

