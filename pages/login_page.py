from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_changes
from ui_components.components.form_components import *
from ui_components.elements.template_elements import ButtonElement
from .base_page import BasePage


class LoginForm(FormComponent):
    DEFAULT_LOCATOR = "//form/div/div"
    account = TextInput("登录账号")
    password = TextInput("登录密码")


class LoginPage(BasePage):
    url = "login"
    form = LoginForm()
    login_button = ButtonElement("登录")

    def login(self, account, password):
        form = self.form
        form.account = account
        form.password = password
        self.login_button.click()
        WebDriverWait(self.driver, 10).until(url_changes(self.full_url))
