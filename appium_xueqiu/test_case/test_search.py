from appium_xueqiu.page.app import App
class TestSearch():
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    def test_search(self):
        self.search.search ("阿里巴巴")
        if self.search.is_choose("阿里巴巴"):
            self.search.reset("阿里巴巴")
        self.search.add("阿里巴巴")
        assert self.search.is_choose("阿里巴巴")