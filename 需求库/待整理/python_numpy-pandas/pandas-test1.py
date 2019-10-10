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

np.random.seed(1234)
d1 = pd.Series(2*np.random.normal(size = 100)+3)
d2 = np.random.f(2,4,size = 100)
d3 = np.random.randint(1,100,size = 100)
d1.count() #非空元素计算
d1.min() #最小值
d1.max() #最大值
d1.idxmin() #最小值的位置，类似于R中的which.min函数
d1.idxmax() #最大值的位置，类似于R中的which.max函数
d1.quantile(0.1) #10%分位数
d1.sum() #求和
d1.mean() #均值
d1.median() #中位数
d1.mode() #众数
d1.var() #方差
d1.std() #标准差
d1.mad() #平均绝对偏差
d1.skew() #偏度
d1.kurt() #峰度
d1.describe() #一次性输出多个描述性统计指标
"""
if __name__ =="__main__":
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,
                      columns=["A","B","C","D"])
    print(df, '\n')
    print(df[:3])# print(df["A"])# print(df)
    print(df.loc[:'20130105', ['A','B']])# print(df.loc['20130102':'20130105'])
    print(df.iloc[3:5,1:3])
    # print(df.ix[:3, ['A','B']])
    print(df[df.A > 8])
    print(df.values)#df.columns#df.index
    print(df.describe())
    print(np.array(df.describe()))

    # np.random.seed(1234)
    # d1 = pd.Series(2 * np.random.normal(size=100) + 3)
    # d2 = np.random.f(2, 4, size=100)
    # d3 = np.random.randint(1, 100, size=100)
    # print(d1)
    # print(d1.describe())