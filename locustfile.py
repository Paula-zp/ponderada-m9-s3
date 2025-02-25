from locust import HttpUser, task, between

class EstadoEntregadorUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(0.1, 0.3)
    
    @task(2)
    def get_entregador(self):
        self.client.get("/entregadores/1")
    
    @task(1)
    def atualizar_estado(self):
        payload = {"novo_estado": "A Caminho do Pedido"}
        self.client.put("/entregadores/1/estado", json=payload)
