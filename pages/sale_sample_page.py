from ui_components.components.form_components import *
from .base_page import BasePage
from ui_components.elements.template_elements import ButtonElement


class SaleSamplePage(BasePage):
    url = "subapp/sale/sample"
    add_button = ButtonElement("新增样单")

    def add(self):
        self.add_button.click()
        new_page = CreateSaleSamplePage(self.driver)
        new_page.jump()
        return new_page


class SaleForm(FormComponent):
    pass


class CreateSaleSamplePage(BasePage):
    url = "subapp/sale/sample/create"
