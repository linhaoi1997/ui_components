from ui_components.components.form_components.form_component import FormComponent
from ui_components.utils.get_driver import get_driver
from ui_components.components.form_components import TextInput, NumberInput


class Form(FormComponent):
    DEFAULT_LOCATOR = "//div[@class='MuiDialogContent-root']//div[contains(@class,'MuiPaper-root')]/div/div/div"

    address = TextInput("详细地址")
    number_field = NumberInput("数字字段")
    field = NumberInput("新增字段")

    def __get__(self, instance, owner):
        super(Form, self).__get__(instance, owner)
        return self


class Page:
    form = Form()

    def __init__(self, driver):
        self.driver = driver


def test():
    driver = get_driver()
    page = Page(driver)
    page.form.address = "测试地址"
    print(page.form.address.value)


def test2():
    driver = get_driver()
    page = Page(driver)
    page.form.field = 11
    print(page.form.field.value)
