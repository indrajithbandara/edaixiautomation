#-*- coding:utf-8 -*-  
#enc oding:utf-8
#mysqldb      
import time, MySQLdb, sys  ,ConfigParser
import sys
import logging
import time
conf = ConfigParser.ConfigParser()
   
conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
mysqlhostname = conf.get("databaseconn", "mysqlhostname")
mysqlusername = conf.get("databaseconn", "mysqlusername")
mysqlpassword = conf.get("databaseconn", "mysqlpassword")
mysqldatabase = conf.get("databaseconn", "mysqldatabase")

#print mysqlhostname,mysqlusername,mysqlpassword, mysqldatabase
conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
global cursor
global ordersnnumber,huiyuannumber
cursor = conn.cursor()

def getordersn():
   n = cursor.execute("SELECT ordersn FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL order by id") 
   for row in cursor.fetchall():
      for ordersn in row: 
           return ordersn

    #return ordersn
#sglobal ordersn 
#print getordersn()           
#global ordersnnumber
ordersnnumber=str(getordersn())
        #print "the random ordersn  is ",ordersn  
#print ordersn
def gethuiyuanid():
    n = cursor.execute("SELECT cardno FROM ims_icard_card WHERE cardno IS NOT NULL order by id") 
    for row in cursor.fetchall():
      for huiyuanid in row: 
          return huiyuanid  
      
#print gethuiyuanid()  
huiyuannumber=str(gethuiyuanid())
print huiyuannumber

def getcloseconn():
   if cursor!="":
     cursor.close()
   elif conn!="":
     conn.close()

#global huiyuannumber        cursor.execute("UPDATE ims_washing_order SET fanxidan_id='0' WHERE ordersn='15072110393738'")
cursor.execute("UPDATE ims_washing_order SET status_delivery='1' WHERE ordersn='040300362586'")
conn.commit()

#huiyuannumber=str(huiyuanid)
        

#ordersnnumber=str(ordersn)
#huiyuannumber=str(huiyuanid)
#print ordersnnumber,huiyuannumber


#conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
#global cursor ,ordernumber
#cursor = conn.cursor()
#n = cursor.execute("SELECT ordersn ,username,tel,address FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL ORDER BY id") 
#for i in xrange(cursor.rowcount):
 #   ordersn ,username,tel,address = cursor.fetchone()
#getcloseconn() 

#print ordersn ,username,tel,address
#for row in cursor.fetchone():
#    for ordersn in row: 
#        ordersn 
#ordernumber=ordersn[1]
#print ordernumber

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
        
def Logger(message):
    logger=logging.getLogger()
    filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    #handler=logging.FileHandler("./log/"+filename+"error")
    handler=logging.FileHandler("C:/edaixi_testdata/"+filename+"error")
    #C:/edaixi_testdata/userdata_caiwu.conf
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.info(message)
       
def writeLog(message):
    logger=logging.getLogger()
    filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    #handler=logging.FileHandler("./log/"+filename+"error")
    handler=logging.FileHandler("C:/edaixi_testdata/"+filename+"error")
    #C:/edaixi_testdata/userdata_caiwu.conf
    logger.addHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.info(message)

if __name__ == '__main__': 
    writeLog("hello")



