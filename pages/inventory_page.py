from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # --- Localizadores ---
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, product_name):
        product_locator = (self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1].format(product_name=product_name))
        self.clicar(product_locator)

    def add_backpack_to_cart(self):
        self.clicar(self.ADD_BACKPACK_BTN)

    def get_cart_items_count(self):
        return self.obter_texto(self.CART_BADGE)

    def get_title(self):
        return self.obter_texto(self.PAGE_TITLE)

    def go_to_cart(self):
        self.clicar(self.CART_ICON)

    def is_inventory_title_visible(self):
        return self.elemento_esta_visivel(self.PAGE_TITLE)