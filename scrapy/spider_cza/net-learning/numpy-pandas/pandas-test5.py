import numpy as np
import pandas as pd
"""
1、for i,j in sorted(fd.items(), key=lambda x:x[0], reverse=False)
2、line=line.decode('utf-8', 'ignore')  或者  line=line.encode('utf-8', 'ignore')
3、dict[cza] = dict.get(cza, 0) + 1
4、data['pre']=data['pre'].apply(lambda x:str(round(x/2))+'%')  #对某一列进行计算
5、data=data[~(data['SN'].isin(list))].reset_index(drop=True)
6、data['xxx']=data['xxx'].replace(list1, list2)
7、data.rename(columns={'old':'new'}, inplace=True)
8、pd.set_option('display.max_colwidth', 100)
9、data['ERROR'].unique()
10、df.groupby('SN').sum()
11、df['A'].isin(list)  #这里就是针对A列，我们判断并保留值在这list中的各行

# 使用pandas进行excel操作
writer = pd.ExcelWriter('xxx.xlsx')  # 定义一个可以多页写的表格
dataframe.to_excel(writer, sheet_name='cza', index=False, encoding='utf-8')  # 定义sheet页，index表示是否写入排序
write.save()
"""
if __name__ == "__main__":
    left = pd.DataFrame({"key":["k0","k1","k2","k3"],
                         "A":["A0","A1","A2","A3"],
                         "B":["B0","B1","B2","B3"]})
    right = pd.DataFrame({"key": ["k0", "k1", "k2", "k3"],
                         "C": ["C0", "C1", "C2", "C3"],
                         "D": ["D0", "D1", "D2", "D3"]})
    # res = pd.merge(left, right, on='key')  # on是指定基于哪一个columns进行合并
    # print(res)

    left1 = pd.DataFrame({"key1": ["k0", "k1", "k2", "k3"],
                          "key2": ["k0", "k1", "k2", "k3"],
                         "A": ["A0", "A1", "A2", "A3"],
                         "B": ["B0", "B1", "B2", "B3"]})
    right1 = pd.DataFrame({"key1": ["k0", "k1", "k2", "k3"],
                           "key2": ["k0", "k1", "k2", "k3"],
                          "C": ["C0", "C1", "C2", "C3"],
                          "D": ["D0", "D1", "D2", "D3"]})
    res = pd.merge(left1, right1, on=['key1', 'key2'])
    print(res)