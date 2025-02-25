from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json

app = FastAPI()

# Estou utilizando dados mockados
def carregar_dados():
    with open("./data/entregadores_mock.json", "r") as file:
        return json.load(file)

def salvar_dados(dados):
    with open("entregadores_mock.json", "w") as file:
        json.dump(dados, file, indent=4)

class AtualizarEstado(BaseModel):
    novo_estado: str

ESTADOS_VALIDOS = [
    "Disponível", 
    "Aguardando Pedido", 
    "A Caminho do Pedido",
    "Pedido Coletado", 
    "Entregando", 
    "Pedido Entregue", 
    "Indisponível"
]

# Rotas
@app.get("/entregadores")
def listar_entregadores():
    dados = carregar_dados()
    return dados["entregadores"]

@app.get("/entregadores/{entregador_id}")
def buscar_entregador(entregador_id: int):
    dados = carregar_dados()["entregadores"]
    entregador = next((entregador for entregador in dados if entregador["id"] == entregador_id), None)
    
    if not entregador:
        raise HTTPException(status_code=404, detail="Entregador não encontrado")
    return entregador

@app.put("/entregadores/{entregador_id}/estado")
def atualizar_estado(entregador_id: int, atualizar: AtualizarEstado):
    novo_estado = atualizar.novo_estado
    if novo_estado not in ESTADOS_VALIDOS:
        raise HTTPException(status_code=400, detail="Estado inválido")

    entregadores = carregar_dados()["entregadores"]
    entregador = next((entregador for entregador in entregadores if entregador["id"] == entregador_id), None)

    if not entregador:
        raise HTTPException(status_code=404, detail="Entregador não encontrado")

    if novo_estado == "Pedido Entregue":
        novo_estado = "Disponível"

    entregador["estado"] = novo_estado
    entregador["ultima_atualizacao"] = datetime.now().isoformat()

    salvar_dados({"entregadores": entregadores})

    return {
        "message": "Estado atualizado com sucesso!",
        "entregador_id": entregador_id,
        "novo_estado": novo_estado
    }

