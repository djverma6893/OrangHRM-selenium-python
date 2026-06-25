import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def setup(browser):
    if browser == 'chrome':
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")  # Run Chrome in headless mode
        driver = webdriver.Chrome(service=service,options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        service = Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")