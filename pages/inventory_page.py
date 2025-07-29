from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # --- Localizadores ---
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PAGE_TITLE = (By.CLASS_NAME, "product_label")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, product_name):
        product_locator = (self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1].format(product_name=product_name))
        self.clicar(product_locator)

    def go_to_cart(self):
        self.clicar(self.CART_ICON)

    def is_inventory_title_visible(self):
        return self.elemento_esta_visivel(self.PAGE_TITLE)