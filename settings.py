import os

BROWSER = os.environ.get('BROWSER', 'firefox')

# download it here http://chromedriver.storage.googleapis.com/index.html
CHROME_EXECUTABLE_PATH = \
    os.environ.get('CHROME_EXECUTABLE_PATH', '/usr/bin/google-chrome')

URL_HOME = os.environ.get('URL_HOME', 'http://localhost:8000/')

SELENIUM_IMPLICIT_WAIT = os.environ.get('SELENIUM_IMPLICIT_WAIT', 10)
