from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_matches
from config import BASE_URL


class BasePage(object):
    base_url = BASE_URL
    url = ""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def jump(self):
        self.driver.get(self.full_url)
        self.wait_for_jump()

    def wait_for_jump(self):
        WebDriverWait(self.driver, 10).until(url_matches(self.full_url))

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
