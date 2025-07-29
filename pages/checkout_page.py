from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # --- Localizadores ---
    CHECKOUT_BUTTON = (By.LINK_TEXT, "CHECKOUT")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    FINISH_BUTTON = (By.LINK_TEXT, "FINISH")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        self.clicar(self.CHECKOUT_BUTTON)

    def fill_customer_data(self, first_name, last_name, zip_code):
        self.escrever(self.FIRST_NAME_INPUT, first_name)
        self.escrever(self.LAST_NAME_INPUT, last_name)
        self.escrever(self.ZIP_CODE_INPUT, zip_code)

    def finish_purchase(self):
        self.clicar(self.CONTINUE_BUTTON)
        self.clicar(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.obter_texto(self.SUCCESS_MESSAGE)