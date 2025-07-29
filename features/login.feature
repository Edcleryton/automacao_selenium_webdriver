# language: pt

Funcionalidade: Autenticação de Usuário
  Para garantir a segurança do sistema, apenas usuários válidos devem conseguir acessar
  e usuários bloqueados devem receber uma mensagem de erro.

  Esquema do Cenário: Tentativa de login com diferentes usuários
    Quando eu tento fazer login com o usuário "<usuario>"
    Então eu devo ver o resultado "<resultado>"

    Exemplos:
      | usuario         | resultado   |
      | standard_user   | sucesso     |
      | locked_out_user | falha       |