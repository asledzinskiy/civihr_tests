import pytest

import browser
from pages.example_page import ExamplePage
from settings import URL_HOME


class TestReactPage(object):

    @classmethod
    def setup_class(cls):
        cls.driver = browser.start_driver()
        cls.example_page = ExamplePage(cls.driver)
        cls.driver.get(URL_HOME)

    @classmethod
    def teardown_class(cls):
        browser.quit_driver()

    def test_add_todo(self):
        self.example_page.create_todo("test1")
        assert self.example_page.check_todo_present("test1"),\
            "Element test1 wasn't added"
        self.example_page.click_active_filter()
        assert self.example_page.check_todo_present("test1"),\
            "Element test1 not present on active tab"
        self.example_page.click_completed_filter()
        assert self.example_page.check_todo_not_present("test1"),\
            "Element test1 present on completed tab"
        self.example_page.click_all_filter()

        self.example_page.delete_todo_by_name("test1")

    def test_complete_todo(self):
        self.example_page.create_todo("test2")
        assert self.example_page.check_todo_present("test2"),\
            "Element test2 wasn't added"
        self.example_page.select_todo_by_name("test2")
        self.example_page.click_active_filter()
        assert self.example_page.check_todo_not_present("test2"),\
            "Element test2 present on active tab"
        self.example_page.click_completed_filter()
        assert self.example_page.check_todo_present("test2"),\
            "Element test2 not present on completed tab"
        self.example_page.click_all_filter()

        self.example_page.delete_todo_by_name("test2")

    def test_clear_completed(self):
        self.example_page.create_todo("test1")
        self.example_page.create_todo("test2")
        self.example_page.click_select_all()
        self.example_page.click_active_filter()
        assert self.example_page.check_todo_not_present("test1"),\
            "Element test1 present on active tab"
        assert self.example_page.check_todo_not_present("test2"),\
            "Element test2 present on active tab"
        self.example_page.click_completed_filter()
        assert self.example_page.check_todo_present("test1"),\
            "Element test1 not present on completed tab"
        assert self.example_page.check_todo_present("test2"),\
            "Element test2 not present on completed tab"
        self.example_page.click_clear_all()
        assert self.example_page.check_todo_not_present("test1"),\
            "Element test1 present on active tab"
        assert self.example_page.check_todo_not_present("test2"),\
            "Element test2 present on active tab"
    






