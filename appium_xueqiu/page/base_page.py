from typing import Any, Union

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging
import yaml
#把核心代码写进base_page中，持续维护base_page
from appium_xueqiu.page.wrapper import handle_black


class BasePage:
    # 弹框 处理的定位列表


    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def finds(self,locator, value):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator,tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator,value)
        self._driver.implicitly_wait(10)
        return element

    @handle_black
    def find_and_get_text(self, locator, value):
        element: WebElement
        if isinstance(locator,tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text


    def step(self, path, name):

        with open (path,encoding="utf-8") as f:
            steps = yaml.safe_load (f)[name]
        for step in steps:
            if "action" in step.keys ():
                action = step["action"]
                if action == "click":
                    if "by" in step.keys ():
                        self.find (step["by"], step["locator"]).click()
                if "send" == action:
                        self.find (step["by"], step["locator"]).send_keys(step["value"])

                if "len > 0" == action:
                    eles = self.finds(step["by"],step["locator"])
                    return len(eles) > 0




