from logic.iframe_availability_logic import text_in_iframe
import pytest
from logic.dragdrop_logic import drag_and_drop_image

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_iframe_text_present(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    result = text_in_iframe(driver)
    assert result, "❌ Текст не найден или не отображается в iframe"


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_drag_and_drop_image(driver):
    result = drag_and_drop_image(driver)
    assert result, "❌ Резульат перетаскивания - неудача."
