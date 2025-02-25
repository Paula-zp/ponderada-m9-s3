# Gerenciamento do Estado do Entregador

## Descrição do Projeto
Este projeto implementa uma API com FastAPI que gerencia o estado dos entregadores utilizando dados mockados.

## Requisito Funcional
#### Atualização do Estado do Entregador
  - Permite atualizar o estado de um entregador.
  - Cenários testados:
    - Atualizar de "Disponível" para "A Caminho do Pedido".
    - Retornar erro 400 quando um estado inválido é enviado.
    - Atualizar de "Entregando" para "Pedido Entregue" (convertendo para "Disponível" internamente).
    - Retornar erro 404 para entregador inexistente.

## Requisito Não Funcional
#### Desempenho e Confiabilidade
  - A API deverá responder às operações de consulta e atualização em até 150ms em 95% das requisições, mesmo sob 50 requisições por segundo.
  - A taxa de erro deverá ser inferior a 0,5% para todas as operações.

## Testes e Resultados
#### Testes de Funcionalidade (Behave)
  Os cenários estão definidos no arquivo `tests/feature.feature` e implementados em `tests/steps/estado_entregador.py`, validando todos os cenários listados no requisito funcional. Os testes que não passarem ocorre erro devido ao mock.


#### Testes de Carga (Locust)
  O teste de carga foi implementado em `locustfile.py`.

Exemplo de execução:
    ```
        locust --headless --users 50 --spawn-rate 1 --run-time 50s
    ```

  **Resultados observados:**
  - Requisições GET: tempo médio, mediana e percentis mantidos baixos.
  - Requisições PUT: tempos médios entre ~194ms e ~268ms, sem falhas durante o teste com 5 usuários.

## Como Rodar
1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
2. Inicie o servidor:
   ```
   uvicorn app.main:app --reload
   ```
3. Execute os testes de funcionalidade:
   ```
   behave
   ```
4. Execute os testes de carga:
   ```
   locust --headless --users 50 --spawn-rate 1 --run-time 50s
   ```
