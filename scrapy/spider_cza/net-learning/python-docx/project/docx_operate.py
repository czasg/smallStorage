from docx import Document
import numpy as np

def get_document(file):
    return Document(str)

class _Table(object):
    def __init__(self, table):
        self.table = table  # 5,4
        self.nrows = len(self.table.column_cells(0))
        self.ncols = len(self.table.row_cells(0))

    @property
    def merged_cells(self):
        row_mat = self.get_matrix(row=True)
        col_mat = self.get_matrix(col=True).T
        return self.chech_merge_cells(row_mat, col_mat)  # list

    def get_matrix(self, row=False, col=False):
        father_num,child_num = 0,0
        get_data = lambda x:x
        if row:
            father_num = self.nrows
            child_num = self.ncols
            get_data = self.table.row_cells
        elif col:
            father_num = self.ncols
            child_num = self.nrows
            get_data = self.table.column_cells
        res_list = []
        for i in range(father_num):
            all_cells = get_data(i)
            all_set = set(all_cells)
            res = np.zeros(child_num)
            if len(all_set) == child_num:
                res_list.append(res)
                continue
            pool = []
            flag = 1
            for i, cell in enumerate(all_cells):
                if cell in pool:
                    res[i] += flag
                    res[i - 1] += flag
                    flag += 1
                    continue
                pool.append(cell)
            res_list.append(res)
        return np.array(res_list)

    def chech_merge_cells(self, row_mat, col_mat):
        fusion = row_mat * col_mat
        # test_list = [fusion, row_mat, col_mat]
        test_list = [col_mat]
        result = []
        for mat in test_list:  # todo
            res = []
            index = 1
            while True:
                if index in mat:
                    ix = np.isin(mat, index)
                    x, y = np.where(ix)
                    res.append((x[0], x[-1], y[0], y[-1]))
                    index += 1
                else:
                    break
            result += res
        return result



class DocxReader(object):
    def __init__(self, document):
        self.document = document
        self.tables = self.document.tables
        self.tables_res = []

    @classmethod
    def from_str(cls, string=None, path=None):
        file = string if string else path
        if file:
            return cls(get_document(file))
        else:
            raise Exception("None thing to reading")

    def table_manage(self, ):
        pass

    def table2dict(self, ):
        # for table in self.tables:
        #     res = {}
        pass


if __name__ == "__main__":
    doc = Document('text.docx')
    table = doc.tables[0]
    print(_Table(table).merged_cells)

