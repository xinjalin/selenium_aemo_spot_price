import pytest
from src.core.webdriver_manager import WebDriverManager

@pytest.fixture
def web_driver():
    web_driver_manager = WebDriverManager("https://example.com/")
    driver = web_driver_manager.get_driver()
    yield driver
    web_driver_manager.quit()


def test_with_fixture(web_driver):
    assert web_driver.current_url == "https://example.com/"
