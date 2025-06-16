from time import sleep

from helpers.button_text_changing import enter_and_click
from helpers.img_attribute_checking import get_third_img_alt

def test_text_changing(driver):
    driver.get("http://uitestingplayground.com/textinput")
    result = enter_and_click(driver, "ITCH")
    assert result == "ITCH", f"Ожидалось, что текст кнопки будет 'ITCH', а получили '{result}'"

def test_img_alt_checking(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    sleep(10)
    alt = get_third_img_alt(driver)
    # assert alt == "award", f"Ожидалось alt='award', а получили alt='{alt}'"
    assert alt == "award", f"Картинка не найдена или alt неправильный: {alt}"
