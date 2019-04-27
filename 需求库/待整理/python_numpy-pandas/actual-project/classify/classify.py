import os
import numpy as np
import pandas as pd


class classify(object):
    def __init__(self, sourceFile, resFile):
        self.df = pd.read_excel(sourceFile)
        self.resFile = resFile
        self.reslist = []
    def get_company_to_dict(self):
        res = {}
        def func(df):
            res[df["责任方"]] = res.get(df["责任方"], 0) + 1
        self.df.apply(func, axis=1)
        return res
    def process(self):
        self.get_company_classify()
        self.get_company_statistics()
        self.save_excel_writer()
    def get_company_classify(self):
        companys = self.df["责任方"].unique()
        for company in companys:
            df = self.df[self.df["责任方"]==company].reset_index(drop=True)
            self.reslist.append(tuple((company,df)))
    def get_company_statistics(self):
        self.df["count"] = 1
        df = self.df.groupby("责任方", as_index=False).sum()[["责任方", "count"]]
        self.reslist.append(tuple(("统计", df)))
    def save(self):
        self.df.to_excel(self.resFile)
    def save_excel_writer(self):
        with pd.ExcelWriter(self.resFile) as writer:
            for sheetname,res in self.reslist:
                res.to_excel(writer, sheet_name=sheetname,index=True)

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = (os.sep).join([current_path, 'source', 'source_test.xls'])
    resFilename = (os.sep).join([current_path, 'result', 'result.xls'])
    o = classify(file_path,resFilename).process()
    pass