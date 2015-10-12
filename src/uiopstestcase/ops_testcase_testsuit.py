#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
import unittest, time, re 
import HTMLTestRunner
import ops_utiltools

from ops_testcase01_permissionmanage_permission import *
from ops_testcase01_permissionmanage_position import *

from ops_testcase02_layoutmanage_bigfunction import *
from ops_testcase02_layoutmanage_branchbanner import *
from ops_testcase02_layoutmanage_masterbanner import *
from ops_testcase02_layoutmanage_smallfunction import *
from ops_testcase02_mapsetting_subcitymapsetting import *
from ops_testcase02_innertestingmanage import *

from ops_testcase03_distribution_addgoods import *
from ops_testcase03_distribution_editgoods import *
from ops_testcase03_distribution_query import *
from ops_testcase03_distribution_updown import *

from ops_testcase04_category_edittemplate_xiyi import *
from ops_testcase04_category_edittemplate_xixie import *
from ops_testcase04_category_edittemplate_xijiafang import *
from ops_testcase04_category_edittemplate_xishechipin import *
from ops_testcase04_category_substation import *
from ops_testcase04_categorymanage import *


from ops_testcase05_price_clothes import *
from ops_testcase05_price_hometextile import *
from ops_testcase05_price_shoes import *

from ops_testcase06_freight_feeapprove import *
from ops_testcase06_freight_substationapprove import *

from ops_testcase07_clothesmanage_effect import *
from ops_testcase07_clothesmanage_endprice import *
from ops_testcase07_clothesmanage_historyprice import *
from ops_testcase07_clothesmanage_brand  import  *
from ops_testcase07_clothesmanage_minor  import *

from ops_testcase08_recharge_returncrash import *

from ops_testcase09_citymanage_areaadd import *
from ops_testcase09_citymanage_areaonoff import *
from ops_testcase09_citymanage_areauserdefine import *
from ops_testcase09_citymanage_onoff import *
from ops_testcase09_citymanage_queryadd import *

from ops_testcase10_couponmanage import *
from ops_testcase11_marketingtools_sendsms import *
from ops_testcase11_marketingtools_sendyouhuiquan import *

if __name__ == '__main__':  
    suite = unittest.TestSuite()  

    #caiwu testcase01 permission and position manage testcase
    suite.addTest(OpsTestcase01Permissionmanagepermission('test_ops_testcase01_permissionmanage_permission'))
    time.sleep(3)
    suite.addTest(OpsTestcase01PermissionmanagePosition('test_ops_testcase01_permissionmanage_position'))
    time.sleep(3)
    #caiwu testcase02
    suite.addTest(OpsTestcase02LayoutManageMasterBanner('test_ops_testcase02_layoutnmanage_masterbanner'))
    time.sleep(3)
    suite.addTest(OpsTestcase02LayoutManageBigFunction('test_ops_testcase02_layoutmanage_bigfunction'))
    time.sleep(3)
    suite.addTest(OpsTestcase02LayoutManageSmallFunction('test_ops_testcase02_layoutmanage_smallfunction'))
    time.sleep(3)
    
    suite.addTest(OpsTestcase02MapSettingSubCityMapSetting('test_ops_testcase02_mapSetting_subCityMapSetting'))
    time.sleep(3)
    
    suite.addTest(OpsTestcase02innertestingmanage('test_ops_testcase02_innertestingmanage'))
    time.sleep(3)

    #caiwu testcase03s
    suite.addTest(OpsTestcase03DistributionQuery('test_ops_testcase03_distribution_query'))
    time.sleep(3)
    suite.addTest(OpsTestcase01DistributionUpDown('test_ops_testcase03_Distribution_updown'))
    time.sleep(3)
    suite.addTest(OpsTestcase03DistributionAddgoods('test_ops_testcase01_Distribution_addgoods'))
    time.sleep(3)
    suite.addTest(OpsTestcase01Distributioneditgoods('test_ops_testcase01_Distribution_editgoods'))
    time.sleep(3)
    #caiwu testcase04
    suite.addTest(OpsTestcase04Categorymanage('test_ops_testcase04_categorymanage'))
    time.sleep(3)
#     suite.addTest(OpsTestcase04CategorySubStation('test_ops_testcase04_Category_substation'))
#     time.sleep(3)
    suite.addTest(OpsTestcase04Categoryedittemplatexiyi('test_ops_testcase04_Categoryedittemplatexiyi'))
    time.sleep(3)
    suite.addTest(OpsTestcase04Categoryedittemplatexixie('test_ops_testcase04_Categoryedittemplatexixie'))
    time.sleep(3)
    suite.addTest(OpsTestcase04Categoryedittemplatexijiafang('test_ops_testcase04_Categoryedittemplatexijiafang'))
    time.sleep(3)
    suite.addTest(OpsTestcase04Categoryedittemplatexishechipin('test_ops_testcase04_Categoryedittemplatexishechipin'))
    time.sleep(3)
    #caiwu testcase05
    suite.addTest(OpsTestcase05PriceClothes('test_ops_testcase05_PriceClothes'))
    time.sleep(3)
    suite.addTest(OpsTestcase05PriceHometextile('test_ops_testcase05_PriceHometextile'))
    time.sleep(3)
    suite.addTest(OpsTestcase05PriceShoes('test_ops_testcase05_PriceShoes'))
    time.sleep(3)
    #caiwu testcase06
    suite.addTest(OpsTestcase06freightfeeapprove('test_ops_testcase06_freightfeeapprove'))
    time.sleep(3)
    suite.addTest(OpsTestcase06freightsubstationapprove('test_ops_testcase06_freightsubstationapprove'))
    time.sleep(3)

    #ops testcase07
    suite.addTest(OpsTestcase07clothesmanagebrand('test_ops_testcase07_clothesmanagebrand'))
    time.sleep(3)
    suite.addTest(OpsTestcase07clothesmanageeffect('test_ops_testcase07_clothesmanageeffect'))
    time.sleep(3)
    suite.addTest(OpsTestcase07clothesmanageminor('test_ops_testcase07_clothesmanageminor'))
    time.sleep(3)
    suite.addTest(OpsTestcase07clothesmanageendprice('test_ops_testcase07_clothesmanageendprice'))
    time.sleep(3)
    #suite.addTest(OpsTestcase07clothesmanagehistoryprice('test_ops_testcase07_clothesmanageendprice'))
    #time.sleep(3)
    #ops testcase08
       
    suite.addTest(OpsTestcase08rechargereturncrash('test_ops_testcase08_rechargereturncrash'))
    time.sleep(3)
    #ops testcase09
    suite.addTest(OpsTestcase09citymanagequeryadd('test_ops_testcase09_citymanagequeryadd'))
    time.sleep(3)
    suite.addTest(OpsTestcase09citymanageonoff('test_ops_testcase09_citymanageonoff'))
    time.sleep(3)
    suite.addTest(OpsTestcase09citymanageareauserdefine('test_ops_testcase09_citymanageareauserdefine'))
    time.sleep(3)
    suite.addTest(OpsTestcase09citymanageareaadd('test_ops_testcase09_citymanageareaadd'))
    time.sleep(3)
    suite.addTest(OpsTestcase09citymanageareaonoff('test_ops_testcase09_citymanageareaonoff'))
    time.sleep(3)
    #ops testcase10
    suite.addTest(OpsTestcase10couponmanage('test_ops_testcase10_couponmanage'))
    time.sleep(3)
    #ops testcase11s
    suite.addTest(OpsTestcase11MarketingToolsSendSms('test_ops_testcase11_MarketingToolsSendSms'))
    time.sleep(3)
    suite.addTest(OpsTestcase11MarketingToolsSendyouhuiquan('test_ops_testcase11_MarketingToolsSendyouhuiquan'))
    time.sleep(3)
        
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime

    fp = file("c:\\edaixi_testdata\\"+currenttime+"-ops_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiops testing result",description="201508 luke")
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
    