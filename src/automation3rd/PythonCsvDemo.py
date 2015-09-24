#!/usr/lib/python2.7
# -*- coding: utf-8 -*-

import csv

# with open('C:\edaixi_testdata\wechattestdata.csv','rb') as f:
#     reader = csv.reader(f)
# for row in reader:
#     print row
#     reader.close() 
    
    
csvfile = file('C:\edaixi_testdata\wechattestdata.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print line

print reader
print line[1]

csvfile.close() 


csvfile = file('C:\edaixi_testdata\wechattestdata.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]
writer.writerows(data)

csvfile.close()


