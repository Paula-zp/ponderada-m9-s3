Feature: Gerenciamento do Estado do Entregador

  Scenario: Atualizar estado para "A Caminho do Pedido"
    Given que existe um entregador com ID 1 no estado "Disponível"
    When o estado é atualizado para "A Caminho do Pedido"
    Then o estado do entregador deve ser "A Caminho do Pedido"

  Scenario: Tentar atualizar com estado inválido
    Given que existe um entregador com ID 1 no estado "A Caminho do Pedido"
    When é tentado atualizar o estado para "Inexistente"
    Then a API deve retornar um erro 400 com a mensagem "Estado inválido"

  Scenario: Atualizar estado para "Pedido Entregue"
    Given que existe um entregador com ID 1 no estado "Entregando"
    When o estado é atualizado para "Pedido Entregue"
    Then o estado do entregador deve ser "Pedido Entregue"

  Scenario: Entregador inexistente
    Given que o entregador com ID 99 não existe
    When é tentado atualizar seu estado para "Disponível"
    Then a API deve retornar um erro 404 com a mensagem "Entregador não encontrado"
