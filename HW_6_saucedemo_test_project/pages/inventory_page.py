from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BUTTONS = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
    }
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self, product_names):
        for name in product_names:
            self.click(self.ADD_TO_CART_BUTTONS[name])

    def go_to_cart(self):
        self.click(self.CART_LINK)
