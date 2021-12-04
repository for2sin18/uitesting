from page.app import App
##对test的通用改进例如对断言改进都可以写在test_case中

class TestBase:
    app = None
    def setup(self):
        self.app = App()