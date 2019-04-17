import xlrd, xlwt


if __name__ == "__main__":
    filename = 'mergeCells.xlsx'
    r = xlrd.open_workbook(filename)
    sheet = r.sheet_by_name("czaOrz")
    print(sheet.merged_cells)
    print(sheet.row(0))