#-*-coding:utf-8-*- 
#coding=utf-8
from selenium import webdriver
import threading 

#class appobjectops:
# class appObjectUtils(self):
#     
def GetInstance():  
    instance = None  
    mutex = threading.Lock() 
    if(instance == None):  
            mutex.acquire()   
            if(instance == None):  
                #printInfo(u'åˆ�å§‹åŒ–å�•ä¾‹')  
                print u"initial kefu webdriver singleton .........."
                instance = webdriver.Chrome()
                #instance = webdriver.Firefox()
                #instance = webdriver.Ie()
            else:  
                print u" kefu webdriver Sigleton has been initial...."
                #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')    
            mutex.release()  
    else:  
            print u" kefu webdriver Sigleton has been initial...."
            #printInfo(u'å�•ä¾‹å·²ç»�åˆ�å§‹åŒ–')          
    return instance  
#
#kefu automation testing frameworks
#our testing env include test14 test15 test09    test15 is total deploy testing env, 
#test14 is pre-deploy testing env, test09 is xiaoe testing env
#test15
global kefu_tab_feedback,kefu_tab_myuserfeedback,kefu_tab_orderlist
global kefu_tab_tabmanage,kefu_tab_usuallyreply,kefu_tab_usuallyquery
global kefu_tab_estimatemanage,kefu_tab_estimatecomplain,ordersnnumber
kefu_tab_feedback=str(1)
kefu_tab_myuserfeedback=str(2)
kefu_tab_orderlist=str(3)

kefu_tab_tabmanage=str(4)
kefu_tab_usuallyreply=str(5)
kefu_tab_usuallyquery=str(7)

kefu_tab_estimatemanage=str(8)
kefu_tab_estimatecomplain=str(9)

global kefu_tab_test00_myfeedback,kefu_tab_test00_ordertousu,kefu_tab_test00_orderlist,kefu_tab_test00_orderpinjia
global kefu_tab_test00_ueuallyfeedbak,kefu_tab_test00_ueuallyquery,kefu_tab_test00_rdt3_ueuallyquery

kefu_tab_test00_myfeedback=str(7)
kefu_tab_test00_ordertousu=str(7)
kefu_tab_test00_orderlist=str(2)
kefu_tab_test00_orderpinjia=str(6)
kefu_tab_test00_ueuallyfeedbak=str(3)
kefu_tab_test00_ueuallyquery=str(5)


kefu_tab_test00_rdt3_ueuallyquery=str(3)


#test14

# this is test data for automation testing 
ordersnnumber="15100828225690"

# class appobjectkefu:
#     
#     #operation system testcase01 perminssion manage module appobject
#     permloginClickButton="div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
#     clickPermissionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
#     clickPermissionButton="div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success"
#     
#     clickPositionLink="div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle"
#     clickPositionNewButton="div#container.container div#content-container a.btn.btn-info.col-md-1"
#     clickPositionEditButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info"
#     clickPositionDeleteButton="div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-danger"
#     
#     
#     
#     #operation sysytem testcase08 RechargeReturncrash module app object
#     loginClickButton = "div#container.container h3.text-center.text-primary a.btn.btn-success.text-center"
#     clickRechargeReturncrashLink= "div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a"
#     
#     clickNewButtonRechargeReturncrash="div#container.container div a.btn.btn-info.btn-info"
#     addchizhifanxianResult="div#container.container div.alert.fade.in.alert-success"
#     
#     clickEditButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child"
#     editchizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
#     
#     clickDeleteButtonRechargeReturncrash="div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child"
#     deletechizhifanxianresult="div#container.container div.alert.fade.in.alert-success"
#     
    
    
    #operation sysytem testcase03
    
    #operation sysytem testcase04
    
    #operation sysytem testcase05
    
    
    
 
    
    