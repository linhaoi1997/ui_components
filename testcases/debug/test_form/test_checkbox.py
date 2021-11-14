from ui_components.components.form_components.form_component import FormComponent
from ui_components.utils.get_driver import get_driver
from ui_components.components.form_components.checkbox_input import CheckBoxGroupInput


class Form(FormComponent):
    checkbox = CheckBoxGroupInput("复选框组")

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
    page.form.checkbox = ["1", "2", "3"]
    print(page.form.checkbox.value)
