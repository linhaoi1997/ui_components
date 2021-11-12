from ui_components.components.form_components.form_component import FormComponent
from ui_components.utils.get_driver import get_driver
from ui_components.components.form_components import DateInput
import datetime


class Form(FormComponent):
    date = DateInput("日期")

    def __get__(self, instance, owner):
        super(Form, self).__get__(instance, owner)
        return self


class Page():
    form = Form()

    def __init__(self, driver):
        self.driver = driver


def test():
    driver = get_driver()
    page = Page(driver)
    page.form.date = datetime.datetime.now()
    print(page.form.date.value)
