import requests
from behave import given, when, then

BASE_URL = "http://localhost:8000"

# 1. Atualizar para "A Caminho do Pedido"
@given('que existe um entregador com ID {entregador_id} no estado "Disponível"')
def step_given_entregador_disponivel(context, entregador_id):
    response = requests.get(f"{BASE_URL}/entregadores/{entregador_id}")
    assert response.status_code == 200, f"Erro ao buscar entregador: {response.json()}"
    entregador = response.json()
    assert entregador["estado"] == "Disponível", f"Estado inicial incorreto: {entregador['estado']}"
    context.entregador_id = entregador_id

@when('o estado é atualizado para "A Caminho do Pedido"')
def step_when_atualizar_estado_caminho_pedido(context):
    payload = {"novo_estado": "A Caminho do Pedido"}
    context.response = requests.put(f"{BASE_URL}/entregadores/{context.entregador_id}/estado", json=payload)

@then('o estado do entregador deve ser "A Caminho do Pedido"')
def step_then_verificar_estado_caminho_pedido(context):
    entregador_id = context.entregador_id
    response = requests.get(f"{BASE_URL}/entregadores/{entregador_id}")
    assert response.status_code == 200
    estado_atual = response.json()["estado"]
    assert estado_atual == "A Caminho do Pedido", f"Esperado: A Caminho do Pedido, Obtido: {estado_atual}"

# 2. Estado inválido
@given('que existe um entregador com ID {entregador_id} no estado "A Caminho do Pedido"')
def step_given_entregador_caminho_pedido(context, entregador_id):
    response = requests.get(f"{BASE_URL}/entregadores/{entregador_id}")
    assert response.status_code == 200, f"Erro ao buscar entregador: {response.json()}"
    entregador = response.json()
    assert entregador["estado"] == "A Caminho do Pedido", f"Estado inicial incorreto: {entregador['estado']}"
    context.entregador_id = entregador_id

@when('é tentado atualizar o estado para "Inexistente"')
def step_when_estado_invalido(context):
    payload = {"novo_estado": "Inexistente"}
    context.response = requests.put(f"{BASE_URL}/entregadores/{context.entregador_id}/estado", json=payload)

@then('a API deve retornar um erro 400 com a mensagem "Estado inválido"')
def step_then_erro_estado_invalido(context):
    assert context.response.status_code == 400
    resposta_json = context.response.json()
    assert "Estado inválido" in resposta_json["detail"], f"Esperado: Estado inválido, Obtido: {resposta_json}"

# 3. Atualizar estado para "Pedido Entregue"
@given('que existe um entregador com ID {entregador_id} no estado "Entregando"')
def step_given_entregador_entregando(context, entregador_id):
    response = requests.get(f"{BASE_URL}/entregadores/{entregador_id}")
    assert response.status_code == 200, f"Erro ao buscar entregador: {response.json()}"
    entregador = response.json()
    assert entregador["estado"] == "Entregando", f"Estado inicial incorreto: {entregador['estado']}"
    context.entregador_id = entregador_id

@when('o estado é atualizado para "Pedido Entregue"')
def step_when_atualizar_estado_pedido_entregue(context):
    payload = {"novo_estado": "Pedido Entregue"}
    context.response = requests.put(f"{BASE_URL}/entregadores/{context.entregador_id}/estado", json=payload)

@then('o estado do entregador deve ser "Pedido Entregue"')
def step_then_verificar_estado_pedido_entregue(context):
    entregador_id = context.entregador_id
    response = requests.get(f"{BASE_URL}/entregadores/{entregador_id}")
    assert response.status_code == 200
    estado_atual = response.json()["estado"]
    assert estado_atual == "Pedido Entregue", f"Esperado: Pedido Entregue, Obtido: {estado_atual}"

# 4. Entregador inexistente
@given('que o entregador com ID {entregador_id} não existe')
def step_given_entregador_inexistente(context, entregador_id):
    context.entregador_id = entregador_id

@when('é tentado atualizar seu estado para "Disponível"')
def step_when_atualizar_estado_inexistente(context):
    payload = {"novo_estado": "Disponível"}
    context.response = requests.put(f"{BASE_URL}/entregadores/{context.entregador_id}/estado", json=payload)

@then('a API deve retornar um erro 404 com a mensagem "Entregador não encontrado"')
def step_then_erro_entregador_inexistente(context):
    assert context.response.status_code == 404
    resposta_json = context.response.json()
    assert "Entregador não encontrado" in resposta_json["detail"], f"Esperado: Entregador não encontrado, Obtido: {resposta_json}"
