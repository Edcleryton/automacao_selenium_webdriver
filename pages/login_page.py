from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # --- Localizadores ---
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        # A URL agora é recebida como parâmetro
        self.driver.get(url)

    def execute_login(self, username, password):
        self.escrever(self.USERNAME_INPUT, username)
        self.escrever(self.PASSWORD_INPUT, password)
        self.clicar(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.obter_texto(self.ERROR_MESSAGE_CONTAINER)