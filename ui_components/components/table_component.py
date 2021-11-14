import allure
from selenium.webdriver.support.wait import WebDriverWait

from ui_components.components.base_component import PageComponent


class TValues(object):
    """表格的基本元素"""

    def __init__(self, element):
        self.element = element

    @property
    def value(self):
        """:return 元素的值"""
        return self.element.text

    @property
    def buttons(self):
        """:return 返回元素里面存在的按钮"""
        return self.element.find_elements_by_tag_name("button")

    @property
    def status(self):
        """表格第一行一般是勾选的checkbox"""
        return "checked" in self.element.find_element_by_xpath("./span").get_attribute("class")

    def select(self):
        if self.status:
            print("already selected")
        else:
            self.element.click()
            WebDriverWait(self.element.parent, 5).until(lambda: self.status is True, "点击失败，未知原因")


class THead(object):
    """表格头"""

    def __init__(self, element):
        self.element = element
        self.columns = [TValues(i) for i in self.element.find_elements_by_tag_name("th")]

    def __iter__(self):
        yield from self.columns


class TBody(object):
    """表格内容"""

    def __init__(self, element, thead):
        self.head = thead
        self.element = element
        self.columns = [TColumn(i, self.head) for i in self.element.find_elements_by_tag_name("tr")]

    def __getitem__(self, item):
        # 数字
        return self.columns[item]

    def __iter__(self):
        yield from self.columns


class TColumn(object):
    """表格行"""

    def __init__(self, element, head):
        self.head = head
        self.element = element
        self.values = [TValues(i) for i in self.element.find_elements_by_tag_name("td")]

    def get_element(self, item):
        for index, i in enumerate(self.head):
            if i.value == item:
                return self.values[index]
        raise Exception("没有名字为%s的列" % item)

    @property
    def operation(self):
        return self.get_element("操作")

    def get_value(self, item):
        return self.get_element(item).value

    def __getitem__(self, item):
        # 具体值
        return self.get_value(item)

    def to_dict(self):
        result = {}
        for index, i in enumerate(self.head):
            result[i.value] = self.values[index].value
        return result

    def __str__(self):  # 调试用
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__()


class Table(PageComponent):
    DEFAULT_LOCATOR = '//table'

    @property
    def head(self):
        return THead(self.element.find_element_by_tag_name("thead"))

    @property
    def body(self):
        return TBody(self.element.find_element_by_tag_name("tbody"), self.head)

    # 获取第几行
    def __getitem__(self, item):
        return self.body[item]

    def filter(self, items: dict):
        iter_list = self.body
        for key, value in items.items():
            iter_list = list(filter(lambda a: a[key] == str(value), iter_list))
        return list(iter_list)

    # 返回一行表格的值，如果不是一行报错
    def search(self, items: dict) -> TColumn:
        iter_list = self.filter(items)
        if len(iter_list) != 1:
            allure.attach(self.element.parent.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
            raise AssertionError("期望只返回一个值，但是返回为%s" % iter_list)
        return iter_list[0]

    # 获取某列的所有值
    def get_column_values(self, column_name) -> list:
        result = []
        for i in self.body:
            result.append(i.get_value(column_name))
        return result

    def to_dict(self):
        return [i.to_dict() for i in self.body]

    def __get__(self, instance, owner):
        super(Table, self).__get__(instance, owner)
        return self
