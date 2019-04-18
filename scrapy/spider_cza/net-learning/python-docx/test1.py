from docx import Document


doc = Document('database.docx')
table = doc.tables
rows = table[0].rows  # cell object
cols = rows[0].cells
# cell = cols[0].text
# columns = table[0].columns
row_cells = table[0].row_cells(0)

# print(doc)
print(table)
print(rows)
print(cols)
# print(cell)
# print(columns, len(columns))
# for column in columns:
#     print(column.cells)
#     for col in column.cells:
#         print(col.text)
print(row_cells)
# cols is different from row_cells???
# for i in cols:
#     print(i.text)
#
# for i in row_cells:
#     print(i.text)
