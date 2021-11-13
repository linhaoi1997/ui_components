import datetime
from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class MinMaxCase(BaseFormCase):
    @property
    def data(self):
        return {
            "radios": "1",
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            date = RadioGroupInput("单选按钮组")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "单选按钮组",
                "args": {
                    "text": ["1", "2", "3"],
                    "default": "2",
                },
                "config_form": RadioForm
            },
        ]
