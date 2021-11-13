from .base_input import BaseInput


class TextInput(BaseInput):
    """文本输入框"""

    @property
    def value(self):
        """:return input已经输入的值"""
        return self.element.find_element_by_xpath(".//input| .//textarea").get_attribute("value")

    @value.setter
    def value(self, value: str):
        self._value = value
        input_ = self.element.find_element_by_xpath(".//input|.//textarea")
        self.send_keys(input_, value)


class NumberInput(BaseInput):
    """文本输入框"""

    @property
    def value(self):
        """:return input已经输入的值"""
        return float(self.element.find_element_by_xpath(".//input").get_attribute("value"))

    @value.setter
    def value(self, value: float):
        self._value = value
        input_ = self.element.find_element_by_xpath(".//input")
        self.send_keys(input_, value)


class TextAreaInput(BaseInput):
    """文本输入框"""

    @property
    def value(self):
        """:return input已经输入的值"""
        return self.element.find_element_by_xpath(".//input| .//textarea").get_attribute("value")

    @value.setter
    def value(self, value: str):
        self._value = value
        input_ = self.element.find_element_by_xpath(".//input| .//textarea")
        self.send_keys(input_, value)

    @property
    def label(self):
        return self.element.find_element_by_xpath(".//label/span[last()]").text


class OptionTextInput(BaseInput):
    """输入框，以回车为结束，新增选项"""

    @property
    def value(self):
        """:return input已经输入的值"""
        options = self.element.find_element_by_xpath(".//input").find_elements_by_xpath("./preceding-sibling::div")
        return [i.get_attribute("value") for i in options]

    @value.setter
    def value(self, value: list):
        self._value = "\n".join(value) + "\n"
        input_ = self.element.find_element_by_xpath(".//input")
        self.send_keys(input_, self._value)

# class NoLabelTextInput(TextInput):
#     """有些输入框没有标题label，待实现"""
