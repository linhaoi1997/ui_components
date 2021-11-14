from typing import Type

from .base_form_case import BaseFormCase
from ..config_form import *
from ...form_components import *


class SelectCase(BaseFormCase):
    @property
    def data(self):
        return {
            "select": "金斧子",
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            select = NativeSelectInput("下拉单选框")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "下拉单选框",
                "args": {
                    "options": ["金斧子", "银斧子", "铜斧子"],
                    "hint": "输入提示",
                    "default": "金斧子"
                },
                "config_form": SingleSelectForm
            },
        ]
