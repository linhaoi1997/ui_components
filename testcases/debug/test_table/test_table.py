from pages.sale_sample_page import UpdateSaleSamplePage
from ui_components.components.table_component import Table
from ui_components.elements.elements import Element
from ui_components.elements.options_elements import OptionsElement
from ui_components.utils.get_driver import get_driver


class Page:
    table = Table()
    options = OptionsElement()
    edit_button = Element("//li[text()='提交']")

    def __init__(self, driver):
        self.driver = driver


def test():
    driver = get_driver()
    page = Page(driver)
    table = page.table
    table[0].operation.buttons[0].click()
    page.edit_button.click()


def test2():
    driver = get_driver()
    page = UpdateSaleSamplePage(driver)
    form = page.form
    print(form.address.value)
