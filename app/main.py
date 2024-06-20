from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router as api_router

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas da API
app.include_router(api_router)
