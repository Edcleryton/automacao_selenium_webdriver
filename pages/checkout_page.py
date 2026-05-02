from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # --- Localizadores ---
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        self.clicar(self.CHECKOUT_BUTTON)

    def start_checkout(self):
        self.proceed_to_checkout()

    def fill_customer_data(self, first_name, last_name, zip_code):
        self.escrever(self.FIRST_NAME_INPUT, first_name)
        self.escrever(self.LAST_NAME_INPUT, last_name)
        self.escrever(self.ZIP_CODE_INPUT, zip_code)

    def fill_personal_info(self, first_name, last_name, zip_code):
        self.fill_customer_data(first_name, last_name, zip_code)
        self.clicar(self.CONTINUE_BUTTON)

    def finish_purchase(self):
        self.clicar(self.FINISH_BUTTON)

    def finish_order(self):
        self.finish_purchase()

    def get_success_message(self):
        return self.obter_texto(self.SUCCESS_MESSAGE)

    def get_completion_message(self):
        return self.get_success_message()