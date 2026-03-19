from fastapi import APIRouter
from typing import Optional
from app.controllers import temperatura_controller

router = APIRouter()

@router.post("/temperatura")
def guardar(valor: float):
    return temperatura_controller.guardar_temperatura(valor)

# 👇 GET con parámetros
@router.get("/datos")
def listar(min_temp: Optional[float] = None, max_temp: Optional[float] = None):
    return temperatura_controller.obtener_datos(min_temp, max_temp)
