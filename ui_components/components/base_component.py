from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseComponent(object):
    base_finder_attr = "element"
    DEFAULT_LOCATOR = ""

    def __init__(self, locator=None):
        if isinstance(locator, list):
            self.locator = locator
        elif locator is None:
            self.locator = [By.XPATH, self.DEFAULT_LOCATOR]
        else:
            self.locator = [By.XPATH, locator]
        self.base_finder = None
        self.driver = None

    @property
    def element(self):
        return self.base_finder.find_element(*self.locator)

    @property
    def elements(self):
        return self.base_finder.find_element(*self.locator)

    def __get__(self, instance, owner):
        element: WebElement = getattr(instance, self.base_finder_attr)
        self.base_finder = element
        self.driver = element.parent
        return self


class PageComponent(BaseComponent):
    base_finder_attr = "driver"

    def __get__(self, instance, owner):
        driver: WebDriver = getattr(instance, self.base_finder_attr)
        self.base_finder = driver
        self.driver = driver
        return self
