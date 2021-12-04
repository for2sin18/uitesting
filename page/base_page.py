import yaml
from appium.webdriver.webdriver import WebDriver

#本质上是对driver操作的一个封装
from selenium.webdriver.common.by import By


class BasePage:
    #driver被定义为WebDriver类型的实例变量，子类可以直接用
    _driver: WebDriver
    _black_list = [(By.ID, "iv_close")]
    def __init__(self, driver: WebDriver = None):
        self._driver = driver


    def find(self,locator, value):
        try:
          el = self._driver.find_element(locator,value)
          return el
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator, value)

#对yaml文件进行循环解析
    def steps(self,path):
        with open(path) as f :
            steps = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action =="click":
                    element.click()