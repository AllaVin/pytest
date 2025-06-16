from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def enter_and_click(driver, input_text):
    wait = WebDriverWait(driver, 20)

    entry_field = driver.find_element(By.ID, "newButtonName")
    entry_field.clear()
    entry_field.send_keys(input_text)

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), input_text))
    return button.text
