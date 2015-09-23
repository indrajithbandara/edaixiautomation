#-*-coding:utf-8-*- 
#coding=utf-8

from selenium import webdriver
import threading 



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



#wechat end testcase
global wechatend_tab_basesetting,wechatend_tab_mainbusiness,wechatend_tab_twodimensioncode
global wechatend_tab_setting,wechatend_tab_hongbao,wechatend_tab_credit
global wechatend_tab_promotion,wechatend_tab_crm

global wechatend_tab_basesetting_defaultkeywords,wechatend_tab_basesetting_fronreply,wechatend_tab_basesetting_graphreply
wechatend_tab_basesetting=str(1)
wechatend_tab_basesetting_defaultkeywords=str(4)
wechatend_tab_basesetting_fronreply=str(2)
wechatend_tab_basesetting_graphreply=str(3)





 
    
    