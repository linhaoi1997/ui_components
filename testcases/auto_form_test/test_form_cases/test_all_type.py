import logging

import allure
import pytest

from testcases.auto_form_test.components import DefineFormComponent
from testcases.auto_form_test.form_cases_class import *
from ui_components.utils.get_driver import get_driver

cases = [
    TextCase,
    # DateCase, CheckboxCase, RadioCase, MuiSelectCase, NumberCase, SelectCase,
    # AllTypeCase,NumberRangeCase
]


class Page:
    define_form = DefineFormComponent()

    def __init__(self, driver):
        self.driver = driver


class TestPage:

    def setup_class(self):
        driver = get_driver()
        self.page = Page(driver)

    @allure.title("每种场景的自定义表单定义")
    @pytest.mark.parametrize("case_type", cases)
    def test1(self, case_type):
        define_form = self.page.define_form
        case = case_type()
        define_form.set_form(case)
        gen_form = define_form.defined_form
        for i in case.data:
            logging.info(getattr(gen_form, i).value)
