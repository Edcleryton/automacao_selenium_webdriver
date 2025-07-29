from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Classe base para todas as Pages Objects.
    Contém os métodos comuns de interação com a página.
    """
    def __init__(self, driver):
        self.driver = driver
        # Define um tempo de espera padrão de 10 segundos
        self.wait = WebDriverWait(self.driver, 10)

    def clicar(self, by_locator):
        """Clica em um elemento da página esperando ele ser clicável."""
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def escrever(self, by_locator, text):
        """Escreve um texto em um elemento esperando ele ser visível."""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def obter_texto(self, by_locator):
        """Obtém o texto de um elemento esperando ele ser visível."""
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def elemento_esta_visivel(self, by_locator):
        """Verifica se um elemento está visível na página."""
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False