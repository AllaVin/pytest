import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture
def driver():
    chrome_options = ChromeOptions()
    ## chrome_options.add_argument('--incognito') # Запускает браузер в режиме инкогнито (как при ручном открытии окна "новое приватное окно").
    ## chrome_options.add_argument('--headless') # Запускает браузер без графического интерфейса, то есть "в фоне", без открытия окна браузера на экране.
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
