"""复合表单，这里面实现了所有的自定义表单声明的字段，待实现"""
import logging

from selenium.common.exceptions import NoSuchElementException

from .base_input import BaseInput
from .text_input import TextInput, NoLabelTextInput, TextAreaInput
from .select_input import NativeSelectInput, NoLabelMuiSelectInput, MuiSelectInput
from .date_input import DateInput
from .checkbox_input import CheckBoxGroupInput

from .form_component import FormComponent
from ...utils.change_wait_time import change_wait_time


class TextGroupForm(FormComponent):
    DEFAULT_LOCATOR = ".//div[@variant='outlined']"
    base_finder_attr = "element"
    input1 = TextAreaInput(num=1)
    input2 = TextAreaInput(num=2)
    input3 = TextAreaInput(num=3)


class TextGroupInput(BaseInput):
    INPUTS_LOCATOR = ".//div[@variant='outlined']/div"
    form = TextGroupForm()

    @property
    def value(self):
        with change_wait_time(self.driver):
            form = self.form
            result = {}
            for i in range(3):
                try:
                    input_element = getattr(form, "input" + str(i + 1))
                    logging.info(input_element.label)
                    result[input_element.label] = input_element.value
                except NoSuchElementException as e:
                    logging.info(e)

        return result

    @value.setter
    def value(self, values: list):
        form = self.form
        for i in range(3):
            logging.info(values[i])
            setattr(form, "input" + str(i + 1), values[i])


class SelectAndTextGroupForm(FormComponent):
    DEFAULT_LOCATOR = ".//div[@variant='outlined']"
    base_finder_attr = "element"
    input1 = NativeSelectInput(num=1)
    input2 = TextAreaInput(num=2)


class SelectAndTextGroupInput(BaseInput):
    INPUTS_LOCATOR = ".//div[@variant='outlined']/div"
    form = SelectAndTextGroupForm()

    @property
    def value(self):
        form = self.form
        return [form.input1.value, form.input2.value]

    @value.setter
    def value(self, value: list):
        form = self.form
        form.input1 = value[0]
        form.input2 = value[1]


class MultiSelectAndTextGroupForm(FormComponent):
    DEFAULT_LOCATOR = ".//div[@variant='outlined']"
    base_finder_attr = "element"
    input1 = MuiSelectInput(num=1)
    input2 = TextAreaInput(num=2)


class MuiSelectAndTextGroupInput(SelectAndTextGroupInput):
    pass


class SelectAndDateInput(BaseInput):
    INPUTS_LOCATOR = ".//div[@variant='outlined']/div"

    def __init__(self, element):
        super(SelectAndDateInput, self).__init__(element)
        tmp = self.element.find_elements_by_xpath(self.INPUTS_LOCATOR)
        self.select_input = NativeSelectInput(tmp[0])
        self.date_input = DateInput(tmp[1])

    @property
    def value(self):
        """:return input已经输入的值"""
        return self._value or str([self.select_input.value, self.date_input.value])

    @value.setter
    def value(self, value):
        self.select_input.value = value[0]
        self.date_input.value = value[1]
        self._value = value


class MuiSelectAndDateInput(SelectAndDateInput):

    def __init__(self, element):
        super(MuiSelectAndDateInput, self).__init__(element)
        tmp = self.element.find_elements_by_xpath(self.INPUTS_LOCATOR)
        self.select_input = NoLabelMuiSelectInput(tmp[0], self.element.find_element_by_xpath(self.LABEL_LOCATOR))
        self.date_input = DateInput(tmp[1])


class CheckBoxGroupAndTextInput(BaseInput):
    INPUTS_LOCATOR = ".//div[@variant='outlined']/div"

    def __init__(self, element):
        super(CheckBoxGroupAndTextInput, self).__init__(element)
        tmp = self.element.find_elements_by_xpath(self.INPUTS_LOCATOR)
        self.checkbox_group_input = CheckBoxGroupInput(tmp[0])
        self.text_input = NoLabelTextInput(tmp[1])

    @property
    def real_value(self):
        return [self.checkbox_group_input.real_value, self.text_input.value]

    @property
    def value(self):
        """:return input已经输入的值"""
        return self._value or str([self.checkbox_group_input.real_value, self.text_input.value])

    @value.setter
    def value(self, value):
        self.checkbox_group_input.value = value[0]
        self.text_input.value = value[1]
        self._value = value
