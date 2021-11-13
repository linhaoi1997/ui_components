import logging

from testcases.auto_form_test.components import DefineFormComponent
from testcases.auto_form_test.form_cases_class.number_range_case import MinMaxCase
from ui_components.utils.get_driver import get_driver


class Page:
    define_form = DefineFormComponent()

    def __init__(self, driver):
        self.driver = driver


class TestPage:

    def setup_class(self):
        driver = get_driver()
        self.page = Page(driver)

    def test1(self):
        define_form = self.page.define_form
        define_form.delete_all_fields()
        case = MinMaxCase()
        define_form.set_form(case)
        gen_form = define_form.defined_form
        for i in case.data:
            logging.info(getattr(gen_form, i).value)
