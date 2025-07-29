from behave import when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@when('eu tento fazer login com o usuário "{user_type}"')
def step_impl(context, user_type):
    context.login_page = LoginPage(context.driver)

    # Pega o nome de usuário do contexto, que foi carregado do .env
    username = getattr(context.config, user_type)
    password = context.config.password

    context.login_page.open(context.config.base_url)
    context.login_page.execute_login(username, password)

@then('eu devo ver o resultado "{result}"')
def step_impl(context, result):
    if result == "sucesso":
        inventory_page = InventoryPage(context.driver)
        assert inventory_page.is_inventory_title_visible(), "Login falhou, não fui para a página de inventário."
    elif result == "falha":
        error_message = "Epic sadface: Sorry, this user has been locked out."
        assert error_message in context.login_page.get_error_message(), "Mensagem de erro para usuário bloqueado não apareceu." 
    
            