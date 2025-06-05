import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()

def test_text_changing(driver):
    wait = WebDriverWait(driver, 20)  # Ожидание результата

    entry_field = driver.find_element(By.ID, "newButtonName")
    entry_field.send_keys("ITCH")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    assert entry_field, "ITCH"
    sleep(3)

