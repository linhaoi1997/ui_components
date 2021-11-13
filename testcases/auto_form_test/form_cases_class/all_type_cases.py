from typing import Type

from testcases.auto_form_test.base_form_case import BaseFormCase
from testcases.auto_form_test.config_form import *
from ui_components.components.form_components import *


class AllTypeCase(BaseFormCase):
    @property
    def data(self):
        return {
            "text": "测试文本",
            # "number": 10,
            "input_group": ["输入框1文本", 10],
            "select_and_text": ["2", "输入框文本"],
            "checkbox_and_text": [["1", "2"], "输入框文本"]
        }

    @property
    def form(self) -> Type[FormComponent]:
        class Form(FormComponent):
            hint = TextInput("提示")
            text = TextAreaInput("输入框-文本")
            # number = NumberInput("输入框-数值") 有bug，待修复
            input_group = TextGroupInput("输入框组")
            select_and_text = SelectAndTextGroupInput("下拉框+输入框")
            checkbox_and_text = CheckBoxGroupAndTextInput("复选框组+输入框")
            mui_select_and_text = MuiSelectAndTextGroupInput("多选下拉框+数值输入框")
            min_max_input = DoubleNumbersInput("数值范围输入框组")

        return Form

    @property
    def config(self):
        return [
            {"field_name": "提示", "args": {"text": "测试文本"}, "config_form": HintForm},
            {
                "field_name": "输入框-文本",
                "args": {
                    "hint": "输入提示",
                    "default": "测试默认值",
                    "unit": "输入单位",
                },
                "config_form": TextForm
            },
            {
                "field_name": "输入框-数值",
                "args": {
                    "number_config.range.min_range": 1,
                    "number_config.range.max_range": 10,
                    "number_config.decimal_digits": "2",
                    "number_config.can_be_zero": "不可为零",
                    "hint": "输入数字提示",
                    "default": 4,
                    "unit": "输入数字单位",
                },
                "config_form": NumberForm
            },
            {
                "field_name": "输入框组",
                "args": {
                    "text_form1.name": "输入框1",
                    "text_form1.hint": "输入框1提示",
                    "text_form2.name": "输入框2",
                    "text_form2.number_config.range.min_range": 1,
                    "text_form2.number_config.range.max_range": 10,
                    "text_form2.number_config.decimal_digits": "2",
                    "text_form2.number_config.can_be_zero": "不可为零",
                    "text_form2.hint": "输入数字提示",
                    "text_form2.default": 4,
                    "text_form2.unit": "输入数字单位",
                },
                "config_form": TextGroupForm
            },
            {
                "field_name": "下拉框+输入框",
                "args": {
                    "options": ["1", "2"],
                    "default": "1",
                    "hint": "输入提示",
                    "select_hint": "下拉输入提示",
                    "unit": "x¥",
                },
                "config_form": SingleSelectAndTextForm
            },
            {
                "field_name": "多选下拉框+数值输入框",
                "args": {
                    "options": ["1", "2"],
                    "select_hint": "多选下拉输入提示",
                    "default": "1",
                    "hint": "数值输入提示",
                    "number_config.range.min_range": 1,
                    "number_config.range.max_range": 10,
                    "unit": "mx¥",
                },
                "config_form": MuiSelectAndNumberForm
            },
            {
                "field_name": "复选框组+输入框",
                "args": {
                    "text": ["1", "2"],
                    "hint": "输入框提示"
                },
                "config_form": CheckboxAndTextForm
            },
            {
                "field_name": "数值范围输入框组",
                "args": {
                    "decimal_places": "2",
                    "form1.range": [10, 20],
                    "form1.required": "不必填",
                    "form1.can_be_zero": "不可为零",
                    "form1.hint": "输入提示",
                    "form1.default": 11,
                    "form1.unit": "输入单位",
                },
                "config_form": MinMaxRangeForm
            },
            {
                "field_name": "单选下拉框+日期",
                "args": {
                    "options": ["1", "2", "3"],
                    "default": "1",
                    "hint": "输入提示",
                    "date_format": "yyyy"
                },
                "config_form": SingleSelectAndDateForm
            },
        ]
