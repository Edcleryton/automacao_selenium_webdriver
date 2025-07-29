from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    A classe base para todas as Page Objects.
    Contém métodos comuns de interação com elementos da web.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        """Encontra e retorna um elemento, esperando até que ele esteja presente."""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator: tuple, timeout: int = 10):
        """Espera um elemento ser clicável e então clica nele."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(locator)).click()

    def _send_keys(self, locator: tuple, text: str, timeout: int = 10):
        """Encontra um elemento, limpa seu conteúdo e envia o texto."""
        element = self._find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator: tuple, timeout: int = 10) -> str:
        """Retorna o texto de um elemento."""
        return self._find_element(locator, timeout).text