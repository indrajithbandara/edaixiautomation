# -*- coding: utf-8 -*-

from time import strftime, localtime
from datetime import timedelta, date
import calendar
import time,random
import datetime
import ConfigParser,MySQLdb

global jiagongdianjiesuan_balancetab
jiagongdianjiesuan_balancetab=str(9)
ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

def makeNewIdentifiedCardId():
    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                        random.randint(01,99),
                                        random.randint(01,99),
                                        random.randint(t - 80, t - 18),
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(1,999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' %(x, LAST[y % 11])


conf = ConfigParser.ConfigParser()
conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
global CAIWU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
mysqlhostname = conf.get("databaseconn", "mysqlhostname")
mysqlusername = conf.get("databaseconn", "mysqlusername")
mysqlpassword = conf.get("databaseconn", "mysqlpassword")
mysqldatabase = conf.get("databaseconn", "mysqlrongchangdb")
print mysqlhostname, mysqlusername, mysqlpassword, mysqldatabase

conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
global cursor
global ordersnnumber,fanidnumber
cursor = conn.cursor()

def getordersn():
   n = cursor.execute("SELECT ordersn FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
   for row in cursor.fetchall():
      for ordersn in row: 
           return ordersn

    #return ordersn
#sglobal ordersn 
#print getordersn()           
#global ordersnnumber
#ordersnnumber=str(getordersn())
ordersnnumber=str(15051110387266)
print "the random ordersn  is ",ordersnnumber  
#print ordersn
def getfanid():
    n = cursor.execute("SELECT fan_id FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
    for row in cursor.fetchall():
      for fanid in row: 
          return fanid  
      
#print gethuiyuanid()  
fanidnumber=str(getfanid())
print fanidnumber

def getcloseconn():
   if cursor!="":
     cursor.close()
   elif conn!="":
     conn.close()
     
     
year = strftime("%Y",localtime())
mon  = strftime("%m",localtime())
day  = strftime("%d",localtime())
hour = strftime("%H",localtime())
min  = strftime("%M",localtime())
sec  = strftime("%S",localtime())

def today():
    '''''
    get today,date format="YYYY-MM-DD"
    '''''
    return date.today()

def todaystr():
    '''
    get date string, date format="YYYYMMDD"
    '''
    return year+mon+day

def datetime():
    '''''
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    '''
    return strftime("%Y-%m-%d %H:%M:%S",localtime())

def datetimestr():
    '''''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year+mon+day+hour+min+sec

def get_day_of_day(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)

def get_days_of_month(year,mon): 
    ''''' 
    get days of month 
    ''' 
    return calendar.monthrange(year, mon)[1] 
  
def get_firstday_of_month(year,mon): 
    ''''' 
    get the first day of month 
    date format = "YYYY-MM-DD" 
    ''' 
    days="01" 
    if(int(mon)<10): 
        mon = "0"+str(int(mon)) 
    arr = (year,mon,days) 
    return "-".join("%s" %i for i in arr) 
  
def get_lastday_of_month(year,mon): 
    ''''' 
    get the last day of month 
    date format = "YYYY-MM-DD" 
    ''' 
    days=calendar.monthrange(year, mon)[1] 
    mon = addzero(mon) 
    arr = (year,mon,days) 
    return "-".join("%s" %i for i in arr) 
  
def get_firstday_month(n=0): 
    ''''' 
    get the first day of month from today 
    n is how many months 
    ''' 
    (y,m,d) = getyearandmonth(n) 
    d = "01" 
    arr = (y,m,d) 
    return "-".join("%s" %i for i in arr) 
  
def get_lastday_month(n=0): 
    ''''' 
    get the last day of month from today 
    n is how many months 
    ''' 
    return "-".join("%s" %i for i in getyearandmonth(n)) 
 
def getyearandmonth(n=0): 
    ''''' 
    get the year,month,days from today 
    befor or after n months 
    ''' 
    thisyear = int(year) 
    thismon = int(mon) 
    totalmon = thismon+n 
    if(n>=0): 
        if(totalmon<=12): 
            days = str(get_days_of_month(thisyear,totalmon)) 
            totalmon = addzero(totalmon) 
            return (year,totalmon,days) 
        else: 
            i = totalmon/12 
            j = totalmon%12 
            if(j==0): 
                i-=1 
                j=12 
            thisyear += i 
            days = str(get_days_of_month(thisyear,j)) 
            j = addzero(j) 
            return (str(thisyear),str(j),days) 
    else: 
        if((totalmon>0) and (totalmon<12)): 
            days = str(get_days_of_month(thisyear,totalmon)) 
            totalmon = addzero(totalmon) 
            return (year,totalmon,days) 
        else: 
            i = totalmon/12 
            j = totalmon%12 
            if(j==0): 
                i-=1 
                j=12 
            thisyear +=i 
            days = str(get_days_of_month(thisyear,j)) 
            j = addzero(j) 
            return (str(thisyear),str(j),days) 
  
def addzero(n): 
    ''''' 
    add 0 before 0-9 
    return 01-09 
    ''' 
    nabs = abs(int(n)) 
    if(nabs<10): 
        return "0"+str(nabs) 
    else: 
        return nabs 

def get_today_month(n=0): 
    ''''' 
    获取当前日期前后N月的日期
    if n>0, 获取当前日期前N月的日期
    if n<0, 获取当前日期后N月的日期
    date format = "YYYY-MM-DD" 
    ''' 
    (y,m,d) = getyearandmonth(n) 
    arr=(y,m,d) 
    if(int(day)<int(d)): 
        arr = (y,m,day) 
    return "-".join("%s" %i for i in arr) 
  
def get3rdcaiwupath():
    return "C:/edaixi_testdata/userdata_caiwu.conf"

def get3rdwuliupath():
    return "C:/edaixi_testdata/userdata_wuliu.conf"



if __name__=="__main__":
    start = time.clock()
        
    print today()  
    print todaystr()
    print datetime()
    print datetimestr()
    print get_day_of_day(1)
    print get_day_of_day(-3)
    print get_today_month(-3)
    print get_today_month(3)