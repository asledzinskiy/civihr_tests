from base_page import BasePage
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
        return self.driver.find_element_by_xpath("//*[@id='edit-submit']")

    def log_in(self, username=settings.USERNAME, password=settings.PASSWORD):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.login_button.click()
        import time
        time.sleep(3)
        self.username.send_keys(username)
        self.password.send_keys(password)
        time.sleep(3)
        self.login_button.click()
        time.sleep(3)
