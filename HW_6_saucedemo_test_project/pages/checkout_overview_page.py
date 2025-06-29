from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutOverviewPage(BasePage):
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def get_total(self):
        return self.get_text(self.TOTAL)
