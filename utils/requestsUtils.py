import requests
import urllib3
import json
from utils.excelUtils import ExcelUtils
from utils.logger import Log

urllib3.disable_warnings()  # 忽略ssl问题


class RequestsUtils(object):

    log = Log()

    def send_requests(self, s, testdata):
        """
            封装Requests请求
        :param s:
        :param testdata:
        :return:
        """
        is_run = testdata["run"]
        method = testdata["method"]
        url = testdata["url"]

        # url后面的params参数
        try:
            params = self.covert_params(testdata["params"], ";")
            self.log.info("请求参数: %s" % params)
        except:
            params = None
        # 请求头部headers
        try:
            headers = eval(testdata["headers"])
            self.log.info("请求头部：%s" % headers)
        except:
            headers = None

        # post请求body类型
        type = testdata["type"]

        test_nub = testdata['id']
        self.log.info("*******正在执行用例：-----  %s  ----**********" % test_nub)
        self.log.info("请求方式：%s, 请求url:%s" % (method, url))

        # post请求body内容
        try:
            bodydata = testdata["body"]
        except:
            bodydata = {}

        # 判断传data数据还是json
        if type == "data":
            body = bodydata
        elif type == "json":
            body = json.dumps(bodydata)
        else:
            body = bodydata
        if method == "post":
            self.log.info("post请求body类型为：%s ,body内容为：%s" % (type, body))

        verify = False
        restult = {}  # 接受返回数据

        try:
            r = s.request(method=method,
                          url=url,
                          params=params,
                          headers=headers,
                          data=body,
                          verify=verify
                          )
            self.log.info("页面返回信息：%s" % r.content.decode("utf-8"))
            restult['id'] = testdata['id']
            restult['rowNum'] = testdata['rowNum']
            restult["statuscode"] = str(r.status_code)  # 状态码转成str
            restult["text"] = r.content.decode("utf-8")
            restult["times"] = str(r.elapsed.total_seconds())  # 接口请求时间转str
            self.log.info("接口执行状态码: %s" % r.status_code)
            if restult["statuscode"] != "200":
                restult["error"] = restult["text"]
            else:
                restult["error"] = ""
            restult["msg"] = ""
            if testdata["checkpoint"] in restult["text"]:
                restult["result"] = "pass"
                self.log.info("用例测试结果:   %s---->%s" % (test_nub, restult["result"]))
            else:
                restult["result"] = "fail"
            return restult
        except Exception as msg:
            restult["msg"] = str(msg)
            return restult

    def covert_params(self, params, regex):
        map = {}
        if params != None:
            params_list = params.split(regex)
            for i in params_list:
                str = i.strip()
                value = str.split("=")
                map[value[0]] = value[1]
        return map

if __name__ == "__main__":
    opers = ExcelUtils('/Users/lvjing/PycharmProjects/ApiForPython/excel_file/apis.xls', 'api')
    data = opers.dict_data()
    send = RequestsUtils()
    s = requests.session()
    for i in range(len(data)):
        result = send.send_requests(s, data[i])
        print("-------------------------------")
