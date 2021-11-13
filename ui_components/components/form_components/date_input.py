from .base_input import BaseInput
import datetime


class DateInput(BaseInput):

    @property
    def value(self):
        return self.element.find_element_by_xpath(".//input").get_attribute("value"). \
            replace("/", " ").replace(":", " ")

    @value.setter
    def value(self, value: datetime.datetime):
        self._value = value
        input_ = self.element.find_element_by_xpath(".//input")
        if isinstance(value, datetime.datetime):
            self.send_keys(input_, value.strftime("%Y%m%d%H%M"))
        else:
            self.send_keys(input_, value)

    def fake(self):
        self.value = datetime.datetime.now()
