# ui自动化实践

1. 项目背景
    
    公司有一个项目为自定义表单通用产品，前端有通用组件，后端有通用服务
    
    即对于公司的每一个表单，都可以使用这个产品为公司的表单装饰一个自定义表单
    
    前端的自定义表单的页面的操作方式是一样的，所有的可以选择的字段也是一样的（输入框，下拉框，radio，checkbox还有许多复杂字段），唯一的不同是页面的不同。
    
    期望ui自动化可以实现
    
    1. 设计所有自定义字段的测试用例
    2. 校验自定义表单的定义
    3. 校验自定义表单装饰表单的填写正常
    4. 校验自定义表单装饰表单填写后的数据与填写的一致
2. 实现思路
    
    公司对于前端的表单组件是有规范的，ui自动化这边去实现对应用到的组件的操作（table，input），然后由这些组件去组成表单，组成页面，实现代码的复用
    
    元素 → 组件 → 页面
    
    比方说对于一个表单界面，期望写出这样的代码
    
    ```python
    class LoginForm(FormComponent):
        DEFAULT_LOCATOR = "//form/div/div"
        account = TextInput("登录账号")
        password = TextInput("登录密码")
    
    class LoginPage(BasePage):
        url = "login"
        form = LoginForm()
        login_button = ButtonElement("登录")
    
        def login(self, account, password):
            form = self.form
            form.account = account
            form.password = password
            self.login_button.click()
            WebDriverWait(self.driver, 10).until(url_changes(self.full_url))
    ```
    
    而自定义表单的具体的用例实现可以抽象为三个步骤
    
    1. 定义表单，在自定义表单页面定义成功（这个界面本身是填写各个字段的表单类型）
    2. 对应装饰的表单页面填写表单成功（定义自定义表单之后会生成一个表单，在对应页面去填写）
    3. 填写表单后校验数据保存成功
    
    所以一个测试用例应该包含三个数据
    
    1. 自定义表单页面的配置
    2. 自定义配置后返回的表单
    3. 表单填写的数据
3. 代码封装思路
    1. 自定义表单也是由表单填写的，先定义所有自定义表单的表单（有点绕哈），然后定义自定义表单组件的所有操作
        1. 自定义表单的表单定义
            
            ```python
            # 文本的表单的输入选项，除了基本的是否必填，字段名称在BaseDefinedForm定义之后，特殊的字段如下定义
            class TextForm(BaseDefinedForm):
                limit = RadioGroupInput("输入内容限制")
                hint = TextInput("输入提示")
                default = TextAreaInput("输入默认内容")
                unit = TextInput("输入单位")
            
                def setup(self):
                    self.field_format = "输入框"
                    self.limit = "文本"
            ```
            
        2. 用例定义期望写出这样的方法，调用自定义表单组件的设置表单方法就可以完成表单定义
            
            ```python
            class DateCase(BaseFormCase):
                @property
                def data(self): # 填写的表单
                    return {
                        # "date": datetime.datetime.now(),
                        "date": "2021"
                    }
            
                @property
                def form(self) -> Type[FormComponent]: # 自定义之后生成的表单
                    class Form(FormComponent):
                        date = TextInput("日期")
            
                    return Form
            
                @property
                def config(self): # 自定义表单的配置
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
            ```
            
    2. 实现对应页面的基础表单填写，做一个上下文管理器，将本来表单的必填项填写好，在上下文管理器执行的中进行自定义表单数据的填写（每个要装饰的表单有一定的开发量，但是使用的是一样的用例），填写完自定义的表单之后提交表单
        
        ```python
        class SaleForm(FormComponent):
            name = NativeSelectInput("客户名称")
            except_time = DateInput("期望交期")
            country = NativeSelectInput("地区")
            address = TextInput('详细地址')
        
        class CreateSaleSamplePage(BasePage):
            url = "subapp/sale/sample/create"
            form = SaleForm()
            add_product_button = ButtonElement("添加")
            save = ButtonElement("保存")
        
            def add_product(self): # 表单之外的交互流程
                self.add_product_button.click()
                self.driver.find_element(By.XPATH, "//table//button[span='添加']").click()
                self.driver.find_element(By.XPATH, "//div[@role='presentation']//button/span/*[name()='svg']").click()
                self.driver.find_element(By.XPATH, "//input[@name='itemList.0.price']").send_keys(10)
                self.driver.find_element(By.XPATH, "//input[@name='itemList.0.orderNumber']").send_keys(10)
        
            @contextmanager
            def prepare_for_form(self):
                form = self.form # 填写自定义表单之前填写页面本身的表单
                form.name.fake()
                form.except_time.fake()
                form.country = "伊朗"
                form.address.fake()
                self.add_product()
                yield # 这里上下文管理器执行，填写自定义表单
                self.save.click()
                WebDriverWait(self.driver, 5).until(url_changes(self.full_url))
                new_page = SaleSamplePage(self.driver)
                return new_page
        ```
        
    3. 填写后在详情页，或者编辑页面做数据的校验，具体页面根据业务去开发不同的代码