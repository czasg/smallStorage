import numpy as np
import pandas as pd
"""
1、读取excel文件，可以通过sheet_name指定sheet页
df1 = pd.read_excel('database.xlsx', sheet_name='database')

统计与操作
1、count&unique&nunique
df[column].count()  # 统计该列的总行数
df[column].apply(lambda v: 1 if v=="value" else 0).sum()  # 统计该列中"value"出现的次数
df.groupby(column).sum()  
df[column].unique()  # set该列
df[column].nunique()  # 计算上述set的总数

2、获取列名
df.columns.values  # 返回列名
[column for column in df]  # 返回列名组成的list
list(df)  # 与上一步类似，返回列名组成的list

直接执行df[column]==value实际是做一个判断，返回TrueFalse
而df[df[column]==value]则是选出所有值为value的行
"""
