from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

@given('que eu esteja autenticado no sistema')
def step_impl(context):
    login_page = LoginPage(context.driver)
    # Usa as variáveis carregadas do .env pelo environment.py
    base_url = context.config.base_url
    username = context.config.standard_user
    password = context.config.password

    login_page.open(base_url)
    login_page.execute_login(username, password)

@when('eu adiciono o produto "{product_name}" ao carrinho')
def step_impl(context, product_name):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.add_product_to_cart(product_name)

@when('eu acesso o carrinho de compras')
def step_impl(context):
    context.inventory_page.go_to_cart()

@when('eu prossigo para o checkout preenchendo os dados: nome "{first_name}", sobrenome "{last_name}" e CEP "{zip_code}"')
def step_impl(context, first_name, last_name, zip_code):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.proceed_to_checkout()
    context.checkout_page.fill_customer_data(first_name, last_name, zip_code)
    context.checkout_page.finish_purchase()

@then('eu devo ver a mensagem de "{message}" na tela de conclusão')
def step_impl(context, message):
    success_message = context.checkout_page.get_success_message()
    assert message == success_message, f"Mensagem esperada era '{message}', mas o sistema exibiu '{success_message}'"