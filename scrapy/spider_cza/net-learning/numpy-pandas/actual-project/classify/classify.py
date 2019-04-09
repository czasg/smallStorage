import os
import numpy as np
import pandas as pd

class classify(object):
    def __init__(self, sourceFile, resFile):
        self.df = pd.read_excel(sourceFile)
        self.resFile = resFile

    def process(self):
        self.df["count"] = 1
        print(self.df.groupby("责任方").sum())
        pass
    def save(self):
        self.df.to_excel(self.resFile)

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    file_path = (os.sep).join([current_path, 'source', 'source_test.xls'])
    resFilename = (os.sep).join([current_path, 'result', 'result.xls'])
    o = classify(file_path,resFilename).process()
    pass