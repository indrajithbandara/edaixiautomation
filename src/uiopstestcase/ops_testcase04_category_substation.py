#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
import appobjectops,ops_utiltools
class OpsTestcase04CategorySubStation(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Ie()
        self.driver = appobjectops.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(ops_utiltools.getopsconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiadminusername")
        PASS_WORD = conf.get("opssection", "uiadminpassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase04_Category_substation(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(appobjectops.ops_tab_category_username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(appobjectops.ops_tab_category_password)
        driver.find_element_by_id("login-submit").click()
        print " login ops subsystem admin permisssion is ",driver.title
        
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_Category+") a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+appobjectops.ops_tab_Category+").dropdown ul.dropdown-menu li:nth-child("+appobjectops.ops_tab_Category_substation+") a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_link_text(u"类目管理").click()
        #driver.find_element_by_link_text(u"分站类目审核").click()
        #driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child("+str(2)+") td:last-child a.btn.btn-sm.btn-info").click()
        #html body div#container.container table.table.table-bordered.table-striped tbody tr td a.btn.btn-sm.btn-info
        print " check substation for testcase test_ops_testcase04_Category_substation is ",driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        try:
            shenqingvar=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2).danger>td:last-child").text
            print " the shenqingvar is  ",shenqingvar
            if shenqingvar=="":
               driver.find_element_by_css_selector("button.btn.dropdown-toggler").click()
               driver.find_element_by_link_text("logout").click()
               print " the driver title is ",driver.title  
               driver.implicitly_wait(20)             
               self.loginMasterApproveMethod()
        except NoSuchElementException:
            shenqingvarobj=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:last-child").text
            print " the shenqingvarobj is  ",shenqingvarobj
            if shenqingvarobj==u"申请下线":
                driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:last-child").click()
                time.sleep(1)
                self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认申请下线?[\s\S]$")
                time.sleep(2)
                shenqingsubmitresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
                print " the shenqingsubmitresult is  ",shenqingsubmitresult
                #self.assertEqual(shenqingsubmitresult, u"申请已提交")
                assert u"申请已提交" in shenqingsubmitresult
                driver.find_element_by_css_selector("button.btn.dropdown-toggler").click()
                driver.find_element_by_link_text("logout").click()
                driver.implicitly_wait(20)  
                self.loginMasterApproveMethod()
            elif shenqingvarobj==u"申请上线":
                driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:last-child").click()
                time.sleep(1)
                self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认申请上线?[\s\S]$")
                time.sleep(2)
                shenqingsubmitresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
                print " the shenqingsubmitresult is  ",shenqingsubmitresult
                #self.assertEqual(shenqingsubmitresult, u"申请已提交")
                assert u"申请已提交" in shenqingsubmitresult
                driver.find_element_by_css_selector("button.btn.dropdown-toggler").click()
                driver.find_element_by_link_text("logout").click()
                driver.implicitly_wait(20)  
                self.loginMasterApproveMethod()
        else:
                pass
        #html body div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2).danger>td:last-child

#         driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:last-child").click()
#         #html body div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child.btn.btn-sm.btn-warning
#         #self.assert_(driver.title, u"e袋洗城市运营后台")
#         
#         #driver.find_element_by_link_text(u"申请下线").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认申请下线[\s\S]$")
        #申请已提交
        
        ##Master admin login can approve and agrre with 
        ##Brach admin login and submit a request 
#         driver.find_element_by_css_selector("button.btn.dropdown-toggler").click()
#         driver.find_element_by_link_text("logout").click()
#         print " the driver title is ",driver.title
#         
 
    def loginMasterApproveMethod(self):
        driver = self.driver
#         driver.get(self.base_url + "/")
#         driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(4)+") a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+str(4)+").dropdown ul.dropdown-menu li:nth-child("+str(3)+") a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #html body div#container.container table.table.table-bordered.table-striped tbody tr td a.btn.btn-sm.btn-info
        shenhecheckfiled=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:first-child").text
        print " the shenhecheckfiled is ",shenhecheckfiled
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child.btn.btn-sm.btn-info
        if shenhecheckfiled==u"审核":
           driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child.btn.btn-sm.btn-info").click()
           
           driver.find_element_by_css_selector("div#container.container div.text-right a.btn.btn-sm.btn-info").click()
           
           shehepass=driver.find_element_by_css_selector("html body div#container.container div.alert.fade.in.alert-success").text
           print " the shehepass is ",shehepass
           #self.assertEqual(shehepass, u"操作成功")
           assert u"操作成功" in shehepass
        else:
            pass
        #driver.find_element_by_link_text(u"分站类目审核").click()
        #driver.find_element_by_link_text(u"审核").click()
        print " the login master permission system is ",driver.title
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
