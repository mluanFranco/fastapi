from models import db
from sqlalchemy.orm import sessionmaker # Criação de sessões do banco de dados

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()