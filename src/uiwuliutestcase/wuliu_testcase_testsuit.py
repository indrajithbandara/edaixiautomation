#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
import unittest, time, re 
import HTMLTestRunner

from wuliu_testcase01_editpermission import *
from wuliu_testcase01_querypermission  import *

from wuliu_testcase02_factory_delivery import *
from wuliu_testcase02_factory_inoutstockquery import *
from wuliu_testcase02_factory_sign import *

from wuliu_testcase03_site_delivery import *
from wuliu_testcase03_site_inoutstockquery import *
from wuliu_testcase03_site_sign import *

from wuliu_testcase04_pushorder import *
from wuliu_testcase04_modifysignnumber import *

from wuliu_testcase05_takecloth import *

from wuliu_testcase06_pushcloth import *

from wuliu_testcase07_accountbalancequery import *

from wuliu_testcase08_citylist_addredit import *
from wuliu_testcase08_citylist_diaodupaidan_fanxidan_yiconfirm import *
from wuliu_testcase08_citylist_diaodupaidan_fanxidan_yipandan import *
from wuliu_testcase08_citylist_diaoduquery_fanxidan import *
from wuliu_testcase08_citylist_diaoduquery_crud import *

from wuliu_testcase08_citylist_jiagongdian_factorbalance import *
from wuliu_testcase08_citylist_jiagongdianmanage import *
from wuliu_testcase08_citylist_luxuriesLogistics import *
from wuliu_testcase08_citylist_outtimemanage import *
from wuliu_testcase08_citylist_selfmanagedLogistics import *
from wuliu_testcase08_citylist_servicesiteLogistics import *
from wuliu_testcase08_citylist_shouyidianmanage import *

from wuliu_testcase08_citylist_dividebasearea import *
from wuliu_testcase08_citylist_dividekuaidiarea import *
from wuliu_testcase08_citylist_divideluxuryarea import *
from wuliu_testcase08_citylist_dividexiaoesitearea import *
from wuliu_testcase08_citylist_dividezhongbaoarea import *

from wuliu_testcase08_citylist_xiaoemanagerLogistics import *
from wuliu_testcase08_citylist_xiaoeyizhansiteLogistics import *
from wuliu_testcase08_citylist_xiaoeyizhansitepersonmanage import *

from wuliu_testcase09_factory_orderquery import *

from wuliu_testcase10_site_orderquery import *

from wuliu_testcase11_sitepersonmanage import *

from wuliu_testcase00_editpermission_sitepersmission import *
from wuliu_testcase00_factorysite_servicesitequery import *
from wuliu_testcase00_factorysite_sitepeoplemanage import *


if __name__ == '__main__':  
     suite = unittest.TestSuite()  
    
     #caiwu testcase01 first need chongzhi,then koukuan,finally is tuikuan testcase
     suite.addTest(WuliuTestcase01EditPermission('test_wuliu_testcase01_EditPermission'))
     time.sleep(3)
#      suite.addTest(WuliuTestcase01Querypermission('test_wuliu_testcase01_querypermission'))
#      time.sleep(3)
     #caiwu testcase02
     suite.addTest(WuliuTestcase02factorydelivery('test_wuliu_testcase02_factory_delivery'))
     time.sleep(3)
     suite.addTest(WuliuTestcase02factoryinoutstockquery('test_wuliu_testcase02_factory_inoutstockquery'))
     time.sleep(3)
     suite.addTest(WuliuTestcase02factorysign('test_wuliu_testcase02factory_sign'))
     time.sleep(3)
     #caiwu testcase03s
     suite.addTest(WuliuTestcase03sitedelivery('test_wuliu_testcase03_site_delivery'))
     time.sleep(3)
     suite.addTest(WuliuTestcase03siteinoutstockquery('test_wuliu_testcase03_site_inoutstockquery'))
     time.sleep(3)
     suite.addTest(WuliuTestcase03sitesign('test_wuliu_testcase03_site_sign'))
     time.sleep(3)
     #caiwu testcase04
     suite.addTest(WuliuTestcase04pushorder('test_wuliu_testcase04_pushorder'))
     time.sleep(3)

     suite.addTest(WuliuTestcase04modifysignnumber('test_wuliu_testcase04_modifysignnumber'))
     time.sleep(3)
     #caiwu testcase05
     suite.addTest(WuliuTestcase05takecloth('test_wuliu_testcase05_takecloth'))
     time.sleep(3)
     #caiwu testcase06
     suite.addTest(WuliuTestcase06pushcloth('test_wuliu_testcase06_pushcloth'))
     time.sleep(3)
     #ops testcase07
     suite.addTest(WuliuTestcase07AccountBalance('test_wuliu_testcase07_accountbalance'))
     time.sleep(3)
     #ops testcase08
     suite.addTest(WuliuTestcase08CitylistAddEdit('test_wuliu_testcase08_citylist_addedit'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08citylistdiaodupaidanfanxidanYiPandan('test_wuliu_testcase08citylist_diaodupaidan_fanxidan_yipandan'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08citylistdiaodupaidanfanxidanYiConfirm('test_wuliu_testcase08citylist_diaodupaidan_fanxidan_yiconfirm'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08citylistdiaoduqueryfanxidan('test_wuliu_testcase08_citylist_diaoduquery_fanxidan'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08citylistdiaoduquerycrud('test_wuliu_testcase08_citylist_diaoduquery_crud'))
     time.sleep(3)
     
     suite.addTest(WuliuTestcase08Citylistdividebasearea('test_wuliu_testcase08_citylist_dividebasearea'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistdividekuaidiarea('test_wuliu_testcase08_citylist_dividekuaidiarea'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistdivideluxuryarea('test_wuliu_testcase08_citylist_divideluxuryarea'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistdividexiaoesitearea('test_wuliu_testcase08_citylist_dividexiaoesitearea'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistdividezhongbaoarea('test_wuliu_testcase08_citylist_dividezhongbaoarea'))
     time.sleep(3)
    
     suite.addTest(WuliuTestcase08CitylistJiagongdianFactoryBalance('test_wuliu_testcase08_citylist_jiagongdian_factorybalance'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistjiagongdianmanage('test_wuliu_testcase08_citylist_jiagongdianmanage'))
     time.sleep(3)
     
     suite.addTest(WuliuTestcase08CitylistluxuriesLogistics('test_wuliu_testcase08_citylist_luxuriesLogistics'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistouttimemanage('test_wuliu_testcase08_citylist_outtimemanage'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08CitylistselfmanagedLogistics('test_wuliu_testcase08_citylist_selfmanagedLogistics'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08CitylistservicesiteLogistics('test_wuliu_testcase08_citylist_servicesiteLogistics'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08Citylistshouyidianmanage('test_wuliu_testcase08_citylist_shouyidianmanage'))
     time.sleep(3)
 
     
     suite.addTest(WuliuTestcase08CitylistxiaoemanagerLogistics('test_wuliu_testcase08_citylist_xiaoemanagerLogistics'))
     time.sleep(3)
     suite.addTest(WuliuTestcase08CitylistxiaoeyizhansiteLogistics('test_wuliu_testcase08_citylist_xiaoeyizhansiteLogistics'))
     time.sleep(3)
 #     suite.addTest(WuliuTestcase08Citylistxiaoeyizhansitepersonmanage('test_wuliu_testcase08_citylist_xiaoeyizhansitepersonmanage'))
 #     time.sleep(3)
     
     #wuliu testcase09
     suite.addTest(WuliuTestcase09FactoryOrderQuery('test_wuliu_testcase09_factory_orderquery'))
     time.sleep(3)
     #wuliu testcase10
     suite.addTest(WuliuTestcase10SiteOrderquery('test_wuliu_testcase10_site_orderquery'))
     time.sleep(3)
     
     #wuliu testcase11
     suite.addTest(WuliuTestcase11SitePersonManage('test_wuliu_testcase11_site_personmanage'))
     time.sleep(3)
    
    
    #wuliu permission rdt siteuiusername
     suite.addTest(WuliuTestcase00EditSitePermission('test_wuliu_testcase00_EditSitePermission'))
     time.sleep(3)
     suite.addTest(WuliuTestcase00siteservicesitequery('test_wuliu_testcase00_site_servicesitequery'))
     time.sleep(3)
     suite.addTest(WuliuTestcase00sitepeoplemanage('test_wuliu_testcase00_site_peoplemanage'))
     time.sleep(3)
    
     currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
     print currenttime

     fp = file("c:\\edaixi_testdata\\"+currenttime+"-wuliu_test_report.html", 'wb')
    
     htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiwuliu testing result",description="2015 luke")
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
    