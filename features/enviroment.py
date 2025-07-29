import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Adiciona a pasta raiz do projeto ao path do Python para resolver imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

def before_all(context):
    """Carrega as variáveis de ambiente do arquivo .env."""
    load_dotenv()
    context.config.base_url = os.getenv("BASE_URL")
    context.config.standard_user = os.getenv("STANDARD_USER")
    context.config.locked_out_user = os.getenv("LOCKED_OUT_USER")
    context.config.password = os.getenv("PASSWORD")

def before_scenario(context, scenario):
    """Inicia o navegador ANTES de cada cenário e o guarda no contexto."""
    service = ChromeService(executable_path=ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()

def after_scenario(context, scenario):
    """Fecha o navegador APÓS cada cenário."""
    context.driver.quit()