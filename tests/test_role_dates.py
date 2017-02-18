import browser
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from settings import URL_HOME
from utils import helpers


class TestReactPage(object):

    @classmethod
    def setup_class(cls):
        cls.driver = browser.start_driver()
        cls.contact_page = ContactPage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.driver.get(URL_HOME)
        cls.login_page.log_in()


    @classmethod
    def teardown_class(cls):
        browser.quit_driver()

    def test_job_role_default_dates(self):
        """Create job role with default contract dates

        Scenario:
            1. Create job contract
            2. Create job role, leave default contract dates
            3. Check job role dates are equal to job contract dates
        """
        role_name = "test role"
        contract_name = "test contract"
        set_start_date = helpers.generate_current_date()
        set_end_date = helpers.generate_half_year_date()
        self.contact_page.add_new_contract(contract_name, 1,
                                           set_start_date,
                                           set_end_date)
        start_date, end_date = self.contact_page.add_new_job_role(role_name,
                                                                  contract_name)
        assert set_start_date == start_date, "start date was wrongly prefilled," \
                                             " it should be {}," \
                                             " it is {}".format(set_start_date, start_date)
        assert set_end_date == end_date, "end date was wrongly prefilled," \
                                         " it should be {}," \
                                         " it is {}".format(set_end_date, end_date)
        role_start_date = self.contact_page.get_role_start_date(role_name)
        role_end_date = self.contact_page.get_role_end_date(role_name)
        assert set_start_date == role_start_date, "start date was wrongly prefilled," \
                                                  " it should be {}," \
                                                  " it is {}".format(set_start_date, role_start_date)
        assert set_end_date == role_end_date, "end date was wrongly prefilled," \
                                              " it should be {}," \
                                              " it is {}".format(set_end_date, role_end_date)
        self.contact_page.delete_job_role(role_name)
        self.contact_page.delete_job_contract(contract_name)

    def test_job_role_modified_dates(self):
        """Create job role with modified contract dates

        Scenario:
            1. Create job contract
            2. Create job role, change default contract dates
            3. Check job role dates are the same as they were specified
        """
        role_name = "test role 2"
        contract_name = "test contract 2"
        self.contact_page.add_new_contract(contract_name, 1,
                                           helpers.generate_current_date(),
                                           helpers.generate_half_year_date())
        set_start_date = helpers.generate_date_future_day()
        set_end_date = helpers.generate_date_future_month()
        start_date, end_date = self.contact_page.add_new_job_role(role_name,
                                                                  contract_name,
                                                                  start_date=set_start_date,
                                                                  end_date=set_end_date)
        assert set_start_date == start_date, "start date was wrongly prefilled," \
                                             " it should be {}," \
                                             " it is {}".format(set_start_date, start_date)
        assert set_end_date == end_date, "end date was wrongly prefilled," \
                                         " it should be {}," \
                                         " it is {}".format(set_end_date, end_date)
        role_start_date = self.contact_page.get_role_start_date(role_name)
        role_end_date = self.contact_page.get_role_end_date(role_name)
        assert set_start_date == role_start_date, "start date was wrongly prefilled," \
                                                  " it should be {}," \
                                                  " it is {}".format(set_start_date, role_start_date)
        assert set_end_date == role_end_date, "end date was wrongly prefilled," \
                                              " it should be {}," \
                                              " it is {}".format(set_end_date, role_end_date)
        self.contact_page.delete_job_role(role_name)
        self.contact_page.delete_job_contract(contract_name)
