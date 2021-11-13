from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class MinMaxCase(BaseFormCase):
    @property
    def data(self):
        return {
            "text": "输入框-文本测试",
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            text = TextInput("输入框-文本")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "输入框-文本",
                "args": {
                    "hint": "输入提示",
                    "default": "测试默认值",
                    "unit": "输入单位",
                },
                "config_form": TextForm
            },
        ]
