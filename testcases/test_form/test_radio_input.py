from ui_components.components.form_components.form_component import FormComponent
from ui_components.utils.get_driver import get_driver
from ui_components.components.form_components import RadioGroupInput


class Form(FormComponent):
    radio = RadioGroupInput("通知生产条件")

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
    page.form.radio = "关联收款金额"
    print(page.form.radio.value)
