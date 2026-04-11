from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

# Definindo requisições
@order_router.get("/")
async def orders():
    """
    Rota padrão de pedidos do sistema.
    """
    return {"mensagem": "Você acessou o endpoint de pedidos", "autenticado": False}