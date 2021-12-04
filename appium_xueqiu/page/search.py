
import time
import yaml
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
class Search(BasePage):

    def search(self,name):

        # self.find(By.ID, 'search_input_text').send_keys("alibaba")
        # self._driver.implicitly_wait(5)
        # self.find(By.XPATH, '//*[@text="BABA"]').click()
        # self._driver.implicitly_wait(3)
        # self.find(By.XPATH,
        #           f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="加自选"]').click()

        # with open ("../page/search1.yaml",encoding="utf-8") as f:
        #     steps = yaml.safe_load (f)
        # for step in steps:
        #     if "by" in step.keys ():
        #         element = self.find (step["by"], step["locator"])
        #     if "action" in step.keys ():
        #         action = step["action"]
        #         if action == "click":
        #             element.click ()
        #         if "send" == action:
        #             element.send_keys(step["value"])
        self.step("../page/search.yaml","search")
    def add(self,name):
        self.step("../page/search.yaml","add")



    def is_choose(self,name):
         # eles = self.finds(By.XPATH,
         #                   f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="已添加"]')
         #return len(eles) > 0
         return self.step("../page/search.yaml","is_choose")
    def reset(self,reset):
        return self.step("../page/search.yaml","reset")