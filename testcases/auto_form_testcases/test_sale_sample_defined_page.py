import logging

import allure
import pytest

from pages.sale_sample_page import SaleSamplePage
from pages.sale_form_page import SaleFormDefinedPage
from testcases.auto_form_test.form_cases_class import *
from selenium import webdriver

from ui_components.utils.get_driver import get_driver

cases = [TextCase, DateCase, CheckboxCase, RadioCase, MuiSelectCase, NumberCase,
         SelectCase,
         # AllTypeCase,NumberRangeCase
         ]


class Test:

    def setup_class(self):
        driver = get_driver()
        # driver = webdriver.Chrome()
        self.page = SaleSamplePage(driver)
        self.defined_page = SaleFormDefinedPage(driver)

    @pytest.mark.parametrize("case_type", cases)
    def test1(self, case_type):
        with allure.step("定义表单"):
            defined_page = self.defined_page
            defined_page.jump()
            define_form = defined_page.define_form
            case = case_type()
            define_form.set_form(case)
            gen_form = define_form.defined_form
            for i in case.data:
                logging.info(getattr(gen_form, i).value)  # 打印出来说明左面的页面成功添加了
            defined_page.save()

        with allure.step("新建表单"):
            page = self.page
            page.jump()
            create_page = page.add()
            with create_page.prepare_for_form():
                define_form_type = case.form
                setattr(create_page, "define_form", define_form_type(base_finder=create_page.driver))
                real_form = create_page.define_form
                for key, value in case.data.items():
                    setattr(real_form, key, value)

        with allure.step("校验填写"):
            update_page = page.edit_new_sale()
            setattr(update_page, "define_form", define_form_type(base_finder=update_page.driver))
            real_form = create_page.define_form
            for key, value in case.data.items():
                logging.info(f"校验 {key} 的值等于value")
                assert getattr(real_form, key).value == value
