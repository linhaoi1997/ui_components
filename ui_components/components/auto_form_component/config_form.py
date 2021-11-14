from ui_components.components.base_component import BaseComponent
from ui_components.components.form_components import *


# 基类表单
class BaseDefinedForm(BaseComponent):
    DEFAULT_LOCATOR = "//label[span='字段名称']/ancestor::div[label]/.."

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

    def __setattr__(self, key, value):
        if "." in key:
            keys = key.split(".")
            object_ = self
            for i in keys[:-1]:
                object_ = getattr(object_, i)
            setattr(object_, keys[-1], value)
        else:
            super(BaseDefinedForm, self).__setattr__(key, value)


# 提示文本表单
class HintForm(BaseDefinedForm):
    text = TextInput("文本内容")

    def setup(self):
        # self.field_format = "提示"
        self.field_format = "提示文本"


# 文本表单
class TextForm(BaseDefinedForm):
    limit = RadioGroupInput("输入内容限制")
    hint = TextInput("输入提示")
    default = TextAreaInput("输入默认内容")
    unit = TextInput("输入单位")

    def setup(self):
        self.field_format = "输入框"
        self.limit = "文本"


# 下拉框表单
class SingleSelectForm(BaseDefinedForm):
    options = OptionTextInput("选项内容")
    is_single = RadioGroupInput("下拉是否多选")
    hint = TextInput("下拉输入提示")
    default = NativeSelectInput("下拉默认内容")

    def setup(self):
        self.field_format = "下拉框"
        self.is_single = "单选"


class MuiSelectForm(SingleSelectForm):
    default = MuiSelectInput("下拉默认内容")

    def setup(self):
        self.field_format = "下拉框"
        self.is_single = "多选"


# 数值范围子表单
class NumberRangeForm(BaseComponent):
    DEFAULT_LOCATOR = ".//label[span='最小值']/parent::div[label]/.."
    min_range = NumberInput("最小值")
    max_range = NumberInput("最大值")


# 数值配置表单
class NumberConfigForm(BaseComponent):
    DEFAULT_LOCATOR = "//label[span='大小范围']/parent::div[label]/.."
    range = NumberRangeForm()
    can_be_zero = RadioGroupInput("能否为零")
    decimal_digits = RadioGroupInput("小数位数")


# 数值表单
class NumberForm(TextForm):
    number_config = NumberConfigForm()

    def setup(self):
        self.field_format = "输入框"
        self.limit = "数值"


# 日期表单
class DateForm(BaseDefinedForm):
    hint = TextInput("日期输入提示")
    default = RadioGroupInput("日期默认内容")
    date_format = NativeSelectInput("日期显示格式")

    def setup(self):
        self.field_format = "日期"


# 单选按钮组表单
class RadioForm(BaseDefinedForm):
    text = OptionTextInput("选项内容")
    default = NativeSelectInput("默认选中选项")

    def setup(self):
        self.field_format = "单选按钮组"


# 复选框组表单
class CheckForm(BaseDefinedForm):
    text = OptionTextInput("复选选项")
    default = MuiSelectInput("默认选中选项")

    def setup(self):
        self.field_format = "复选框组"


# 子表单
class SubTextForm(TextForm):
    name = TextInput("输入框名称")

    def setup(self):
        self.limit = "文本"


class SubNumberForm(NumberForm):
    name = TextInput("输入框名称")

    def setup(self):
        self.limit = "数值"


# 输入框组表单
TEXT_GROUP_LOCATOR = "//label[span='是否必填']/ancestor::div[label]/following-sibling::div/div/div[%s]" \
                     "//label[span='输入框名称']/ancestor::div[label]/.."


class TextGroupForm(BaseDefinedForm):
    text_form1 = SubTextForm(TEXT_GROUP_LOCATOR % 1)
    text_form2 = SubNumberForm(TEXT_GROUP_LOCATOR % 2)

    def setup(self):
        # self.field_format = "输入框组"
        self.field_format = "文本+输入框"


# 下拉框+输入框
class SingleSelectAndTextForm(SingleSelectForm, TextForm):
    select_hint = TextInput("下拉输入提示")

    def setup(self):
        self.field_format = "下拉框+输入框"
        self.is_single = "单选"
        self.limit = "文本"


class MuiSelectAndTextForm(MuiSelectForm, TextForm):

    def setup(self):
        self.field_format = "下拉框+输入框"
        self.is_single = "多选"
        self.limit = "文本"


class MuiSelectAndNumberForm(MuiSelectForm, NumberForm):

    def setup(self):
        self.field_format = "下拉框+输入框"
        self.is_single = "多选"
        self.limit = "数值"


# 下拉框+日期
class SingleSelectAndDateForm(SingleSelectForm, DateForm):

    def setup(self):
        self.field_format = "下拉框+日期"
        self.is_single = "单选"


# 复选框组+日期
class CheckboxAndTextForm(CheckForm, TextForm):

    def setup(self):
        self.field_format = "复选框组+输入框"
        self.limit = "文本"


# 复选框组+日期


class MinMaxRangeConfigForm(NumberConfigForm):
    required = RadioGroupInput("是否必填")
    range = DoubleNumbersInput("数值大小范围")
    hint = TextInput("输入提示")
    default = NumberInput("输入默认内容")
    unit = TextInput("输入单位")


class MinMaxRangeForm(BaseDefinedForm):
    form1 = MinMaxRangeConfigForm("//p[text()='最小值输入框']/following-sibling::div")
    form2 = MinMaxRangeConfigForm("//p[text()='最大值输入框']/following-sibling::div")
    decimal_places = RadioGroupInput("小数位数")

    def setup(self):
        self.field_format = "数值范围输入框组"
