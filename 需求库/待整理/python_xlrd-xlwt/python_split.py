#encoding = utf-8
import os,sys,xlrd,xlwt,time
from xlutils.copy import copy
from lxml import etree

result_file_path = u'C:\\Users\\Administrator\\Desktop\\python_test\\python_excel_xml_mass_test\\result\\result.xls'
source_file_path = u'C:\\Users\\Administrator\\Desktop\\python_test\\python_excel_xml_mass_test\\source\\source_test.xls'
xml_path = u'C:\\Users\\Administrator\\Desktop\\python_test\\python_excel_xml_mass_test\\info.xml'

cloumn = {u'责任方':-1,u'时间':-1} #value is index in source
company = {u'中软':0,u'诚迈':0,u'BJC':0} #value is all of counts about YuQing

def open_xml(xml_path):
    tree = etree.parse(xml_path)
    return tree

def open_file(path):
    temp = xlrd.open_workbook(path)
    return temp

def get_time(ndoe_name,node_root):
    temp_time = node_root.find(ndoe_name).text
    return temp_time

def get_time_from_xml(xml):
    list = []
    root = xml.getroot()
    start_time = get_time('start_time',root)
    end_time = get_time('end_time',root)
    list.append(start_time)
    list.append(end_time)
    print('Get time success! it is: ',start_time,end_time)
    return list

def column_get_index(source_file):
    source_sheet0 = source_file.sheet_by_index(0)
    for s0Index,s0Column in enumerate(source_sheet0.row_values(0)):
        for column_index,column_key in enumerate(cloumn):
            if s0Column == column_key:
                cloumn[column_key] = s0Index      
    print('column get index Success!')

def company_total(source_file):
    source_sheet0 = source_file.sheet_by_index(0)
    for i in range(1,source_sheet0.nrows):
        for s0Index,s0Column in enumerate(source_sheet0.row_values(i)):
            if s0Index == cloumn['责任方']:
                for company_index,company_key in enumerate(company):
                    if company_key == s0Column:
                        company[company_key] += 1
    print('company total Success!')

def get_result_sheet(wb):
    list = []
    for i in range(4):
        list.append(wb.get_sheet(i))
    return list

def summary_to_result3(resultSheet):
    result_sheet_read_3 = (open_file(result_file_path)).sheet_by_index(3)
    result_sheet_3 = resultSheet[3]
    for i in range(1,result_sheet_read_3.nrows):
        for r3Index,r3Cloumn in enumerate(result_sheet_read_3.row_values(i)):
            for company_index,company_key in enumerate(company):
                if company_key == r3Cloumn:
                    result_sheet_3.write(i,1,company[company_key])

def split_info_source_to_result(source_file,result_file,result_sheet):
    summary_to_result3(result_sheet)
    a = b = c = 1
    for i in range(1,(source_file.sheet_by_index(0)).nrows):
        source_rowValue = (source_file.sheet_by_index(0)).row_values(i)
        for s0Index,s0Column in enumerate(source_rowValue):
            for j in range(3):
                if result_file.sheet_names()[j] == s0Column:
                    for k in range((source_file.sheet_by_index(0)).ncols):
                        for s0Index_1,s0Column_1 in enumerate(source_rowValue):
                            if k == s0Index_1:
                                if j == 0:
                                    result_sheet[j].write(a,k,s0Column_1)
                                elif j == 1:
                                    result_sheet[j].write(b,k,s0Column_1)
                                elif j == 2:
                                    result_sheet[j].write(c,k,s0Column_1)
                    if j == 0:
                        a += 1
                    elif j == 1:
                        b += 1
                    elif j == 2:
                        c += 1
    print('split information from source to result, Success!')

def main():
    #init xml/source_file/result_file
    xml = open_xml(xml_path)
    source_file = open_file(source_file_path)
    result_file = open_file(result_file_path)

    #get start time and end time from XML
    aim_time = get_time_from_xml(xml) #this is a list

    #add value for Dictionary cloumn and company
    column_get_index(source_file)
    company_total(source_file)
    
    #get result.xls sheet, there is adding four sheets to a list
    wb = copy(result_file)
    result_sheet = get_result_sheet(wb) #this is a list

    #split infomation from source to result
    split_info_source_to_result(source_file,result_file,result_sheet)

    #save the result
    wb.save(result_file_path)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('succeed! Using: %s' % (end_time - start_time))