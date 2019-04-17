import os
import xlrd, xlwt
from xlutils.copy import copy

from .path_func import to_path


class ExcelWrite(object):
    def __init__(self, fileName, sheetName, path=''):
        self.fileName = self.check_suffix(fileName)
        self.sheetName = sheetName
        self.save_path = to_path(path, self.fileName) if path else self.fileName
        self.row_index = 0
        self.col_index = 0
        self.xlsWB = copy(self.load_excel(self.save_path, sheetName))
        try:
            self.sheet = self.xlsWB.get_sheet(sheetName)
        except:
            self.sheet = self.xlsWB.add_sheet(sheetName)

    @staticmethod
    def load_excel(filePath, sheetName):
        check = os.path.exists(filePath)
        if check:
            print("文件已存在，使用默认文件进行读写")
            return xlrd.open_workbook(filePath)
        else:
            print("文件不存在，新建中...")
            try:
                xlwt.Workbook().add_sheet(sheetName).save()
            except:
                raise Exception("创建出错！")
            else:
                print("新建成功！")

    def check_suffix(self, fileName):
        if '.' in fileName:
            if not fileName.endswith((".xls", ".xlsx")):
                raise ValueError("请输入正确的文件名，如'xxx'或'xxx.xls'或'xxx.xlsx'")
            else:
                return fileName
        else:
            return fileName + ".xls"

    def cursor_move(self, right=False, left=False, up=False, down=False):
        if right:
            self.col_index += 1
        if left:
            self.col_index -= 1
        if up:
            self.row_index -= 1
        if down:
            self.row_index += 1

    def cursor_jump(self, row_index, col_index):
        self.row_index = row_index
        self.col_index = col_index

    def save(self):
        self.xlsWB.save()










if __name__ == "__main__":
    pass