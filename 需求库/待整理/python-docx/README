docx模块针对表格table：
读：表格关健属性有：表格整体、行、列、单元格、单元格的属性(文本内容)、合并单元格的特征
写：pass

加载docx.Document模块，获取doc句柄
doc = docx.Document(fileName)/doc = docx.Document()  -> doc.save(fileName)
打开指定文件/打开空文件，保存指定文件（必须指定）
其中输入可以是文件路径，也可以是string、文件对象（不支持bytes）

tables = doc.tables  # 获取所有表格，返回获取到的Table对象-list集

rows = tables[0].rows  # 获取该表中所有行，返回一个_Rows对象
columns = tables[0].columns  # 获取该表中所有的列，_Columns对象

row_cells = rows[0].cells  # 获取一行中所有单元格，返回获取到的单元格对象-tuple集
row_cells = tables[0].row_cells(index)
col_cells = columns[0].cells  # 获取一列中所有单元格，返回获取到的单元格对象-tuple集
col_cells = tables[0].column_cells(index)

row_cells[0].text  # 获取该单元格的文本
row_cells[0].width  # 获取该单元格宽度
row_cells[0].paragraphs  # 以'\n'切割该单元格，每个单元格可以进行 .text 操作，如下
    for p in cell.paragraphs:   # 首先会以'\n'切割此单元格的内容，每一个p表示一个字单元格对象，可用p.text获取文本
        p.text

row_cells[0].text中若文本为空则返回 ''

合并单元格的特征：
多个单元格合并后，每个单元格仍旧存在，且内存指向合并后的单元格
即合并三个单元格后，此三个单元格仍旧存在，且均指向该合并后的单元格，若对该三个单元格各写入111，最后结果为'111'



todo 再写两个举证分析函数。即行只管横的逻辑，列就只管竖的逻辑，不要影响混合矩阵
todo 全部都是1的情况，会出现bug，如何避免？

