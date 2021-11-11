"""复合表单，这里面实现了所有的自定义表单声明的字段，待实现"""
import logging

from selenium.common.exceptions import NoSuchElementException

from .base_input import BaseInput
from .text_input import TextAreaInput
from .select_input import NativeSelectInput, MuiSelectInput
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


# 单选下拉框
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


# 多选下拉框
class MultiSelectAndTextGroupForm(SelectAndTextGroupForm):
    input1 = MuiSelectInput(num=1)


class MuiSelectAndTextGroupInput(SelectAndTextGroupInput):
    form = MultiSelectAndTextGroupForm()


# 下拉框+日期
class SelectAndDateFrom(SelectAndTextGroupForm):
    input2 = DateInput(num=2)


class SelectAndDateInput(SelectAndTextGroupInput):
    form = SelectAndDateFrom()


# 多选下拉框+日期
class MuiSelectAndDateForm(SelectAndDateFrom):
    input1 = MuiSelectInput(num=1)


class MuiSelectAndDateInput(SelectAndDateInput):
    form = MuiSelectAndDateForm()


class CheckBoxGroupAndTextFrom(SelectAndTextGroupForm):
    input1 = CheckBoxGroupInput()


class CheckBoxGroupAndTextInput(SelectAndTextGroupInput):
    form = CheckBoxGroupAndTextFrom()
