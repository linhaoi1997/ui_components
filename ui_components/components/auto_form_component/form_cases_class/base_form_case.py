from abc import ABCMeta, abstractmethod


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


