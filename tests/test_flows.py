import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_successful_purchase_flow(driver):
    """
    Testa o fluxo completo de uma compra bem-sucedida usando Page Objects.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Acessar e fazer login
    login_page.load().login("standard_user", "secret_sauce")
    
    # Verificar se o login foi bem-sucedido e estamos na página de produtos
    assert inventory_page.get_title() == "Products"

    # 2. Adicionar item ao carrinho e verificar
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_items_count() == "1"

    # 3. Navegar para o carrinho e iniciar o checkout
    inventory_page.go_to_cart()
    checkout_page.start_checkout()

    # 4. Preencher informações e finalizar
    checkout_page.fill_personal_info("Test", "User", "12345")
    checkout_page.finish_order()

    # 5. Verificar a mensagem de sucesso
    assert checkout_page.get_completion_message() == "Thank you for your order!"

def test_locked_out_user_login(driver):
    """Testa a tentativa de login com um usuário bloqueado."""
    login_page = LoginPage(driver)
    login_page.load().login("locked_out_user", "secret_sauce")

    # Verificar a mensagem de erro
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert expected_error in login_page.get_error_message()