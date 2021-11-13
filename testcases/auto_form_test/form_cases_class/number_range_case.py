from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class MinMaxCase(BaseFormCase):
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
                    "form1.range": [10, 20],
                },
                "config_form": MinMaxRangeForm
            },
        ]
