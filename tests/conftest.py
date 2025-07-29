import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Esta fixture inicializa e finaliza o WebDriver para cada teste.
    O Selenium Manager cuidará do download do chromedriver automaticamente.
    
    É definida em conftest.py para estar disponível para todos os testes.
    """
    # Inicializa o WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Aumentar um pouco a espera implícita é uma boa prática
    
    # Disponibiliza o driver para o teste
    yield driver
    
    # Finaliza o WebDriver após o teste
    driver.quit()