import xlrd
from xlutils.copy import copy
from utils.logger import Log


class ExcelUtils(object):
    log = Log()

    def __init__(self, excelName, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelName)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        self.excelName = excelName

    def dict_data(self):
        if self.rowNum <= 1:
            self.log.info('excel文件总行数小于1')
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum - 1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

    # 写入数据, 写入excel,row,col,value
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.excelName)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.excelName)


if __name__ == '__main__':
    opers = ExcelUtils('/Users/lvjing/PycharmProjects/ApiForPython/excel_file/apis.xlsx', 'api')
    data = opers.dict_data()
    print(data)
    for i in data:
        print(i)
