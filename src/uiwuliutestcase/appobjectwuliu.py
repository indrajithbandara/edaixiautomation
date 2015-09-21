#-*-coding:utf-8-*- 
#coding=utf-8

from selenium import webdriver
import threading,wuliu_utiltools
import MySQLdb,ConfigParser
import csv
#This module /class is config and test data for wuliu automation testing sripts

conf = ConfigParser.ConfigParser()
conf.read(wuliu_utiltools.getwuliuconfigpath())  
mysqlhostname = conf.get("databaseconn", "mysqlhostname")
mysqlusername = conf.get("databaseconn", "mysqlusername")
mysqlpassword = conf.get("databaseconn", "mysqlpassword")
mysqlrongchangdb  = conf.get("databaseconn", "mysqlrongchangdb")
        
        
#@staticmethod  
def GetInstance():  
    instance = None  
    mutex = threading.Lock() 
    if(instance == None):  
            mutex.acquire()   
            if(instance == None):  
                #printInfo(u'åˆ�å§‹åŒ–å�•ä¾‹')  
                print u"initial singleton .........."
                #instance = webdriver.Firefox()
                #instance = webdriver.Ie()
                instance = webdriver.Chrome()
            else:  
                print u" Sigleton has been initial...."
                #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')    
            mutex.release()  
    else:  
            print u" Sigleton has been initial...."
            #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')          
    return instance  
    
    
class Singleton(): 
    instance = None  
    mutex = threading.Lock()    
    def __init__(self):  
        pass  
     
    @staticmethod  
    def GetInstance():  
        if(Singleton.instance == None):  
            Singleton.mutex.acquire()   
            if(Singleton.instance == None):  
                #printInfo(u'åˆ�å§‹åŒ–å�•ä¾‹')  
                print u"initial singleton .........."
                Singleton.instance = webdriver.Firefox()
            else:  
                print u" Sigleton has been initial...."
                #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')    
            Singleton.mutex.release()  
        else:  
            print u" Sigleton has been initial...."
            #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')          
        return Singleton.instance  
#define wuliu system module tab,if module tab has been changed,we need change the number for wuliu ssyetem tab
global wuliutabone,wuliutabtwo,wuliutabthree,wuliutabfour,wuliutabfive
global wuliutabsix,wuliutabseven,wuliutabeight,wuliutabnine,wuliutabten,wuliutabeleven
wuliutabone=str(1)
wuliutabtwo=str(2)
wuliutabthree=str(3)
wuliutabfour=str(4)
wuliutabfive=str(5)
wuliutabsix=str(6)
wuliutabseven=str(7)
wuliutabeight=str(8)
wuliutabnine=str(9)
wuliutabten=str(10)
wuliutabeleven=str(11)

#This is wuliu system test data for platform

global testcase08_jiagongdian_forbalantestdata ,jiagongdianchuruku_signnumber_testdata,jiagongzhandian_signnumber_testdata
testcase08_jiagongdian_forbalantestdata=u"快洗"
jiagongdianchuruku_signnumber_testdata=""
jiagongzhandian_signnumber_testdata=""

def deleteOutlet_RulesTableData():
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        cursor.execute("DELETE FROM outlet_rules")
        conn.commit()
        cursor.close()
        conn.close()

#class appobjectops:
# class appObjectUtils(self):
# test data for wuliu system
global testdata_ordersnumber
testdata_ordersnumber="E0000000006"
global testdata_bagsnnumber
testdata_bagsnnumber="E0000000006"
# class appobjectops:
global permloginClickButton,clickPermissionLink,clickPermissionButton
global clickPositionLink,clickPositionNewButton,clickPositionEditButton,clickPositionDeleteButton
    #operation system testcase01 perminssion manage module appobject
permloginClickButton="div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
clickPermissionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
clickPermissionButton="div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success"
    
clickPositionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
clickPositionNewButton="div#container.container div#content-container a.btn.btn-info.col-md-1"
clickPositionEditButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info"
clickPositionDeleteButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-danger"
    
    
global loginClickButton,clickRechargeReturncrashLink,clickNewButtonRechargeReturncrash,addchizhifanxianResult
global clickEditButtonRechargeReturncrash,editchizhifanxianresult,clickDeleteButtonRechargeReturncrash,deletechizhifanxianresult

    #operation sysytem testcase08 RechargeReturncrash module app object
loginClickButton = "div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
clickRechargeReturncrashLink= "div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a"
    
clickNewButtonRechargeReturncrash="div#container.container div a.btn.btn-info.btn-info"
addchizhifanxianResult="div#container.container div.alert.fade.in.alert-success"
    
clickEditButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child"
editchizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
    
clickDeleteButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child"
deletechizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
    
    
    
    #operation sysytem testcase03
    
    #operation sysytem testcase04
    
    #operation sysytem testcase05
    
    
    
 
    
    