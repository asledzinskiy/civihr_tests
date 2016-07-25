from pages.example_page import ExamplePage


class TestReactPage(object):

    def __init__(self):
        self.example_page = ExamplePage(self.get_driver)


    def test_add_todo(self):
        self.example_page.create_todo("test1")
        assert self.example_page.check_todo_present("test1"),\
            "Element test1 wasn't added"