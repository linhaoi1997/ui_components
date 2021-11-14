from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_changes

from ui_components.components.auto_form_component.component import DefineFormComponent
from ui_components.elements.template_elements import ButtonElement
from .base_page import BasePage


class SaleFormDefinedPage(BasePage):
    url = "subapp/sale/setting/form/sample"

    define_form = DefineFormComponent()
    save_button = ButtonElement("保存")

    def save(self):
        self.save_button.click()
        # logging.info(self.wait_for_notification())
        # assert self.wait_for_notification() == "保存成功"
        WebDriverWait(self.driver, 5).until(url_changes(self.full_url))
