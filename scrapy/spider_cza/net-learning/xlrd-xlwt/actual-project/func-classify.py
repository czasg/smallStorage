import os
import xlrd,xlwt

class classify(object):
    def __init__(self, filepath, num, resFile):
        self.source = xlrd.open_workbook(filepath)
        self.source_sheet = self.source.sheet_by_index(num)
        self.source_nrows = self.source_sheet.nrows
        # self.result_sheet = self.get_result_sheet()
        self.result = xlwt.Workbook()
        self.company_statistics = {}
        self.column_index = {}
        self.flas = {}
        self.resFile = resFile

    def get_column_index(self):
        for index, column in enumerate(self.source_sheet.row_values(0)):
            self.column_index.setdefault(column, index)
        # self.column_index = sorted(self.column_index, key=lambda x:x[1])
    def get_company_statistics(self):
        index = self.column_index["责任方"]
        for i in range(1, self.source_nrows):
            company = self.source_sheet.row_values(i)[index]
            self.company_statistics[company] = self.company_statistics.get(company, 0) + 1
        # self.company_statistics = sorted(self.company_statistics, key=lambda x:x[1], reverse=True)
    def get_result_sheet(self):
        dict = {}
        print(self.company_statistics)
        for i in self.company_statistics.keys():
            dict[i] = self.result.add_sheet(i)
            # list.append(self.result.add_sheet(i))
        dict["统计"] = self.result.add_sheet("统计")
        return dict
    def process(self):
        self.get_column_index()
        self.get_company_statistics()
        self.result_sheet = self.get_result_sheet()
        self._process()
        self.save()
    def _process(self):
        self.process_company_sheet()
        self.process_statistics_sheet()
    def process_company_sheet(self):
        index = self.column_index["责任方"]
        for i in range(1, self.source_nrows):
            row_data = self.source_sheet.row_values(i)
            company = row_data[index]
            resultsheet = self.result_sheet[company]
            self.flas[company] = self.flas.get(company,-1) + 1
            for c,v in enumerate(row_data):
                resultsheet.write(self.flas[company], c, v)
    def process_statistics_sheet(self):
        index = 1
        sheet = self.result_sheet["统计"]
        sheet.write(0, 0, "公司")
        sheet.write(0, 1, "统计")
        for company,statistic in sorted(self.company_statistics.items(), key=lambda x:x[1], reverse=True):
            sheet.write(index, 0, company)
            sheet.write(index, 1, statistic)
            index += 1
    def save(self):
        self.result.save(self.resFile)

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = (os.sep).join([current_path, 'source', 'source_test.xls'])
    resFilename = (os.sep).join([current_path, 'result','result.xlsx'])
    o = classify(file_path, 0, resFilename).process()
    print('done')