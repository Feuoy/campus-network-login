#coding:utf-8

import csv
import pandas as pd
import os

csv_file = open('es_list_.csv')    #打开csv文件
csv_reader_lines = csv.reader(csv_file)   #逐行读取csv文件

data = []    #创建列表准备接收csv各行数据
row = 0
for one_line in csv_reader_lines:
    data.append(one_line)    #将读取的csv分行数据按行存入列表‘data’
    row = row + 1    #统计行数
csv_file.close()

valid_account = []
i = 0
while i < row:
    # X结尾
    if (data[i][2][-1]) == 'X':
        valid_account.append(data[i])
    i = i + 1

# print(data)
# print(id_number) 
# print(len(data))
# print(len(id_number))

valid_data = pd.DataFrame(data=valid_account)  # 数据有三列，列名分别为one,two,three
print(valid_data)
valid_data.to_csv('result_endWithX.csv', encoding='gbk')

print(valid_data[0][0])
print(valid_data[1][0])
print(valid_data[2][0][-8:])