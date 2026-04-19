from fastapi import APIRouter, Depends # Dependencia de criacao do usuário
from models import Usuario # Importar a tabela de usuários do nosso models.py
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Rota padrão de autenticação do sistema.
    """
    return {"mensagem": "Você acessou o endpoint de autenticação", "autenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(nome:str, email:str, senha:str, session = Depends(pegar_sessao)): # Como é uma dependência, não tem o risco de ser interpretado como parâmetro
    
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    
    if usuario:
        return {"mensagem": "já existe um usuário com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuário cadastrado com sucesso"}