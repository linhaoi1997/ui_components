import logging
from abc import abstractmethod, ABCMeta

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from ui_components.utils.change_wait_time import change_wait_time


class BaseInput(metaclass=ABCMeta):
    LABEL_LOCATOR = ".//label[span='{name}']|.//label[p='{name}']|.//input[@placeholder='{name}']"
    FOCUS_LOCATOR = ".."

    def __init__(self, name=None, num=None):
        self.name = name
        self.num = num
        self.base_finder: WebElement = None
        self._value = None
        self.driver = None

    def _match_input(self, element):
        with change_wait_time(element.parent):
            for i in element.find_elements_by_xpath("./div"):
                try:
                    if i.find_element_by_xpath(self.LABEL_LOCATOR.format(name=self.name)):
                        return i
                except NoSuchElementException as e:
                    pass
                except Exception as e:
                    logging.info(e)

    @property
    def element(self) -> WebElement:
        if self.name:
            return WebDriverWait(self.base_finder, 5).until(self._match_input, f"没找到名称为 '{self.name}' 的元素")
        if self.num:
            return WebDriverWait(self.base_finder, 5).until(lambda x: x.find_element_by_xpath(f"./div[{self.num}]"),
                                                            f"没找到第 '{self.num}' 个元素")
        raise AssertionError("没有传入 name 或者 num")

    def __get__(self, instance, owner):
        element: WebElement = instance.element
        self.base_finder = element
        self.driver = element.parent
        return self

    def __set__(self, instance, value):
        element: WebElement = instance.element
        self.driver = element.parent
        self.base_finder = element
        self.value = value

    @property
    def is_focus(self):
        """:return input是否被选中的状态"""
        return "focused" in self.element.find_element_by_xpath(self.FOCUS_LOCATOR).get_attribute("class")

    @property
    def hint(self):
        """:return =输入的提示"""
        return self.element.find_element_by_xpath(".//p").text

    @property
    @abstractmethod
    def value(self):
        """:return input已经输入的值"""
        return self._value

    @value.setter
    @abstractmethod
    def value(self, value):
        self._value = value

    @property
    def label(self):
        return self.element.find_element_by_xpath(".//label/span[last()]").text

    def fake(self):
        """为input随机填写值"""
        self.value = None

    @staticmethod
    def send_keys(element, value):
        element.click()
        element.clear()
        if element.get_attribute("value"):
            element.send_keys(Keys.ARROW_DOWN)
        while element.get_attribute("value"):
            element.send_keys(Keys.BACKSPACE)
        element.send_keys(value)
