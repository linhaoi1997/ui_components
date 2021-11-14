from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class CheckboxCase(BaseFormCase):
    @property
    def data(self):
        return {
            "checkbox": ["1", "2", "3"],
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            checkbox = CheckBoxGroupInput("复选框组")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "复选框组",
                "args": {
                    "text": ["1", "2", "3"],
                    "default": ["2", "3"],
                },
                "config_form": CheckForm
            },
        ]
