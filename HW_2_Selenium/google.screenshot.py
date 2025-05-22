from time import sleep # for the delay and wait till the page is loaded fully
from selenium import webdriver
from selenium.webdriver.common.by import By # for finding elements by id / name / etc


driver = webdriver.Chrome()
driver.get("https://maple-permanent.wixsite.com/maple")
sleep(5)

# Searching the element by Name ---
gallery_link = driver.find_element(By.LINK_TEXT, "Галерея")

# --- Click on the found element ---
gallery_link.click()
sleep(5)
driver.fullscreen_window()
sleep(2)
# --- Вариант, когда файл сохраняется в текущую директорию без указания абсолютного пути ---
driver.save_screenshot("maple_gallery_1.png")
sleep(5)
contact_link = driver.find_element(By.LINK_TEXT, "Контакты")
contact_link.click()
sleep(5)
# --- Вариант, когда файл сохраняется в текущую директорию с указанием абсолютного пути ---
driver.save_screenshot("/Users/avinografff/pytest_project/HW/HW_2/maple_contacts_2.png")

# --- Вариант, когда файл сохраняется в другую указанную директорию ---
driver.back()
sleep(5)
driver.save_screenshot("/Users/avinografff/Downloads/maple_gallery_3.png")

driver.quit()