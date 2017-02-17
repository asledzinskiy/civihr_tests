import settings
from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ContactPage(BasePage):

    contact_url = settings.URL_HOME + "/civicrm/contact/" \
                                      "view?reset=1&cid={}#/".format(settings.USER_ID)

    def __init__(self, driver):
        super(ContactPage, self).__init__(driver)

    @property
    def job_contract(self):
        return self.driver.find_element_by_id("tab_hrjobcontract")

    @property
    def job_role(self):
        return self.driver.find_element_by_id("tab_hrjobroles")

    @property
    def add_contract(self):
        return self.driver.find_element_by_xpath("//*[@id='hrjob-contract']/div/p/button")

    @property
    def add_job_role(self):
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