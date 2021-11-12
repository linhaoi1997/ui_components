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
