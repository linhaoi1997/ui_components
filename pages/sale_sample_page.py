from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import  url_changes
from selenium.webdriver.support.wait import WebDriverWait

from ui_components.components.form_components import *
from .base_page import BasePage
from ui_components.elements.template_elements import ButtonElement
from contextlib import contextmanager


class SaleSamplePage(BasePage):
    url = "subapp/sale/sample"
    add_button = ButtonElement("新增样单")

    def add(self):
        self.add_button.click()
        new_page = CreateSaleSamplePage(self.driver)
        new_page.wait_for_jump()
        return new_page


class SaleForm(FormComponent):
    name = NativeSelectInput("客户名称")
    except_time = DateInput("期望交期")
    country = NativeSelectInput("地区")
    address = TextInput('详细地址')


class CreateSaleSamplePage(BasePage):
    url = "subapp/sale/sample/create"
    form = SaleForm()
    add_product_button = ButtonElement("添加")
    submit = ButtonElement("确认提交")

    def add_product(self):
        self.add_product_button.click()
        self.driver.find_element(By.XPATH, "//table//button[span='添加']").click()
        self.driver.find_element(By.XPATH, "//div[@role='presentation']//button/span/*[name()='svg']").click()
        self.driver.find_element(By.XPATH, "//input[@name='itemList.0.price']").send_keys(10)
        self.driver.find_element(By.XPATH, "//input[@name='itemList.0.orderNumber']").send_keys(10)

    @contextmanager
    def prepare_for_form(self):
        form = self.form
        form.name.fake()
        form.except_time.fake()
        form.country = "伊朗"
        form.address.fake()
        self.add_product()
        yield
        self.submit.click()
        WebDriverWait(self.driver, 5).until(url_changes(self.full_url))
        new_page = SaleSamplePage(self.driver)
        return new_page
