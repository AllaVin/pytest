# Задание 1: Проверка наличия текста в iframe
# Открыть страницу
# Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
# Проверить наличие текста
# Найти фрейм (iframe), в котором содержится искомый текст.
# Переключиться в этот iframe.
# Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
# Убедиться, что текст отображается на странице.



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def text_in_iframe(driver):
    wait = WebDriverWait(driver, 10)

    # переключаемся в iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))
    # ожидаем загрузки все параграфов
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    paragraphs = driver.find_elements(By.TAG_NAME, "p")

    # перебираем каждый параграф
    target_text = 'semper posuere integer et senectus justo curabitur'
    found = False # Изначально результату нашего поиска присваиваем False
    for p in paragraphs: # Теперь перебираем по всем параграфам ('p' - здесь временное название каждого из параграфов)
        if target_text in p.text:
            found = True
            # assert p.is_displayed(), "Параграф найден, но не отображается"
            break
    assert found, f"Текст '{target_text}' не найден ни в одном параграфе"
    return True



