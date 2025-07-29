from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    """Page Object para o fluxo de checkout."""

    # --- Localizadores ---
    # Cart Page
    CHECKOUT_BUTTON = (By.ID, "checkout")
    # Checkout Step One
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    # Checkout Step Two
    FINISH_BUTTON = (By.ID, "finish")
    # Checkout Complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self._click(self.CHECKOUT_BUTTON)

    def fill_personal_info(self, first_name, last_name, postal_code):
        self._send_keys(self.FIRST_NAME_INPUT, first_name)
        self._send_keys(self.LAST_NAME_INPUT, last_name)
        self._send_keys(self.POSTAL_CODE_INPUT, postal_code)
        self._click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self._click(self.FINISH_BUTTON)

    def get_completion_message(self):
        return self._get_text(self.COMPLETE_HEADER)