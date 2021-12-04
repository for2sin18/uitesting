from selenium.webdriver.common.by import By
import time
from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):

    def goto_search(self):
        #click
        #self.find(By.ID, 'action_search').click()
        return Search(self._driver)