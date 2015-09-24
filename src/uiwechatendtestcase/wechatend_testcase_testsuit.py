# -*- coding: utf-8 -*-
#encoding:utf-8 

#http://weixin03.edaixi.cn/
import unittest, time, re 
from wechatend_testcase01_basesetting_defaultkeyword import *
from wechatend_testcase01_basesetting_fontreply import *
from wechatend_testcase01_basesetting_graphreply import *

from wechatend_testcase02_mainbusiness_exportcouple import *
from wechatend_testcase02_mainbusiness_sendcouple import *
from wechatend_testcase02_mainbusiness_userdefinebatchsend import *
from wechatend_testcase02_mainbusiness_wechatcouple import *


from wechatend_testcase03_twodimensioncode_batchcreate import *
from wechatend_testcase03_twodimensioncode_batchmodify import *
from wechatend_testcase03_twodimensioncode_createqrcode import *
from wechatend_testcase03_twodimensioncode_exportqrcode import *
from wechatend_testcase03_twodimensioncode_handqqrcode import *
from wechatend_testcase03_twodimensioncode_manageqrcode import *
from wechatend_testcase03_twodimensioncode_scanningstatifcation import *
from wechatend_testcase03_twodimensioncode_xiaoeqrcode import *


from wechatend_testcase04_setting_managegroup import *
from wechatend_testcase04_setting_managemenu import *
from wechatend_testcase05_credit_creditregular import *


from wechatend_testcase06_hongbao_gamehongbao import *
from wechatend_testcase06_hongbao_hongbaologistic import *
from wechatend_testcase06_hongbao_linkhongbao import *
from wechatend_testcase06_hongbao_orderhongbao import *
from wechatend_testcase06_hongbao_recommendhongbao import *
from wechatend_testcase06_hongbao_telephonesendcouple import *


from wechatend_testcase07_promotion_Channellist import *
from wechatend_testcase07_promotion_webpushorderlink import  *
 
# from wechatend_testcase08_crm_checktaglist import *
# from wechatend_testcase08_crm_createtag import *
# from wechatend_testcase08_crm_createtaggroup import *
# from wechatend_testcase08_crm_managetag import *
# from wechatend_testcase08_crm_managetaggroup import *
# from wechatend_testcase08_crm_usertag import *


import HTMLTestRunner

if __name__ == '__main__':  
    suite = unittest.TestSuite()  


    #caiwu testcase01 first need chongzhi,then koukuan,finally is tuikuan testcase
    suite.addTest(WechatTestcase01basesettingdefaultkeyword('test_wechat_testcase01_basesetting_defaultkeyword'))
    time.sleep(3)
    suite.addTest(WechatTestcase01basesettingfrontreply('test_wechat_testcase01_basesetting_frontreply'))
    time.sleep(3)
    suite.addTest(WechatTestcase01basesettinggraphreply('test_wechat_testcase01_basesetting_graphreply')) 
    time.sleep(3)
    
    suite.addTest(WechatTestcase02mainbusinessexportcouple('test_ops_testcase02_mainbusiness_exportcouple')) 
    time.sleep(3)
    suite.addTest(WechatTestcase02mainbusinesssendcouple('test_wechat_testcase02_mainbusiness_sendcouple')) 
    time.sleep(3)
    #caiwu testcase02
    suite.addTest(WechatTestcase02mainbusinessuserdefinebatchsend('test_wechat_testcase02_mainbusiness_userdefinebatchsend'))
    time.sleep(3)
    suite.addTest(WechatTestcase02mainbusinesswechatcouple('test_wechat_testcase02_mainbusiness_wechatcouple'))
    time.sleep(3)
    
    
    suite.addTest(WechatTestcase03twodimensioncodebatchcreate('test_twodimensioncode_testcase03_twodimensioncode_batchcreate'))
    time.sleep(3)
    suite.addTest(WechatTestcase03twodimensioncodebatchmodify('test_wechat_testcase03_twodimensioncode_batchmodify'))
    time.sleep(3)
    suite.addTest(wechatTestcase03twodimensioncodecreateqrcode('test_wechat_testcase03_twodimensioncode_createqrcode'))
    time.sleep(3)
    suite.addTest(wechatTestcase03twodimensioncodeexportqrcode('test_wechat_testcase03_twodimensioncode_exportqrcode'))
    time.sleep(3)
    suite.addTest(wechatTestcase03twodimensioncodehandqqrcode('test_wechat_testcase03_twodimensioncode_handqqrcode'))
    time.sleep(3)
    suite.addTest(wechatTestcase03twodimensioncodemanageqrcode('test_wechat_testcase03_twodimensioncode_manageqrcode'))
    time.sleep(3)
    suite.addTest(wechatTestcase03twodimensioncodescanningstatifcation('test_wechat_testcase03_twodimensioncode_scanningstatifcation'))
    time.sleep(3)
    suite.addTest(wechatTestcase03twodimensioncodexiaoeqrcode('test_testcase03_twodimensioncode_xiaoeqrcode'))
    time.sleep(3)
    
    #caiwu testcase04
    suite.addTest(WechatTestcase04settingmanagegroup('test_wechat_testcase04_setting_managegroup'))
    time.sleep(3)
    suite.addTest(WechatTestcase04settingmanagemenu('test_wechat_testcase04_setting_managemenu'))
    time.sleep(3)
    suite.addTest(CreditTestcase05creditcreditregular('test_credit_testcase05_credit_creditregular'))
    time.sleep(3)

    #caiwu testcase05
    suite.addTest(HongbaoTestcase06hongbaogamehongbao('test_hongbao_testcase06_hongbao_gamehongbao'))
    time.sleep(3)
    suite.addTest(HongbaoTestcase06hongbaohongbaologistic('test_hongbao_testcase06_hongbao_hongbaologistic'))
    time.sleep(3)
    suite.addTest(HongbaoTestcase06hongbaolinkhongbao('test_hongbao_testcase06_hongbao_linkhongbao'))
    time.sleep(3)
    suite.addTest(HongbaoTestcase06hongbaoorderhongbao('test_hongbao_testcase06_hongbao_orderhongbao'))
    time.sleep(3)
    suite.addTest(HongbaoTestcase06hongbaorecommendhongbao('test_hongbao_testcase06_hongbao_recommendhongbao'))
    time.sleep(3)
    suite.addTest(HongbaoTestcase06hongbaotelephonesendcouple('test_hongbao_testcase06_hongbao_telephonesendcouple'))
    time.sleep(3)


    suite.addTest(PromotionTestcase07promotionChannellist('test_promotion_testcase07_promotion_Channellist'))
    time.sleep(3)
    suite.addTest(PromotionTestcase07promotionwebpushorderlink('test_promotion_testcase07_promotion_webpushorderlink'))
    time.sleep(3)


    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    #print currenttime

    fp = file("c:\\edaixi_testdata\\"+currenttime+"-wechatend_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi UIwechat testing result",description="201510 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()









