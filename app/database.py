from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuração da URL do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Criando a engine do banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Criando uma classe base para os modelos
Base = declarative_base()

# Criando uma sessionmaker para gerar instâncias de Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter uma instância de Session do banco de dados
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
