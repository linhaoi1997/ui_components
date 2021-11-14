from typing import Type

from .base_form_case import BaseFormCase
from ..config_form import *
from ...form_components import *


class NumberCase(BaseFormCase):
    @property
    def data(self):
        return {
            "number": 5,
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            number = NumberInput("输入框-数值")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "输入框-数值",
                "args": {
                    "number_config.range.min_range": 1,
                    "number_config.range.max_range": 10,
                    "number_config.decimal_digits": "2",
                    "number_config.can_be_zero": "不可为零",
                    "hint": "输入数字提示",
                    "default": 4,
                    "unit": "输入数字单位",
                },
                "config_form": NumberForm
            },
        ]
