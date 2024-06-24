from fastapi import FastAPI
from .database import engine, Base
from .routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware


# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=["*"],  
)
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Olá IBBI !"}



