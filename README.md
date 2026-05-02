# Automação Selenium WebDriver — SauceDemo

![Python](https://img.shields.io/badge/python-%3E%3D3.9-blue)
![Selenium](https://img.shields.io/badge/selenium-%3E%3D4.25-green)
![pytest](https://img.shields.io/badge/tested%20with-pytest-orange)

Suíte de testes automatizados com **Selenium WebDriver** e **Page Object Model (POM)** cobrindo fluxos críticos do site de demonstração [SauceDemo](https://www.saucedemo.com/).

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como rodar os testes](#como-rodar-os-testes)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Cenários cobertos](#cenários-cobertos)
- [Arquitetura — Page Object Model](#arquitetura--page-object-model)

## Pré-requisitos

- Python 3.9+
- Google Chrome instalado
- pip

## Instalação

```bash
git clone https://github.com/Edcleryton/automacao_selenium_webdriver.git
cd automacao_selenium_webdriver
pip install selenium webdriver-manager pytest
```

> O ChromeDriver é baixado automaticamente via `webdriver-manager`, sem necessidade de instalação manual.

## Como rodar os testes

```bash
# Todos os testes (headless, sem abrir browser)
python -m pytest tests/ -v

# Com relatório HTML
python -m pytest tests/ -v --html=report.html
```

Os testes rodam em modo **headless** por padrão (sem interface gráfica).

## Estrutura do projeto

```
automacao_selenium_webdriver/
├── pages/
│   ├── base_page.py         # Classe base com métodos comuns de interação
│   ├── login_page.py        # Page Object da tela de login
│   ├── inventory_page.py    # Page Object da listagem de produtos
│   └── checkout_page.py     # Page Object do fluxo de checkout
├── tests/
│   ├── conftest.py          # Fixture do driver (Chrome headless)
│   └── test_flows.py        # Casos de teste end-to-end
├── features/                # Cenários BDD (Gherkin/Behave)
└── requirements.txt
```

## Cenários cobertos

| Teste | Descrição | Status |
|-------|-----------|--------|
| `test_successful_purchase_flow` | Fluxo completo: login → produto → carrinho → checkout → confirmação | ✅ |
| `test_locked_out_user_login` | Login com usuário bloqueado retorna mensagem de erro correta | ✅ |

**Resultado: 2/2 testes passando.**

## Arquitetura — Page Object Model

Cada página da aplicação é representada por uma classe Python que encapsula os seletores e ações disponíveis naquela tela. Os testes interagem apenas com os métodos das páginas, nunca diretamente com o Selenium.

```
LoginPage.load()                      → navega para https://www.saucedemo.com/
LoginPage.login(usuario, senha)       → preenche credenciais e clica em "Login"
InventoryPage.get_title()             → retorna o título da página de produtos
InventoryPage.add_backpack_to_cart()  → adiciona o Backpack ao carrinho
CheckoutPage.start_checkout()         → inicia o checkout
CheckoutPage.fill_personal_info(...)  → preenche dados pessoais e avança
CheckoutPage.finish_order()           → finaliza o pedido
CheckoutPage.get_completion_message() → retorna mensagem de conclusão
```

### Credenciais de teste (SauceDemo)

| Usuário | Senha | Situação |
|---------|-------|----------|
| `standard_user` | `secret_sauce` | Funcional |
| `locked_out_user` | `secret_sauce` | Bloqueado |

## Licença

MIT

## Autor

[Edcleryton Silva](https://github.com/Edcleryton)
