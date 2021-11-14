from typing import Type

from .base_form_case import BaseFormCase
from ..config_form import *
from ...form_components import *


class RadioCase(BaseFormCase):
    @property
    def data(self):
        return {
            "radios": "1",
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            radios = RadioGroupInput("单选按钮组")

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
