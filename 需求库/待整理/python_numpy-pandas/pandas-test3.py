import numpy as np
import pandas as pd
"""
1、df.sort_index(axis=1, ascending=False)
axis=1 按列进行排序   
ascending=False 升序
2、df.sort_value
"""
if __name__ == "__main__":
    dates = pd.date_range('20130101',periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,
                      columns=['A','B','C','D'])
    print(df.sort_index(axis=0, ascending=False))
    # print(df.sort_values(by='B', ascending=False))