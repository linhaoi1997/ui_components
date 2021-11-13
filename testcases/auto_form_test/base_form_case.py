from abc import ABCMeta, abstractmethod
from typing import Type

from .config_form import *
from ui_components.components.form_components import *


class BaseFormCase(metaclass=ABCMeta):

    @property
    @abstractmethod
    def form(self):
        pass

    @property
    @abstractmethod
    def config(self):
        pass

    @property
    @abstractmethod
    def data(self):
        pass


