from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_third_img_alt(driver):
    wait = WebDriverWait(driver, 50)
    # wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))
    driver.save_screenshot("debug_image_check.png")

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    if len(images) < 3:
        raise ValueError("На странице меньше трёх изображений")

    return images[2].get_attribute("alt")
