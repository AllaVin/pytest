from logic.iframe_availability_checking import text_in_iframe



def test_iframe_text_present(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    result = text_in_iframe(driver)
    assert result, "❌ Текст не найден или не отображается в iframe"
