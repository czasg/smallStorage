import numpy as np
import pandas as pd
"""
1、for i,j in sorted(fd.items(), key=lambda x:x[0], reverse=False)
2、line=line.decode('utf-8', 'ignore')  或者  line=line.encode('utf-8', 'ignore')
3、dict[cza] = dict.get(cza, 0) + 1
4、data['pre']=data['pre'].apply(lambda x:str(round(x/2))+'%')  #对某一列进行计算
5、data=data[~(data['SN'].isin(list))].reset_index(drop=True)  # 传说中的过滤一把手啊
6、data['xxx']=data['xxx'].replace(list1, list2)
7、data.rename(columns={'old':'new'}, inplace=True)
8、pd.set_option('display.max_colwidth', 100)
9、data['ERROR'].unique()
10、df.groupby('SN').sum()  # 是否需要label变成索引，可以通过参数as_index=False设置
notebook、df['A'].isin(list)  #这里就是针对A列，我们判断并保留值在这list中的各行。返回TrueFalse
12、res = re.findall('(简历|分工)(.*?)(?=简历|分工|$)', source)  # dict(res) 其中res必须是[(x,y),(x,y)]的结构
13、使用apply(func, axis=1)，默认传入的参数就是该df，但需要加如参数axis=1
apply(func, axis=1, args=(2,))  # 每次取一行数据传入，还可以额外传入参数
apply(func, axis=0, args=(2,))  # 每次取一列数据传入，还可以额外传入参数

# 使用pandas进行excel操作
writer = pd.ExcelWriter('xxx.xlsx')  # 定义一个可以多页写的表格
dataframe.to_excel(writer, sheet_name='cza', index=False, encoding='utf-8')  # 定义sheet页，index表示是否写入排序
write.save()
ExcelWriter一般常用的方法有：
with pd.ExcelWriter(resFile) as writer: 
df.to_excel(writer, sheet_name=name, index=True)  # index表示是否需要带上索引
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