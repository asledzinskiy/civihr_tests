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

    def test_add_delete_todo(self):
        """Add todo

        Scenario:
            1. Create todo with name test1
            2. Check todo was created
            3. Check todo is present on active filter
            4. Check todo isn't present on completed filter
            5. Delete todo
            6. Check todo isn't present
        """
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
        assert self.example_page.check_todo_not_present("test1"),\
            "Element test1 present on completed tab"

    def test_complete_todo(self):
        """Complete todo

        Scenario:
            1. Create todo with name test2
            2. Mark test2 as completed
            3. Check test2 is present on completed filter
            4. Check test2 isn't present on active filter
            5. Delete todo
        """
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

    def test_edit_todo(self):
        """Edit todo

        Scenario:
            1. Create todo with name test3
            2. Change test3 name to test3_edited
            3. Check test3_edited was renamed
            5. Delete test3_edited
        """
        self.example_page.create_todo("test3")
        self.example_page.edit_todo("test3", "_edited")
        assert self.example_page.check_todo_present("test3_edited"),\
            "Element test3_edited not present on active tab"

        self.example_page.delete_todo_by_name("test3_edited")

    def test_clear_completed(self):
        """Clear all todos

        Scenario:
            1. Create todos with name test1, test2
            2. Select all todos
            3. Check test1, test2 isn't present on active filter
            4. Check test1, test2 is present on completed filter
            5. Click clear all button
            6. Check todos were removed
        """
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

    def test_count_items(self):
        """Count items

        Scenario:
            1. Create todo with name test1, test2, test3
            2. Check items equal to 3
            3. Complete on todo
            4. Check items equal to 2
            5. Make todo active again
            6. Check items equal to 3
            7. Delete one todo
            8. Check items equal to 2
            9. Complete all todos
            10. Check items equal to 0
            11. Make active todos
            12. Check items equal to 2
            13. Clear all todos
        """
        self.example_page.create_todo("test1")
        self.example_page.create_todo("test2")
        self.example_page.create_todo("test3")
        self.example_page.click_active_filter()
        assert self.example_page.get_item_count() == 3,\
            "number of items should be equal to 3"
        self.example_page.select_todo_by_name("test1")
        assert self.example_page.get_item_count() == 2,\
            "number of items should be equal to 2"
        self.example_page.click_completed_filter()
        self.example_page.select_todo_by_name("test1")
        assert self.example_page.get_item_count() == 3,\
            "number of items should be equal to 3"
        self.example_page.click_active_filter()
        self.example_page.delete_todo_by_name("test1")
        assert self.example_page.get_item_count() == 2,\
            "number of items should be equal to 2"
        self.example_page.click_select_all()
        assert self.example_page.get_item_count() == 0,\
            "number of items should be equal to 0"
        self.example_page.click_select_all()
        assert self.example_page.get_item_count() == 2,\
            "number of items should be equal to 2"
        self.example_page.click_select_all()
        self.example_page.click_clear_all()