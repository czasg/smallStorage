import numpy as np
import pandas as pd

"""
1、df.concat([df1,df2..], axis=0, ignore_index=True)
axis=0 竖向合并
axis=1 横向合并
ignore_index  忽略原有的索引，重新排序
2、join参数
join='outer' 不等合并，空缺地方使用NAN来填补
join='inner' 去异留同
join='left' 
join='right' 
3、join_axes参数, join_axes=[df1.index]
按照df1.index进行合并，只考虑与df1.index相同的
4、df.append

"""
if __name__ == "__main__":
    df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
    df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
    df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
    # concat
    # res = pd.concat([df1,df2,df3], axis=0, ignore_index=True) # 0竖向合并， 1是横向合并
    # print(res)

    df4 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
    df5 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
    # res = pd.concat([df4,df5], join='outer')  # 没有的地方会用NaN填充
    # print(res) # 默认的方式，
    # res = pd.concat([df4, df5], join='inner')  # 没有的地方会用NaN填充
    # print(res)

    # res = pd.concat([df4, df5], axis=1, join_axes=[df4.index])
    # print(res)  # 指定合并所要的index，那么会按照他的标准合并，无则为NaN

    s1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
    res = df1.append(s1, ignore_index=True)  # axis=1是横向加数据，默认是0，即竖向
    # print(res)
    # print(df1.append([df2,df3]))


