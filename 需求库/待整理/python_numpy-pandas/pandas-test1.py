import pandas as pd
import numpy as np
"""
date_range: 创建时间数据，periods=6表示往后推6天
DataFrame: np数据转化为表格型数据，index->行，columns->列
loc: 以元素的值作为索引
iloc: 以下标作为索引
ix: 混合索引
df.index
df.columns
df.values
"""
if __name__ =="__main__":
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,
                      columns=["A","B","C","D"])
    print(df, '\n')
    print(df[:3])# print(df["A"])# print(df)
    # print(df.loc[:'20130105', ['A','B']])# print(df.loc['20130102':'20130105'])
    # print(df.iloc[3:5,1:3])
    # print(df.ix[:3, ['A','B']])
    # print(df[df.A > 8])
    # print(df.values)#df.columns#df.index