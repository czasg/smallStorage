from docx import Document

"""
simulate func of sheet.merged_cells in xlrd -> [(4,5,2,4), (5,6,2,4)] -> 0start,row4-5,col2-4
aim is an interface: table.merged_cells
"""


def test():
    doc = Document('text.docx')
    table = doc.tables[0]
    # nrows = len(table.rows[0].cells)
    # ncols = len(table.columns[0].cells)
    nrows = len(table.row_cells(0))
    ncols = len(table.column_cells(0))
    print(nrows, ncols)
    # for i in range(ncols):
    #     for j in range(nrows):
    #         table.cell(i, j).text = table.cell(i, j).text + 'cza'
    #         print(table.cell(i,j), i, j, table.cell(i,j).text)
    pool = []
    # for i in range(ncols):
    #     for cell in table.row_cells(i):
    #         if cell not in pool:
    #             pool.append(cell)
    #             cell.text += cell.text + 'cza'
    pool = []
    for i in range(nrows):
        print(table.column_cells(i))
        # for cell in table.column_cells(i):
        #     print(cell)





if __name__ == "__main__":
    test()
