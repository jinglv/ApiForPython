import os
import ddt
import unittest
import requests
from utils.excelUtils import ExcelUtils
from utils.requestsUtils import RequestsUtils

curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "excel_file/apis.xlsx")

testdata = ExcelUtils("/Users/lvjing/PycharmProjects/ApiForPython/excel_file/apis.xlsx", "api").dict_data()


@ddt.ddt
class Test_api(unittest.TestCase):
    send_request = RequestsUtils()

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = self.send_request.send_requests(self.s, data)
        print(res)

        # # 检查点 checkpoint
        # check = data["checkpoint"]
        # print("检查点->：%s"%check)
        # # 返回结果
        # res_text = res["text"]
        # print("返回实际结果->：%s"%res_text)
        # # 断言
        # self.assertTrue(check in res_text)

if __name__ == '__main__':
    unittest.main()