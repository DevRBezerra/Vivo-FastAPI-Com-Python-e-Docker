from fastapi import APIRouter

from app.centro_treinamento.controller import router as centro_treinamento
from app.atleta.controller import router as atleta
from app.categorias.controller import router as categorias

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categorias, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])
