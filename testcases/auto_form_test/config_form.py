from ui_components.components.form_components import *


class BaseDefinedForm(FormComponent):
    field_name = TextInput("字段名称")
    user_role = RadioGroupInput("角色权限")
    field_format = RadioGroupInput("字段格式")
    required = RadioGroupInput("是否必填")

    def setup(self):
        pass

    def __get__(self, instance, owner):
        super(BaseDefinedForm, self).__get__(instance, owner)
        self.setup()
        return self


class HintForm(BaseDefinedForm):
    text = TextInput("文本内容")

    def setup(self):
        self.field_format = "提示"


class TextForm(BaseDefinedForm):
    limit = RadioGroupInput("输入内容限制")
    hint = TextInput("输入提示")
    default = TextAreaInput("输入默认内容")
    unit = TextInput("输入单位")

    def setup(self):
        self.field_format = "输入框"
        self.limit = "文本"


class _NumberConfigForm(FormComponent):
    min_range = NumberInput("最小值")
    max_range = NumberInput("最大值")
    can_be_zero = RadioGroupInput("能否为零")
    decimal_digits = RadioGroupInput("小数位数")

    @property
    def value(self):
        return [self.min_range.value, self.max_range.value, self.can_be_zero.value, self.decimal_digits.value]

    @value.setter
    def value(self, values: list):
        self.min_range = values[0]
        self.max_range = values[1]
        self.can_be_zero = values[2]
        self.decimal_digits = values[3]


class NumberForm(TextForm):
    number_config = _NumberConfigForm()

    def setup(self):
        self.field_format = "输入框"
        self.limit = "输值"


class DateForm(BaseDefinedForm):
    hint = TextInput("日期输入提示")
    default = TextInput("日期默认内容")
    date_format = TextInput("日期显示格式")

    def setup(self):
        self.field_format = "日期"


class RadioForm(BaseDefinedForm):
    text = OptionTextInput("选项内容")
    default = NativeSelectInput("默认选中选项")

    def setup(self):
        self.field_format = "单选按钮组"


class CheckForm(BaseDefinedForm):
    text = OptionTextInput("复选选项")
    default = MuiSelectInput("默认选中选项")

    def setup(self):
        self.field_format = "复选框组"

