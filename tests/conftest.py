import pydantic_settings
import pytest
from selene import browser
from selenium import webdriver


class Settings(pydantic_settings.BaseSettings):
    base_url: str = 'https://demoqa.com'
    window_width: str = '1900'
    window_height: str = '950'
    headless: bool = False


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    config = Settings()
    browser.config.base_url = config.base_url
    if config.headless:
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--headless')
        browser.config.driver_options = driver_options
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height

    yield

    browser.quit()