# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
from caiwu_testcase01_caiwuordermanagechongzhi import *
from caiwu_testcase01_caiwuordermanagekoukuan import *
from caiwu_testcase01_caiwuordermanagetuikuan import *
from caiwu_testcase01_caiwuordermanagemore import *
from caiwu_testcase01_caiwuordermanageshoukuanmanage import *


from caiwu_testcase02_caiwuyouhuicardgroup import *
from caiwu_testcase02_caiwuyouhuicardlist_create import *
from caiwu_testcase02_caiwuyouhuicardgsearch import *
from caiwu_testcase02_caiwuyouhuiquanlist_addedit_ecouple import *
from caiwu_testcase02_caiwuyouhuiquanlist_addedit_shiticouple import *

from caiwu_testcase02_caiwuyouhuiquanlist_query import *

from caiwu_testcase03_caiwushiticard_create import *
from caiwu_testcase03_caiwushiticard_crud import *
from caiwu_testcase03_caiwushiticard_query import *

from caiwu_testcase04_caiwuhuiyuancardquery_chongzhi import *
from caiwu_testcase04_caiwuhuiyuancardquery_koukuan import *
from caiwu_testcase04_caiwuhuiyuancardquery_tuikuan import *
from caiwu_testcase04_caiwuhuiyuancardquery_more import *

from caiwu_testcase05_caiwuyouchongzhicared_crud import *
from caiwu_testcase05_caiwuyouchongzhicared_fenpei import *
from caiwu_testcase05_caiwuyouchongzhicared_huishou import *
from caiwu_testcase05_caiwuyouchongzhicared_kongbaikaCreate import *
from caiwu_testcase05_caiwuyouchongzhicared_query import *

from caiwu_testcase06_caiwuuserquery_huiyuancard_chongzhi import *
from caiwu_testcase06_caiwuuserquery_huiyuancard_koukuan import *
from caiwu_testcase06_caiwuuserquery_huiyuancard_tuikuan import *
from caiwu_testcase06_caiwuuserquery_huiyuancard_more import *
from caiwu_testcase06_caiwuuserquery_huiyuancardcrud import *
from caiwu_testcase06_caiwuuserquery_query import *


#http://hongbao03.edaixi.cn/mobile.php?uuid=b9a49e1d89858de633c33b5e4fd74485&method=qrcode
#http://weixin03.edaixi.cn/
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
    