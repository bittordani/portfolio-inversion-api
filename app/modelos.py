from pydantic import BaseModel, Field, constr
from datetime import date
from typing import Optional, Annotated

class Inversion(BaseModel):
    id: int = Field(..., gt=0, description="ID debe ser mayor que 0")
    ticker: Annotated[str, constr(strip_whitespace=True, min_length=1, max_length=10)] = Field(..., description="Símbolo bursátil (ej: AAPL)")
    cantidad: int = Field(..., gt=0, description="Cantidad debe ser un número entero mayor que 0")
    precio_compra: float = Field(..., gt=0, description="Precio de compra debe ser mayor que 0")
    fecha_compra: date = Field(..., description="Fecha de compra en formato YYYY-MM-DD")
    sector: Annotated[str, constr(strip_whitespace=True, min_length=1, max_length=30)] = Field(..., description="Sector al que pertenece la inversión")
    observaciones: Optional[Annotated[str, constr(strip_whitespace=True, max_length=200)]] = Field(
        default=None,
        description="Comentario opcional, máximo 200 caracteres"
    )
