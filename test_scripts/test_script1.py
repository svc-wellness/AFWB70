from generic.base_setup import BaseSetup
from generic.excel import Excel

class TestScript1(BaseSetup):

    def test_script1(self):
        print('this is test script 1')
        print(self.driver.title)
        v = Excel.get_data(self.xl_path, "Sheet1", 1, 1)
        print(v)
