from jsonpath import jsonpath
from utils.excelUtils import ExcelUtils

"""
 通过jsonpath提取校验的值
"""


class CheckPointUtils(object):

    def __init__(self, excel_file, sheet_name):
        self.read_excel = ExcelUtils(excel_file, sheet_name)

    # 通过case_id获取该case_id的整行数据
    def get_case_data(self, dependence_id):
        result_data = self.read_excel.dict_data()
        data = ''
        for i in result_data:
            if dependence_id != '' and i["id"] == dependence_id:
                data = i
        return data

    # 根据传入的字段,获取字段的值
    def get_field_value(self, dependence_id, field):
        data = self.get_case_data(dependence_id)
        dependence_data = ''
        if dependence_id != '' and field != '':
            dependence_data = data[field]
        return dependence_data

    # 通过jsonpath表达式获取校验值
    def get_check_value(self, response_result, dependence_id, field):
        dependence_data = self.get_field_value(dependence_id, field)
        result = jsonpath(response_result, dependence_data)
        return result
