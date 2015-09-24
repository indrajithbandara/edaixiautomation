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


from wechatend_testcase07_promotion_qudaolist import *
from wechatend_testcase07_promotion_webpushorderlink import  *
 
from wechatend_testcase08_crm_checktaglist import *
from wechatend_testcase08_crm_createtag import *
from wechatend_testcase08_crm_createtaggroup import *
from wechatend_testcase08_crm_managetag import *
from wechatend_testcase08_crm_managetaggroup import *
from wechatend_testcase08_crm_usertag import *


import HTMLTestRunner

if __name__ == '__main__':  
    suite = unittest.TestSuite()  


    #caiwu testcase01 first need chongzhi,then koukuan,finally is tuikuan testcase
    suite.addTest(CaiwuTestcase01Caiwuordermanagementchongzhi('test_caiwu_testcase01_caiwuordermanagementchongzhi'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase01Caiwuordermanagementkoukuan('test_caiwu_testcase01_caiwuordermanagementkoukuan'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase01Caiwuordermanagementtuikuan('test_caiwu_testcase01_caiwuordermanagementtuikuan')) 
    time.sleep(3)
    suite.addTest(CaiwuTestcase01Caiwuordermanagementmore('test_caiwu_testcase01_caiwuordermanagementmore')) 
    time.sleep(3)
    suite.addTest(CaiwuTestcase01Caiwuordermanagementshoukuanmanagei('test_caiwu_testcase01_caiwuordermanagement_shoukuanmanage')) 
    time.sleep(3)
    #caiwu testcase02
    suite.addTest(CaiwuTestcase02Caiwuyouhuicardgroup('test_caiwu_testcase02_caiwuyouhuicardgroup'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase02Caiwuyouhuicardgsearch('test_caiwu_testcase02_caiwuyouhuicardsearch'))
    time.sleep(3)
    
    suite.addTest(CaiwuTestcase02caiwuYouhuiquanlistAddEditEcouple('test_Caiwu_Testcase02_caiwuyouhuiquanlist_addedit_ecouple'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase02caiwuYouhuiquanlistAddEditShitiCouple('test_Caiwu_Testcase02_caiwuyouhuiquanlist_addedit_shiticouple'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase02CaiwuyouhuicardlistCreate('test_caiwu_testcase02_caiwuyouhuicardlist_create'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase02caiwuYouhuiquanlistQuery('test_CaiwuTestcase02_caiwuyouhuiquanlist_query'))
    time.sleep(3)
        
    #caiwu testcase03s
    suite.addTest(CaiwuTestcase03CaiwushiticardCreate('test_caiwu_testcase03_caiwushiticard_create'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase03CaiwushiticardCrud('test_caiwu_testcase03_caiwushiticard_crud'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase03CaiwushiticardQuery('test_caiwu_testcase03_caiwushiticard_query'))
    time.sleep(3)
    
    #caiwu testcase04
    suite.addTest(CaiwuTestcase04CaiwuhuiyuancardqueryChongzhi('test_caiwu_testcase04_caiwuhuiyuancardquery_chongzhi'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase04CaiwuhuiyuancardqueryKoukuan('test_caiwu_testcase04_caiwuhuiyuancardquery_koukuan'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase04CaiwuhuiyuancardqueryTuikuan('test_caiwu_testcase04_caiwuhuiyuancardquery_tuikuan'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase04CaiwuhuiyuancardqueryMore('test_caiwu_testcase04_caiwuhuiyuancardquery_more'))
    time.sleep(3)
            
    #caiwu testcase05
    suite.addTest(CaiwuTestcase05CaiwuyouchongzhicaredCrud('test_caiwu_testcase05_caiwuyouchongzhicared_crud'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase05CaiwuyouchongzhicaredFenpei('test_caiwu_testcase05_caiwuyouchongzhicared_fenpei'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase05CaiwuyouchongzhicaredHuishou('test_caiwu_testcase05_caiwuyouchongzhicared_huishou'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase05CaiwuyouchongzhicaredKongbaikaCreate('test_caiwu_testcase05_caiwuyouchongzhicared_kongbaika_create'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase05CaiwuyouchongzhicaredQuery('test_caiwu_testcase05_caiwuyouchongzhicared_query'))
    time.sleep(3)
        
    #caiwu testcase06
    suite.addTest(CaiwuTestcase06CaiwuuserqueryQuery('test_caiwu_testcase06_caiwuuserquery_query'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase06CaiwuuserqueryHuiyuancardcrud('test_caiwu_testcase06_caiwuuserquery_huiyuancardcrud'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase06CaiwuuserqueryHuiyuanMore('test_caiwu_testcase06_caiwuuserquery_Huiyuan_more'))
    time.sleep(3)
            
    suite.addTest(CaiwuTestcase06CaiwuuserqueryHuiyuncardChongzhi('test_caiwu_testcase06_caiwuuserquery_Huiyuncard_Chongzhi'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase06CaiwuuserqueryHuiyuncardKoukuan('test_caiwu_testcase06_caiwuuserquery_Huiyuncard_Koukuan'))
    time.sleep(3)
    suite.addTest(CaiwuTestcase06CaiwuuserqueryHuiyuanTuikuan('test_caiwu_testcase06_caiwuuserquery_Huiyuan_Tuikuan'))
    time.sleep(3)

    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    #print currenttime

    fp = file("c:\\edaixi_testdata\\"+currenttime+"-caiwu_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uicaiwu testing result",description="201508 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
'''
def test_caiwu_suite():
    suite= unittest.TestSuite()  

    suite.addTest(CaiwuHuiyuancardquery('test_caiwu_huiyuancardquery'))
    suite.addTest(CaiwuUserquery('test_caiwu_userquery'))
    
    suite.addTest(CaiwuShitika('test_caiwu_shitika'))
    suite.addTest(CaiwuShitikaShengchenka('test_caiwu_shitika_shengchenka')) 
    suite.addTest(CaiwuShitikaQuery('test_caiwu_shitika_query'))
    suite.addTest(CaiwuShitikaModify('test_caiwu_shitika_modify'))
    suite.addTest(CaiwuShitikaChongzhi('test_caiwu_shitika_chongzhi'))
    
    suite.addTest(CaiwuYouhuiquangroup('test_caiwu_youhuiquangroup'))
    suite.addTest(CaiwuYouhuiquanlist('test_caiwu_youhuiquanlist'))
    suite.addTest(CaiwuYouhuiquanlistAdd('test_caiwu_youhuiquanlist_add'))
    suite.addTest(CaiwuYouhuiquanlistExport('test_caiwu_youhuiquanlist_export'))
    suite.addTest(CaiwuYouhuiquanlistModify('test_caiwu_youhuiquanlist_modify'))
    

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"caiwu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uicaiwu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
 '''
    