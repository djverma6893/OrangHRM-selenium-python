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


# pytest report
########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    # Safely add metadata for pytest-html if available
    if not hasattr(config, "_metadata") or config._metadata is None:
        config._metadata = {}
    config._metadata['Project Name'] = 'OrangeHRM Selenium'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Aman verma'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)