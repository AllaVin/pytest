from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    sleep(7)
    driver.quit()

def test_itcareer_main_logo_exist(driver):
    driver.get("https://itcareerhub.de/ru")
    main_logo = driver.find_element(By.CLASS_NAME, "tn-atom__img")
    assert main_logo.is_displayed()

def test_itcareer_programms_exists(driver):
    driver.get("https://itcareerhub.de/ru")
    link_text = driver.find_element(By.XPATH, '//a[text()="Программы"]')
    assert "Программы" in link_text.text

def test_itcareer_payment(driver):
    driver.get("https://itcareerhub.de/ru")
    link_payment = driver.find_element(By.XPATH, '//a[text()="Способы оплаты"]')
    assert "Способы оплаты" in link_payment.text

def test_itcareer_news(driver):
    driver.get("https://itcareerhub.de/ru")
    link_news = driver.find_element(By.XPATH, '//a[text()="Новости"]')
    assert "Новости" in link_news.text

def test_itcareer_about(driver):
    driver.get("https://itcareerhub.de/ru")
    link_about = driver.find_element(By.XPATH, '//a[text()="О нас"]')
    assert "О нас" in link_about.text

def test_itcareer_feedback(driver):
    driver.get("https://itcareerhub.de/ru")
    link_feedback = driver.find_element(By.XPATH, '//a[text()="Отзывы"]')
    assert "Отзывы" in link_feedback.text


def test_itcareer_buttons(driver):
    driver.get("https://itcareerhub.de/ru")
    wait = WebDriverWait(driver, 10)
    button_ru = driver.find_element(By.XPATH, '//a[@href="/ru"]')
    button_de = driver.find_element(By.XPATH, '//a[@href="/ru"]')
    assert  button_ru.is_displayed()
    assert  button_de.is_displayed()



def test_itcareer_call_button(driver):
    driver.get("https://itcareerhub.de/ru")

    # Кликаем по иконке с трубкой
    phone_button = driver.find_element(By.CSS_SELECTOR, 'a[href="#popup:form-tr3"] img')
    phone_button.click()
    # Ожидание появления текста
    popup_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами")]'))
    )
    assert "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами" in popup_text.text