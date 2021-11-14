# import datetime
from typing import Type

from .base_form_case import BaseFormCase
from ..config_form import *
from ...form_components import *


class DateCase(BaseFormCase):
    @property
    def data(self):
        return {
            # "date": datetime.datetime.now(),
            "date": "2021"
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            date = TextInput("日期")

        return Form

    @property
    def config(self):
        return [
            {
                "field_name": "日期",
                "args": {
                    "hint": "日期提示",
                    "default": "默认为当前日期",
                    "date_format": "yyyy"
                },
                "config_form": DateForm
            },
        ]
