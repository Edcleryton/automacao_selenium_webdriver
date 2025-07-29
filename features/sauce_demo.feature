# language: pt

Funcionalidade: Compra de produto no Sauce Demo
  Como um usuário autenticado, eu quero adicionar um produto ao carrinho
  e finalizar a compra com sucesso.

  Cenário: Realizar compra de um item com sucesso
    Dado que eu esteja autenticado no sistema
    Quando eu adiciono o produto "Sauce Labs Backpack" ao carrinho
    E eu acesso o carrinho de compras
    E eu prossigo para o checkout preenchendo os dados: nome "Fulano", sobrenome "Da Silva" e CEP "12345-678"
    Então eu devo ver a mensagem de "Thank you for your order!" na tela de conclusão