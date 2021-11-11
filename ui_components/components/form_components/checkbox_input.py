from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from .base_input import BaseInput
from .base_component import BaseComponent
from ...utils.raise_error import raise_assert_error


class Checkbox(object):
    name_locator = ".//label/p|./span[last()]"
    input_locator = ".//input"

    def __init__(self, element: WebElement):
        self.element = element
        self.driver = element.parent

    @property
    def is_selected(self):
        return "checked" in self.element.find_element_by_xpath("./span").get_attribute("class")

    @property
    def name(self):
        return self.element.find_element_by_xpath(self.name_locator).text

    def select(self):
        if not self.is_selected:
            self.element.find_element_by_xpath(self.input_locator).click()
            WebDriverWait(self.driver, 5).until(lambda x: self.is_selected)

    def do_not_select(self):
        if self.is_selected:
            self.element.find_element_by_xpath(self.input_locator).click()
            WebDriverWait(self.driver, 5).until(lambda x: not self.is_selected)

    @property
    def value(self):
        return self.is_selected

    @value.setter
    def value(self, value: bool):
        if value:
            self.select()
        else:
            self.do_not_select()


class CheckBoxGroupInput(BaseInput):
    box_group_locator = ".//div[contains(@class,'MuiFormGroup')]"
    box_locator = "./label"

    @property
    def check_boxs(self):
        return [Checkbox(i) for i in
                self.element.find_element_by_xpath(self.box_group_locator).find_elements_by_xpath(
                    self.box_locator)]

    @property
    def value(self):
        result = []
        input_eles = self.element.find_elements_by_xpath(".//input")
        for ele in input_eles:
            if ele.is_selected():
                result.append(ele.get_attribute("value"))
        return result

    @value.setter
    def value(self, values: list):
        [check_box.do_not_select() for check_box in self.check_boxs]
        for value in values:
            for check_box in self.check_boxs:
                if check_box.name == value:
                    check_box.value = True
                    break
            else:
                raise_assert_error(self.driver,
                                   f"没找到从check_boxs{[i.name for i in self.check_boxs]}中想要的下拉选项{values}")

        self._value = values
