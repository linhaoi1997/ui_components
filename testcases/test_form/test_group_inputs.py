import datetime

from ui_components.components.form_components.form_component import FormComponent
from ui_components.utils.get_driver import get_driver
from ui_components.components.form_components import TextGroupInput, SelectAndTextGroupInput, SelectAndDateInput \
    , CheckBoxGroupAndTextInput, MuiSelectAndTextGroupInput


class Form(FormComponent):
    inputs = TextGroupInput("输入框组")
    select_and_text = SelectAndTextGroupInput("下拉框+输入框")
    select_and_date = SelectAndDateInput("下拉框+日期")
    checkbox_and_date = CheckBoxGroupAndTextInput("复选框组+输入框")
    mui_select_and_text = MuiSelectAndTextGroupInput("多选下拉+输入框")

    def __get__(self, instance, owner):
        super(Form, self).__get__(instance, owner)
        return self


class Page():
    form = Form()

    def __init__(self, driver):
        self.driver = driver


class TestGroup:
    def setup_class(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def test1(self):
        form = self.page.form
        form.select_and_date = ["1", datetime.datetime.now()]
        print(form.select_and_date.value)

    def test2(self):
        form = self.page.form
        form.inputs = ["1", "2", "3"]
        print(form.inputs.value)

    def test3(self):
        form = self.page.form
        form.checkbox_and_date = [["1", "2"], "1"]
        print(form.checkbox_and_date.value)

    def test4(self):
        form = self.page.form
        form.mui_select_and_text = [["1", "2"], "1"]
        print(form.mui_select_and_text.value)
