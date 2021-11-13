import datetime
from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class MinMaxCase(BaseFormCase):
    @property
    def data(self):
        return {
            "date": datetime.datetime.now(),
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            date = DateInput("日期")

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
