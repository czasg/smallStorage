from docx import Document
import numpy as np  # np.array(list)

doc = Document('text.docx')
table = doc.tables[0]
nrows = len(table.column_cells(0))
ncols = len(table.row_cells(0))  # print(nrows,ncols) 4-3
print(nrows,ncols)
res_list = []
for i in range(nrows):  #
    row_cells = table.row_cells(i)
    row_set = set(row_cells)
    res = np.zeros(ncols)
    if len(row_set) == ncols:
        res_list.append(res)
        continue
    pool = []
    flag = 1
    for i,cell in enumerate(row_cells):
        if cell in pool:
            res[i] += flag
            res[i-1] += flag
            flag += 1
            continue
        pool.append(cell)
    res_list.append(res)
row_matrix = np.array(res_list)
# print(row_matrix)


res_list = []
for i in range(ncols):  #
    col_cells = table.column_cells(i)
    col_set = set(col_cells)
    res = np.zeros(nrows)
    if len(col_set) == nrows:
        res_list.append(res)
        continue
    pool = []
    flag = 1
    for i,cell in enumerate(col_cells):
        if cell in pool:
            res[i] += flag
            res[i-1] += flag
            flag += 1
            continue
        pool.append(cell)
    res_list.append(res)
col_matrix = np.array(res_list).T
# print(col_matrix)

res = row_matrix*col_matrix
print(res, type(res))

# ix = np.isin(res, 1)
# print(ix)
# x,y = np.where(ix)
# print(x,y)
# print([(x[0],y[0]),(x[-1]),y[-1]])
index = 1
cza = []
while True:
    if index in res:
        ix = np.isin(res, index)
        x,y = np.where(ix)
        print(x,y)
        cza.append((x[0], x[-1], y[0], y[-1]))
        index += 1
    else:
        break
print(cza)





# print(np.where(res>1))
# print(np.where(res>1, 0, res))




# resl = res.tolist()
# res2 = res.T.tolist()
# print(res.T,res2)
# pool = set()
# for list in resl:
#     pool = pool.union(set(list))
# print(pool, type(pool))
#
# for i in range(len(pool)):




