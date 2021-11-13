from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_matches
import os


class BasePage(object):
    base_url = os.getenv("WEB_BASE_URL", "https://mc-test.teletraan.io/")
    url = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def jump(self):
        self.driver.get(self.full_url)
        WebDriverWait(self.driver, 5).until(url_matches(self.url))

    @property
    def full_url(self):
        return self.base_url + self.url

    @property
    def is_in_page(self):
        return url_matches(self.url)(self.driver)

    def wait_for_notification(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//div[@class='MuiAlert-message']")
        )
        return element.text
