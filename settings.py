import os

BROWSER = os.environ.get('BROWSER', 'firefox')

# download it here http://chromedriver.storage.googleapis.com/index.html
CHROME_EXECUTABLE_PATH = \
    os.environ.get('CHROME_EXECUTABLE_PATH', '/usr/bin/google-chrome')

URL_HOME = os.environ.get('URL_HOME', None)
USERNAME = os.environ.get('USERNAME', None)
PASSWORD = os.environ.get('PASSWORD', None)
USER_ID = os.environ.get('USER_ID', 374)

SELENIUM_IMPLICIT_WAIT = os.environ.get('SELENIUM_IMPLICIT_WAIT', 5)
