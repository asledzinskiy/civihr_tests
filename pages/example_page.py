from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class ExamplePage(BasePage):

    def __init__(self, driver):
        super(ExamplePage, self).__init__(driver)

    @property
    def todo_input(self):
        return self.driver.find_element_by_css_selector("input.new-todo")

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

    @property
    def get_select_all(self):
        return self.driver.find_element_by_xpath(
            "//input[@class='toggle-all']")

    @property
    def get_clear_all(self):
        return self.driver.find_element_by_xpath(
            "//button[@class='clear-completed']")

    @property
    def get_edit_element(self):
        return self.driver.find_element_by_xpath(
            "//input[@class='edit']")

    def get_item_count(self):
        return int(self.driver.find_element_by_xpath(
            "//span[@class='todo-count']/strong").text)

    def get_todo_by_name(self, name):
        return self.driver.find_element_by_xpath(
            "//div[@class='view']/label[.='{}']".format(name))

    def get_select_todo_by_name(self, name):
        return self.driver.find_element_by_xpath(
            "//div[@class='view']/label[.='{}']/../input[@class='toggle']".format(name))

    def get_delete_todo_by_name(self, name):
        return self.driver.find_element_by_xpath(
            "//div[@class='view']/label[.='{}']/../button[@class='destroy']".format(name))

    def create_todo(self, name):
        self.todo_input.send_keys(name)
        self.todo_input.send_keys(Keys.RETURN)

    def select_todo_by_name(self, name):
        self.get_select_todo_by_name(name).click()

    def delete_todo_by_name(self, name):
        button = self.get_delete_todo_by_name(name)
        self.driver.execute_script("arguments[0].click();", button)

    def edit_todo(self, name, newname):
        todo_element = self.get_todo_by_name(name)
        actions = ActionChains(self.driver)
        actions.move_to_element(todo_element).double_click(todo_element).perform()
        self.get_edit_element.send_keys(newname)
        self.get_edit_element.send_keys(Keys.RETURN)

    def click_all_filter(self):
        self.get_all_filter.click()

    def click_active_filter(self):
        self.get_active_filter.click()

    def click_completed_filter(self):
        self.get_completed_filter.click()

    def click_select_all(self):
        self.get_select_all.click()

    def click_clear_all(self):
        self.get_clear_all.click()

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