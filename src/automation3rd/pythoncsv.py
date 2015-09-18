# coding: utf-8

import csv

csvfile = file('csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]
writer.writerows(data)

csvfile.close()


csvfile = file('csv_test.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print line

csvfile.close() 



#with open('egg2.csv', 'wb') as csvfile:
# spamwriter = csv.writer(csvfile,dialect='excel')
# spamwriter.writerow(['a', '1', '1', '2', '2'])
# spamwriter.writerow(['b', '3', '3', '6', '4'])
# spamwriter.writerow(['c', '7', '7', '10', '4'])
# spamwriter.writerow(['d', '11','11','11', '1'])
# spamwriter.writerow(['e', '12','12','14', '3'])

# 
# with open('egg2.csv', 'wb') as csvfile:
# spamwriter = csv.writer(csvfile, delimiter=' ',
# quotechar='|', quoting=csv.QUOTE_MINIMAL)
# spamwriter.writerow(['a', '1', '1', '2', '2'])
# spamwriter.writerow(['b', '3', '3', '6', '4'])
# spamwriter.writerow(['c', '7', '7', '10', '4'])
# spamwriter.writerow(['d', '11','11','11', '1'])
# spamwriter.writerow(['e', '12','12','14', '3'])


