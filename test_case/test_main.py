from page.app import App
import pytest
import yaml

from test_case.test_base import TestBase

print("测试点1")
class TestMain(TestBase):
    print("测试点2")
    #@pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self):
        self.app.start().main().goto_search()
        #print(value1)
        #print(value1)

#     def test_windows(self):
#         self.app.start().main().goto_windows()
# # if __name__ == '__main__':
# #      test = TestMain()
# #      test.test_windows()