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


global wechatend_tab_mainbusiness_exportcouple,wechatend_tab_mainbusiness_sendcouple,wechatend_tab_mainbusiness,wechatend_tab_mainbusiness_ul
global wechatend_tab_mainbusiness_userdefinebatchsend,wechatend_tab_mainbusiness_wechatcouple

wechatend_tab_mainbusiness=str(1)
wechatend_tab_mainbusiness_ul=str(2)
wechatend_tab_mainbusiness_wechatcouple=str(2)
wechatend_tab_mainbusiness_sendcouple=str(3)
wechatend_tab_mainbusiness_userdefinebatchsend=str(4)
wechatend_tab_mainbusiness_exportcouple=str(5)


global wechatend_tab_twodimensioncode_batchcreate,wechatend_tab_twodimensioncode,wechatend_tab_twodimensioncode_batchmodify
global wechatend_tab_twodimensioncode_createqrcode,wechatend_tab_twodimensioncode_manageqrcode
global wechatend_tab_twodimensioncode_exportqrcode,wechatend_tab_twodimensioncode_scanningstatifcation
global wechatend_tab_twodimensioncode_handqqrcode,wechatend_tab_twodimensioncode_xiaoeqrcode,wechatend_tab_twodimensioncode_ul

wechatend_tab_twodimensioncode=str(1)
wechatend_tab_twodimensioncode_ul=str(3)
wechatend_tab_twodimensioncode_createqrcode=str(2)
wechatend_tab_twodimensioncode_manageqrcode=str(3)
wechatend_tab_twodimensioncode_xiaoeqrcode=str(4)
wechatend_tab_twodimensioncode_handqqrcode=str(5)
wechatend_tab_twodimensioncode_scanningstatifcation=str(6)
wechatend_tab_twodimensioncode_batchcreate=str(7)
wechatend_tab_twodimensioncode_batchmodify=str(8)
wechatend_tab_twodimensioncode_exportqrcode=str(9)



global wechatend_tab_setting,wechatend_tab_setting_ul
global wechatend_tab_setting_managegroup,wechatend_tab_setting_managemenu

wechatend_tab_setting=str(1)
wechatend_tab_setting_ul=str(4)
wechatend_tab_setting_managegroup=str(2)
wechatend_tab_setting_managemenu=str(3)

global wechatend_tab_credit,wechatend_tab_credit_ul,wechatend_tab_credit_creditregular

wechatend_tab_credit=str(1)
wechatend_tab_credit_ul=str(5)
wechatend_tab_credit_creditregular=str(2)



global wechatend_tab_hongbao,wechatend_tab_hongbao_ul
global wechatend_tab_hongbao_gamehongbao,wechatend_tab_hongbao_hongbaologistic,wechatend_tab_hongbao_linkhongbao
global wechatend_tab_hongbao_orderhongbao,wechatend_tab_hongbao_recommendhongbao,wechatend_tab_hongbao_telephonesendcouple
 
wechatend_tab_hongbao=str(1)
wechatend_tab_hongbao_ul=str(6)

wechatend_tab_hongbao_linkhongbao=str(2)
wechatend_tab_hongbao_orderhongbao=str(3)
wechatend_tab_hongbao_gamehongbao=str(4)
wechatend_tab_hongbao_recommendhongbao=str(5)
wechatend_tab_hongbao_telephonesendcouple=str(6)
wechatend_tab_hongbao_hongbaologistic=str(7)



global wechatend_tab_promotion,wechatend_tab_promotion_ul
global wechatend_tab_promotion_channellist,wechatend_tab_promotion_webpushorderlist

wechatend_tab_promotion=str(1)
wechatend_tab_promotion_ul=str(7)
wechatend_tab_promotion_channellist=str(2)
wechatend_tab_promotion_webpushorderlist=str(3)



global wechatend_tab_crm,wechatend_tab_crm_ul,wechatend_tab_crm_usertag
global wechatend_tab_crm_createtag,wechatend_tab_crm_createtaggroup
global wechatend_tab_crm_managetag,wechatend_tab_crm_managetaggroup










    