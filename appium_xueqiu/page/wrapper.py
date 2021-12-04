from selenium.webdriver.common.by import By


def handle_black(func):
    #(*args,**kwargs):接所有参数和所有关键字然后主动调fuc()
    def wrapper(*args,**kwargs):
        from appium_xueqiu.page.base_page import BasePage
        _black_list = [
            (By.ID, 'action_search'),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]

        try:
            element = func(*args,**kwargs)
            # 找到之前 _error_num 归0
            _error_num = 0
            # 隐式等待回复原来的等待，
            instance._driver.implicitly_wait(10)
            return element

        except Exception as e:
            # 出现异常， 将隐式等待设置小一点，快速的处理弹框
            instance._driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return wrapper(*args, **kwargs)

            raise e

    return wrapper