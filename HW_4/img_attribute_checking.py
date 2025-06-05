import pytest
from mako.testing.helpers import result_lines
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()

def test_img_alt_checking(driver):
    wait = WebDriverWait(driver, 50)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))
    sleep(10)

    # --- Находим все изображения в контейнере ---
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    third_img_alt = images[2].get_attribute("alt") # Картинка по индексу 2 (начало идет с нуля)
    assert third_img_alt == "award"