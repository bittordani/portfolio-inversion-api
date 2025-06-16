from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import logging
from app.database import SessionLocal, engine, Base
from app.modelos import Inversion
from app.schemas import InversionOut, InversionCreate

# 📝 Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


app = FastAPI(
    title="Portfolio de inversión con API",
    version="1.0",
    description="API en FastAPI para gestionar un portfolio de inversión en bolsa. "
                "Incluye operaciones CRUD, validaciones, logging y despliegue con Docker."
)

# 🧱 Crear las tablas en la base de datos
@app.on_event("startup")
def startup():
    logging.info("⏳ Creando las tablas si no existen...")
    Base.metadata.create_all(bind=engine)
    logging.info("✅ Tablas listas")
    

# 📦 Dependencia para inyectar sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def inicio():
    logging.info("Inicio de la API")
    return {"mensaje": "API para portfolio de inversión"}


@app.get("/inversiones", response_model=List[InversionOut])
def listar_inversiones(db: Session = Depends(get_db)):
    inversiones = db.query(Inversion).all()
    logging.info(f"Consultadas {len(inversiones)} inversiones")
    return inversiones


@app.get("/inversiones/{id}", response_model=InversionOut)
def obtener_inversion(id: int, db: Session = Depends(get_db)):
    inversion = db.query(Inversion).filter(Inversion.id == id).first()
    if inversion is None:
        logging.warning(f"Inversión con ID {id} no encontrada")
        raise HTTPException(status_code=404, detail="Inversión no encontrada")
    logging.info(f"Inversión consultada: ID {id}")
    return inversion


@app.post("/inversiones", response_model=InversionOut, status_code=201)
def crear_inversion(nueva: InversionCreate, db: Session = Depends(get_db)):
    if db.query(Inversion).filter(Inversion.id == nueva.id).first():
        logging.warning(f"Intento de crear inversión duplicada con ID {nueva.id}")
        raise HTTPException(status_code=400, detail="ID duplicado")

    inversion = Inversion(**nueva.dict())
    db.add(inversion)
    db.commit()
    db.refresh(inversion)
    logging.info(f"Inversión creada: {inversion.ticker} con ID {inversion.id}")
    return inversion


@app.put("/inversiones/{id}", response_model=InversionOut)
def actualizar_inversion(id: int, datos_actualizados: InversionCreate, db: Session = Depends(get_db)):
    inversion = db.query(Inversion).filter(Inversion.id == id).first()
    if not inversion:
        logging.warning(f"Intento de actualizar inversión inexistente: ID {id}")
        raise HTTPException(status_code=404, detail="Inversión no encontrada")

    for key, value in datos_actualizados.dict().items():
        setattr(inversion, key, value)

    db.commit()
    db.refresh(inversion)
    logging.info(f"Inversión actualizada: ID {id}")
    return inversion


@app.delete("/inversiones/{id}", status_code=204)
def eliminar_inversion(id: int, db: Session = Depends(get_db)):
    inversion = db.query(Inversion).filter(Inversion.id == id).first()
    if not inversion:
        logging.warning(f"Intento de eliminar inversión inexistente: ID {id}")
        raise HTTPException(status_code=404, detail="Inversión no encontrada")

    db.delete(inversion)
    db.commit()
    logging.info(f"Inversión eliminada: ID {id}")
