import time
import settings
from base_page import BasePage
from selenium.webdriver.support.ui import Select


class ContactPage(BasePage):

    contact_url = settings.URL_HOME + "/civicrm/contact/" \
                                      "view?reset=1&cid={}#/".format(settings.USER_ID)

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)

    @property
    def job_contract_tab(self):
        return self.driver.find_element_by_id("tab_hrjobcontract")

    @property
    def job_role_tab(self):
        return self.driver.find_element_by_id("tab_hrjobroles")

    @property
    def add_contract_button(self):
        return self.driver.find_element_by_xpath("//*[@id='hrjob-contract']/div/p/button")

    @property
    def add_job_role_button(self):
        return self.driver.find_element_by_xpath("//*[@id='hrjobroles']/div/button")

    @property
    def contract_position(self):
        return self.driver.find_element_by_id("hrjc-position")

    @property
    def contract_type(self):
        return Select(self.driver.find_element_by_id('hrjc-contract-type'))

    @property
    def contract_start_date(self):
        return self.driver.find_element_by_id("hrjc-period-start-date")

    @property
    def contract_end_date(self):
        return self.driver.find_element_by_id("hrjc-period-end-date")

    @property
    def contract_end_reason(self):
        return Select(self.driver.find_element_by_id('hrjc-end-reason'))

    @property
    def save_contract(self):
        return self.driver.find_element_by_xpath("//button[text()='Add New Job Contract']")

    @property
    def save_job_role(self):
        return self.driver.find_element_by_xpath("//*[@id='hrjobroles']/div/div[3]/"
                                                 "div/div/div[2]/div/div[2]/div/button[1]")

    @property
    def job_title(self):
        return self.driver.find_element_by_id("inputTitle")

    @property
    def job_role_contract(self):
        return Select(self.driver.find_element_by_id('newContractId'))

    @property
    def job_start_date(self):
        return self.driver.find_element_by_id("hrjobroles-newStartDate")

    @property
    def job_end_date(self):
        return self.driver.find_element_by_id("hrjobroles-newEndDate")

    def add_new_contract(self, position, contract_type, start_date, end_date=None):
        self.job_contract_tab.click()
        self.add_contract_button.click()
        time.sleep(3)
        self.contract_position.send_keys(position)
        self.contract_type.select_by_index(contract_type)
        self.contract_start_date.send_keys(start_date)
        if end_date:
            self.contract_end_date.send_keys(end_date)
            time.sleep(3)
            self.contract_end_reason.select_by_index(1)
            time.sleep(3)
        self.save_contract.click()
        time.sleep(3)

    def add_new_job_role(self, title, contract, start_date=None, end_date=None, modify=False):
        self.job_role_tab.click()
        self.add_job_role_button.click()
        time.sleep(3)
        self.job_title.send_keys(title)
        self.job_role_contract.select_by_index(contract)
        time.sleep(3)
        if modify:
            self.job_start_date.clear()
            self.job_start_date.send_keys(start_date)
            if end_date:
                self.job_end_date.clear()
                self.job_end_date.send_keys(end_date)
        start_date = self.get_start_date()
        end_date = self.get_end_date()
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.save_job_role)
        time.sleep(3)
        return start_date, end_date

    def get_start_date(self):
        return self.job_start_date.get_attribute('value')

    def get_end_date(self):
        return self.job_end_date.get_attribute('value')

    def get_role_start_date(self, role_name):
        el = self.driver.find_element_by_xpath("//div[@class='hrjobroles-basic-details']/"
                                               "div/div/div/div/p[text()='{}']/../../.."
                                               "/div[3]/div/p".format(role_name))
        return el.text

    def get_role_end_date(self, role_name):
        el = self.driver.find_element_by_xpath("//div[@class='hrjobroles-basic-details']/"
                                               "div/div/div/div/p[text()='{}']/../../.."
                                               "/div[4]/div/p".format(role_name))
        return el.text

    def delete_job_role(self, role_name):
        self.job_role_tab.click()
        time.sleep(3)
        el = self.driver.find_element_by_xpath(
            "//div/div/div/div/div/span[text()='{}']/"
            "../../../../../div[2]/div[2]/"
            "div/div[2]/div/button".format(role_name))
        self.driver.execute_script("arguments[0].click();", el)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Yes']").click()

    def delete_job_contract(self, contract_name):
        self.job_contract_tab.click()
        time.sleep(3)
        details_button = self.driver.find_element_by_xpath(
            "//li/div/div/div/div/div/div/p[text()='{}']/"
            "../../../../../../div[2]/"
            "div/div/a".format(contract_name))
        details_button.click()
        time.sleep(3)
        del_button = self.driver.find_element_by_xpath(
            "//li/div/div/div/div/div/div/p[text()='{}']/"
            "../../../../../../div[2]/div[2]/div/"
            "div[2]/div/button".format(contract_name))
        self.driver.execute_script("arguments[0].click();", del_button)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[text()='Yes']").click()