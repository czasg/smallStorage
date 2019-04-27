import numpy as np
import pandas as pd


if __name__ == "__main__":
    df1 = pd.read_excel('database.xlsx', sheet_name='database')
    head = df1.head()
    cza = df1["性别"]
    print(cza)
    print(df1.loc[:4,["姓名","性别"]])

    # df2 = pd.read_excel('database.xlsx', sheet_name="czaOrz")
    # print(df2)