#-*- coding:utf-8 -*-  
#enc oding:utf-8
#mysqldb      
import time, MySQLdb, sys   
import sys
import threading
import paramiko
import socket
import random
#10.66.110.220
#connect   115.159.23.93
'''
try:
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    ssh.connect("115.159.23.93", port=int(52087), username="ubnutu", password="PR4haxlB4zTabT9ZsD")
    #ssh.exec_command(comm['alter_auth'])
    #ssh.exec_command(comm['exec_program'])
    
except Exception,e:
    print 'chang file auth or execute the file failed:',e
ssh.close()
    '''
#conn=MySQLdb.connect(host="54.223.190.242",user="root",passwd="wwefa232afYUY",db="wuliu03",charset="utf8")  
#conn = MySQLdb.connect(sshhost = '115.159.23.93', sshuser = 'ubuntu', sshpasswd = 'PR4haxlB4zTabT9ZsD', host = '10.66.110.220:3306', user = 'root', passwd = 'wwefa232afYUY', db = 'rongchain03')  
#conn=MySQLdb.connect(host="testdb.edaixi.cn",user="test",passwd="test",db="rongchain03",charset="utf8") 
file=open('C:/edaixi_testdata/userinterface_data.txt','r')
dictobj={}
for line in file:
    key,value=line.split(",")
    dictobj[key]=value
    
print dictobj
print dictobj["hearurl"].strip('\n')+dictobj["contenturl"]
print dictobj["contenturl"]
print dictobj["contenturl"]
print dictobj["mysqlhostname"].strip('\n')
print dictobj["mysqlusername"].strip('\n')
print dictobj["mysqlpassword"].strip('\n')

mysqlhostname=dictobj["mysqlhostname"].strip('\n')
mysqlusername=dictobj["mysqlusername"].strip('\n')
mysqlpassword=dictobj["mysqlpassword"].strip('\n')
mysqldatabase=dictobj["mysqldatabase"].strip('\n')


conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
cursor = conn.cursor()
n = cursor.execute("SELECT ordersn FROM ims_washing_order ORDER BY id") 
for row in cursor.fetchall():
    for rowbagsn in row:      
        print "===rowbagsn is ",rowbagsn  
print rowbagsn


n = cursor.execute("SELECT ordersn FROM ims_washing_order WHERE status_delivery=3 and fanxidan_id=0")      

print n
listbagsn =[]
for i in xrange(cursor.rowcount):
    row= cursor.fetchone()
    #print row[row.find()] str(row)
    rowstr =''.join(row)
    #print rowstr
    listbagsn.append(rowstr)
    #print row
print "00000000000000",listbagsn
print tuple(listbagsn)
#for row in cursor.fetchall():
    #print row


n = cursor.execute("SELECT ordersn FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL order by id") 
for row in cursor.fetchall():
    for rowbagsn in row:      
        print "===rowbagsn is ",rowbagsn  
print rowbagsn
        
        
if 'E0000125599' in listbagsn:
   print "it is exsit on mysql order table."
else:
   print "it is not exsit on mysql order table"
                                    
'''                                  
for row in cursor.fetchall():
     
    for r in row:      
        print r,     
print ""  
'''
cursor.close()
conn.close()
file.close()
print random.randint(0,999)+random.randint(0,999)
'''
cursor.execute("SELECT id, name FROM `table`")
for i in xrange(cursor.rowcount):
    id, name = cursor.fetchone()
    print id, name


cursor.execute("SELECT id, name FROM `table`")
result = cursor.fetchmany()
while result:
    for id, name in result:
        print id, name
    result = cursor.fetchmany()


cursor.execute("SELECT id, name FROM `table`")
for id, name in cursor.fetchall():
    print id, name
    
'''
theTuple = ('a','b','c')
if 'a' in theTuple:
    print 'a in the Tuple'
    
    
theList = ['a','b','c']
if 'a' in theList:
    print 'a in the list'

if 'd' not in theList:
    print 'd is not in the list'