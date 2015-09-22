# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner

from checkMysqlKeywords import *

from autocaiwuwuliu_testcase08_citylist_jiagongdian_factorbalance import *
from autocaiwu_testcase08_citylist_jiagongdian_factorbalancebranch import *
from autocaiwu_testcase08_citylist_jiagongdian_factorbalancemaster import *

if __name__ == '__main__':  
    suite = unittest.TestSuite()  

    #caiwu testcase01 permission and position manage testcase
#     suite.addTest(checkMysqlKeywordsClass('test_checkMysqlKeywordsMethod'))
#     time.sleep(3)
# 
#     suite.addTest(WuliuTestcase08CitylistJiagongdianFactoryBalance('test_wuliu_testcase08_citylist_jiagongdian_factorybalance'))
#     time.sleep(3)
#     suite.addTest(CaiwuTestcase08CitylistJiagongdianFactoryBalanceBranch('test_caiwu_testcase08_citylist_jiagongdian_factorybalance_branch'))
#     time.sleep(3)
#     suite.addTest(CaiwuTestcase08CitylistJiagongdianFactoryBalanceMaster('test_caiwu_testcase08_citylist_jiagongdian_factorybalance_master'))
#     time.sleep(3)
        
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime

    fp = file("c:\\edaixi_testdata\\"+currenttime+"-automation3rd_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi automation3rd testing result",description="201509 luke")
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
    