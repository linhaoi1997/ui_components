from typing import Type

from .base_form_case import BaseFormCase
from ..config_form import *
from ...form_components import *


class NumberRangeCase(BaseFormCase):
    @property
    def data(self):
        return {
            "numbers_group": [10, 10],
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            numbers_group = DoubleNumbersInput("数值范围输入框组")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "数值范围输入框组",
                "args": {
                    "decimal_places": "2",
                    "form1.range": [10, 20],
                    "form1.required": "不必填",
                    "form1.can_be_zero": "不可为零",
                    "form1.hint": "输入提示",
                    "form1.default": 11,
                    "form1.unit": "输入单位",
                },
                "config_form": MinMaxRangeForm
            },
        ]
