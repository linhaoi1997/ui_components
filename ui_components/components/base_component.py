from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions


class OriginElement(object):

    def __get__(self, instance, owner):
        driver = instance.driver
        locator = instance.locator
        return WebDriverWait(driver, 20).until(
            lambda d: driver.find_elements(*locator)
        )


class BaseComponent(object):
    DEFAULT_LOCATOR = ""

    def __init__(self, *locator):
        if not locator:
            self.locator = (By.XPATH, self.DEFAULT_LOCATOR)
        else:
            self.locator = locator

    def refresh(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(self.element))
        self._handle()

    def _handle(self):
        self.elements: List[WebElement] = WebDriverWait(self.driver, 5).until(lambda x: x.find_elements(*self.locator))
        self.element: WebElement = self.elements[0]

    def __get__(self, instance, owner):
        self.driver = instance.driver
        self._handle()
        return self
