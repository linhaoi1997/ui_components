from abc import ABCMeta, abstractmethod
from typing import Type

from ui_components.components.form_components import *
from .config_form import *


class BaseFormCase(metaclass=ABCMeta):

    @property
    @abstractmethod
    def form(self):
        pass

    @property
    @abstractmethod
    def config(self):
        pass


class TextAndHintCase(BaseFormCase):

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            hint = TextInput("提示")
            text = TextInput("输入框-文本")

        return Form

    @property
    def config(self):
        return [
            {"field_name": "提示", "args": {"text": "测试文本"}, "config_form": HintForm},
            {"field_name": "输入框-文本", "args": {"hint": "这是文本"}, "config_form": TextForm},
        ]
