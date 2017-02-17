from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import settings


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    @property
    def username(self):
        return self.driver.find_element_by_id("edit-name")

    @property
    def password(self):
        return self.driver.find_element_by_id("edit-pass")

    @property
    def login_button(self):
        return self.driver.find_element_by_id("edit-submit")

    def log_in(self, username=settings.USERNAME, password=settings.PASSWORD):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
