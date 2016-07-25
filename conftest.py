import pytest
import browser


@pytest.fixture(scope='class', autouse=True)
def get_driver(request):
    """Fixture to start browser
    """
    driver = browser.start_driver()
    return driver

@pytest.fixture(scope='function', autouse=True)
def close_driver(request):
    """Fixture to close browser
    """
    def close_driver():
        browser.quit_driver()
    request.addfinalizer(close_driver)
