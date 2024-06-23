from fastapi import FastAPI
from .database import engine, Base
from .routes import router as api_router

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas da API
app.include_router(api_router)

# Rota raiz (opcional, para verificar se a API está funcionando)
@app.get("/")
def read_root():
    return {"message": "Olá IBBI !"}



