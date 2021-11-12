import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from ..utils.change_wait_time import change_wait_time


class Option(object):

    def __init__(self, element: WebElement):
        self.element = element
        self.driver = self.element.parent

    @property
    def text(self):
        return self.element.text

    @property
    def is_selected(self):
        return "selected" in self.element.get_attribute("class")

    def click(self):
        self.element.click()

    def select(self):
        if not self.is_selected:
            self.element.click()
            WebDriverWait(self.driver, 5).until(lambda x: self.is_selected)

    def do_not_select(self):
        if self.is_selected:
            self.element.click()
            WebDriverWait(self.driver, 5).until(lambda x: not self.is_selected)


class OptionsElement(object):
    """弹出的选项"""

    def __init__(self, xpath="//div[@role='presentation']"):
        self.xpath = xpath

    def __get__(self, instance, owner) -> List[Option]:
        driver = instance.driver
        option: WebElement = driver.find_elements(By.XPATH, self.xpath)[-1]
        with change_wait_time(driver):
            for i in range(5):
                options = option.find_elements_by_xpath(".//ul/li")
                if options:
                    return [Option(i) for i in options]
                time.sleep(1)


class _SelectedElement(object):

    def __init__(self, element: WebElement):
        self.element = element
        self.driver = self.element.parent

    def delete(self):
        self.element.find_element_by_xpath("./*[name()='svg']").click()

    @property
    def value(self):
        return self.element.find_element_by_xpath("./span").text


class SelectedElements(object):
    def __init__(self, *locator):
        if locator:
            self.locator = locator
        else:
            self.locator = (By.XPATH, ".//input/preceding-sibling::div/div")

    def __get__(self, instance, owner) -> List[_SelectedElement]:
        """instance应该是input元素上面的div，表示已经选中哪些选项"""
        element = instance.element
        elements = element.find_elements(*self.locator)
        return [_SelectedElement(i) for i in elements]
