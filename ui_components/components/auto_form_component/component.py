from typing import Type

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, url_changes, invisibility_of_element

from ui_components.components.form_components import FormComponent
from ui_components.utils.change_wait_time import change_wait_time
from .config_form import BaseDefinedForm
from ui_components.components.base_component import PageComponent
from ui_components.elements.template_elements import ButtonElement
from ui_components.components.auto_form_component.form_cases_class.base_form_case import BaseFormCase


class DefineFormComponent(PageComponent):
    DEFAULT_LOCATOR = "//div[contains(@class,'CustomFieldsContainer')]"
    FORM_LOCATOR = "//label[span='字段名称']/ancestor::div[label]/.."
    add_button = ButtonElement("新增字段")  # 新增字段
    save_button = ButtonElement("保存")  # 保存字段
    delete_button = ButtonElement("删除字段")
    confirm_button = ButtonElement("确定")

    _defined_form: BaseDefinedForm
    defined_form_type: Type[FormComponent]  # 返回表单类型会存在这里

    def setup(self):  # 初始化

        def wait_for_click(element):
            self.element.click()
            return element_to_be_clickable(element)

        WebDriverWait(self.driver, 10).until(wait_for_click(self.add_button), "新增字段按钮不可点击")

    def save(self):  # 点击保存按钮
        url = self.driver.current_url
        self.save_button.click()
        WebDriverWait(self.driver, 5).until(url_changes(url))

    @property
    def __all_fields_element(self):
        return self.element.find_elements(By.XPATH, "./div/div")

    def add_field(self):  # 点击新增按钮
        with change_wait_time(self.driver):
            self.setup()
            number = len(self.__all_fields_element)
            self.add_button.click()

            def field_num_changes(num):
                def _predicate(element):
                    return num != len(self.__all_fields_element)

                return _predicate

            WebDriverWait(self.driver, 5).until(field_num_changes(number))

    def set_form(self, form_case: BaseFormCase):  # 设置自定义表单
        self.delete_all_fields()
        setattr(self, "_defined_form", form_case.form("./div"))
        self.defined_form_type = form_case.form
        config = form_case.config
        for field in config:
            self.add_field()
            setattr(self, "config_form", field["config_form"](self.FORM_LOCATOR))
            config_form = getattr(self, "config_form")
            config_form.base_finder = self.element
            config_form.setup()
            setattr(config_form, "field_name", field["field_name"])
            for key, value in field["args"].items():
                setattr(config_form, key, value)

    @property
    def defined_form(self):  # 返回本表单
        form = self._defined_form
        form.base_finder = self.element
        return form

    def delete_all_fields(self):  # 删除自定义字段
        self.setup()
        with change_wait_time(self.driver):
            while self.__all_fields_element:
                element = self.__all_fields_element[-1]
                element.click()
                delete_button = self.delete_button
                delete_button.click()
                self.confirm_button.click()
                WebDriverWait(self.driver, 5).until(invisibility_of_element(delete_button))
