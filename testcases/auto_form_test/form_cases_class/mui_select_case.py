from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class MuiSelectCase(BaseFormCase):
    @property
    def data(self):
        return {
            "mui_select": ["金斧子"],
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            mui_select = MuiSelectInput("下拉多选框")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "下拉多选框",
                "args": {
                    "options": ["金斧子", "银斧子", "铜斧子"],
                    "hint": "输入提示",
                    "default": ["金斧子"]
                },
                "config_form": MuiSelectForm
            },
        ]
