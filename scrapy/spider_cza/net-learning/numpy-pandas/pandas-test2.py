import numpy as np
import pandas as pd
"""
1、修改数据，可以直接在指定位置修改
2、可以重新添加新行新列
对丢失数据的处理：
1、df.dropna
axis=0按行
axis=1按列
how='any'默认，表示只要出现np.nan则直接删除
how='all'，表示只有当数据全部为np.nan的时候才会删除
2、df.fillna 
value='xxx'
3、df.isnull()
会打印是否缺失数据，缺失则打印出True
4、当数据表格很大时，我们使用如下方法，当至少有一个==True时，就会打印True
print(np.any(df.isnull()) == True)
"""
if __name__ == "__main__":
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,
                      columns=['A','B','C','D'])
    df.iloc[2,2] = 666
    df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101',periods=6))
    # print(df)

    df.iloc[0,1] = np.nan
    df.iloc[1,2] = np.nan
    print(df)
    print(df.dropna(axis=0, how='any'))  # how=['any','all']
    print(df.fillna(value='xxx'))
    print(df.isnull() == True)
    print(np.any(df.isnull()) == True)