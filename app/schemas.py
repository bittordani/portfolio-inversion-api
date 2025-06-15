from pydantic import BaseModel, Field, constr
from typing import Optional, Annotated
from datetime import date

class InversionBase(BaseModel):
    ticker: Annotated[str, constr(strip_whitespace=True, min_length=1, max_length=10)] = Field(..., description="Símbolo bursátil (ej: AAPL)")
    cantidad: int = Field(..., gt=0, description="Cantidad debe ser mayor que 0")
    precio_compra: float = Field(..., gt=0, description="Precio de compra debe ser mayor que 0")
    fecha_compra: date = Field(..., description="Fecha de compra en formato YYYY-MM-DD")
    sector: Annotated[str, constr(strip_whitespace=True, min_length=1, max_length=30)] = Field(..., description="Sector de la inversión")
    observaciones: Optional[Annotated[str, constr(strip_whitespace=True, max_length=200)]] = Field(None, description="Observaciones opcionales")

class InversionCreate(InversionBase):
    id: int = Field(..., gt=0)

class InversionOut(InversionCreate):
    class Config:
        from_attributes = True
