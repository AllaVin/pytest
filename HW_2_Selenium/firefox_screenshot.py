from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


try:
    # Открытие страницы
    driver.get("https://maple-permanent.wixsite.com/maple")
    # Задержка для загрузки страницы
    sleep(3)
    # Поиск ссылки "Галерея" и клик
    gallery_link = driver.find_element(By.LINK_TEXT, "Галерея")
    gallery_link.click()
    # Задержка для проверки перехода
    sleep(3)
    driver.fullscreen_window()
    sleep(2)
    # --- Вариант, когда файл сохраняется в текущую директорию без указания абсолютного пути ---
    driver.save_screenshot("firefox_gallery_1.png")
    sleep(3)
    contact_link = driver.find_element(By.LINK_TEXT, "Контакты")
    contact_link.click()
    sleep(3)
    # --- Вариант, когда файл сохраняется в текущую директорию с указанием абсолютного пути ---
    driver.save_screenshot("/Users/avinografff/pytest_project/HW/HW_2/firefox_contacts_2.png")

    # --- Вариант, когда файл сохраняется в другую указанную директорию ---
    driver.back()
    sleep(5)
    driver.save_screenshot("/Users/avinografff/Downloads/firefox_gallery_3.png")

finally:
    # Закрытие браузера
    driver.quit()