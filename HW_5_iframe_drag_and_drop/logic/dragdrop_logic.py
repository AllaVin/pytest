from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def drag_and_drop_image(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(driver, 10)

    # Закрытие куки-баннера
    try:
        consent_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.fc-button.fc-cta-consent"))
        )
        consent_button.click()
    except TimeoutException:
        print("Баннер не найден")

    # iframe с демо
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(iframe)

    # ждем хотя бы одного изображения
    gallery_images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery > li")))
    source = gallery_images[0]
    trash = driver.find_element(By.ID, "trash")

    # перетаскиваем
    ActionChains(driver).drag_and_drop(source, trash).perform()

    # проверяем
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash > ul > li")))
    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash > ul > li")
    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery > li")

    assert len(trash_items) == 1, "В корзине должно быть 1 изображение"
    assert len(gallery_items) == 3, "В галерее должно остаться 3 изображения"
    return True
