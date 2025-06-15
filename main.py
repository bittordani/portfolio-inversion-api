from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.database import engine, Base
from app.modelos import Inversion
from app.schemas import InversionOut, InversionCreate  # crea InversionCreate si no existe

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio de inversión con API",
    version="1.0",
    description="API en FastAPI para gestionar un portfolio de inversión en bolsa. " \
                "Incluye operaciones CRUD, validaciones, logging y despliegue con Docker."
)

# Dependencia para inyectar la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    return {"mensaje": "API para portfolio de inversión"}


@app.get("/inversiones", response_model=List[InversionOut])
def listar_inversiones(db: Session = Depends(get_db)):
    return db.query(Inversion).all()


@app.get("/inversiones/{id}", response_model=InversionOut)
def obtener_inversion(id: int, db: Session = Depends(get_db)):
    inversion = db.query(Inversion).filter(Inversion.id == id).first()
    if inversion is None:
        raise HTTPException(status_code=404, detail="Inversión no encontrada")
    return inversion


@app.post("/inversiones", response_model=InversionOut, status_code=201)
def crear_inversion(nueva: InversionCreate, db: Session = Depends(get_db)):
    if db.query(Inversion).filter(Inversion.id == nueva.id).first():
        raise HTTPException(status_code=400, detail="ID duplicado")
    inversion = Inversion(**nueva.dict())
    db.add(inversion)
    db.commit()
    db.refresh(inversion)
    return inversion


@app.put("/inversiones/{id}", response_model=InversionOut)
def actualizar_inversion(id: int, datos_actualizados: InversionCreate, db: Session = Depends(get_db)):
    inversion = db.query(Inversion).filter(Inversion.id == id).first()
    if not inversion:
        raise HTTPException(status_code=404, detail="Inversión no encontrada")
    for key, value in datos_actualizados.dict().items():
        setattr(inversion, key, value)
    db.commit()
    db.refresh(inversion)
    return inversion


@app.delete("/inversiones/{id}", status_code=204)
def eliminar_inversion(id: int, db: Session = Depends(get_db)):
    inversion = db.query(Inversion).filter(Inversion.id == id).first()
    if not inversion:
        raise HTTPException(status_code=404, detail="Inversión no encontrada")
    db.delete(inversion)
    db.commit()
    return
