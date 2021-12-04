from selenium.webdriver.common.by import By
import time
from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market
import yaml


class Main(BasePage):

    def goto_market(self):
        #self.find(By.XPATH,"//*[@resource-id = 'android:id/tabs']//*[@text='行情']").click()
        self.step("../page/main.yaml","goto_market")
        return Market(self._driver)