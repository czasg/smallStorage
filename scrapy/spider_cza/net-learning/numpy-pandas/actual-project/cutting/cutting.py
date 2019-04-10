import os
import pandas as pd


class cutting(object):
    def __init__(self, sourceFile, resFile):
        self.df = pd.read_excel(sourceFile)
        self.resFile = resFile
        self.reslist = []
    def process(self):
        def func(df, columns):
            res = {}
            for column in columns:
                res.setdefault(column,df[column])
            print(res)
        columns = self.df.columns.values
        self.df.apply(func, axis=1, args=(columns,))
        pass

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = (os.sep).join([current_path, 'source', 'source_test.xls'])
    resFilename = (os.sep).join([current_path, 'result', 'result.xls'])
    o = cutting(file_path,resFilename).process()
    pass