import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options

    browser.config.window_height = 2500
    browser.config.window_width = 1400

    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument("--headless")
    # browser.config.driver_options = driver_options

    browser.config.type_by_js = True

    yield

    browser.quit()
