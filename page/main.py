from selenium.webdriver.common.by import By

from page.base_page import BasePage
#对雪球app操作
class Main(BasePage):
    def goto_search(self):
        #self.find(By.ID,'home_search').click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID,"post_status").click()
        self.find(By.ID, 'home_search').click()
