from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class ExamplePage(BasePage):

    def __init__(self):
        super(ExamplePage, self).__init__()

    @property
    def todo_input(self):
        return self.driver.find_element_by_css_selector("input.new-todo")

    @property
    def get_todo_by_name(self, name):
        return self.driver.find_element_by_xpath(
            "//div[@class='view']/label[.='{}']".format(name))

    @property
    def get_select_todo_by_name(self, name):
        return self.driver.find_element_by_xpath(
            "//div[@class='view']/label[.='{}']/../input[@class='toggle']".format(name))

    @property
    def get_delete_todo_by_name(self, name):
        return self.driver.find_element_by_xpath(
            "//div[@class='view']/label[.='{}']/../button[@class='destroy']".format(name))

    @property
    def get_all_filter(self):
        return self.driver.find_element_by_xpath(
            "//ul[@class='filters']/li/a[text()='All']")

    @property
    def get_active_filter(self):
        return self.driver.find_element_by_xpath(
            "//ul[@class='filters']/li/a[text()='Active']")

    @property
    def get_completed_filter(self):
        return self.driver.find_element_by_xpath(
            "//ul[@class='filters']/li/a[text()='Completed']")

    def create_todo(self, name):
        self.todo_input.send_keys(name)
        self.todo_input.submit()

    def select_todo_by_name(self):
        self.get_select_todo_by_name.click()

    def delete_todo_by_name(self):
        self.get_delete_todo_by_name.click()

    def click_all_filter(self):
        self.get_all_filter.click()

    def click_active_filter(self):
        self.get_active_filter.click()

    def click_completed_filter(self):
        self.get_completed_filter.click()

    def check_todo_not_present(self, name):
        try:
            self.get_todo_by_name(name)
            return False
        except NoSuchElementException:
            return True

    def check_todo_present(self, name):
        try:
            self.get_todo_by_name(name)
            return True
        except NoSuchElementException:
            return False