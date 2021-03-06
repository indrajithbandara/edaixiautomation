#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectkefu,kefu_utiltools
class KefuTestcase00rdt3usellyquery(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectkefu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(kefu_utiltools.getkefuconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_kefu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        KEFU_URL = conf.get("kefusection", "uihostname")
        USER_NAME = conf.get("kefusection", "rdt3uiusername")
        PASS_WORD = conf.get("kefusection", "rdt3uipassword")
        print KEFU_URL,USER_NAME,PASS_WORD  
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase00_rdt3_usellyquery(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")


        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(1)>a").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")
#         time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(2)>a").click()
        time.sleep(1)
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(3)>a").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")
        #time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(4)>a").click()
        #time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(5)>a").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(6)>a").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(7)>a").click()
        self.assertEqual(driver.title,u"客服系统")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(8)>a").click()
        self.assertEqual(driver.title,u"客服系统")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+")>a").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_test00_rdt3_ueuallyquery+").dropdown>ul.dropdown-menu>li:nth-child(9)>a").click()
        self.assertEqual(driver.title,u"客服系统")
        
        
#         driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:first-child>a").click()
#         #driver.find_element_by_link_text(u"反馈总列表").click()
#         #driver.find_element_by_link_text(u"踢").click()
#         self.assertEqual(driver.title,u"客服系统")
#         driver.find_element_by_css_selector("div#container.container div.panel.panel-primary ul.nav.nav-tabs li:first-child.active a").click()
#         #driver.find_element_by_link_text(u"处理").click()
#         self.assertEqual(driver.title,u"客服系统")
#         driver.find_element_by_css_selector("div#container.container div.panel.panel-primary table.table.table-stripe tbody#table_new_customer tr#customer_1239520 td a.btn.btn-success.btn-sm").click()
#         #driver.find_element_by_id("tag_to_feedback_71874").click()
#         self.assertEqual(driver.title,u"客服系统")
#         driver.find_element_by_css_selector("div#container.container div.col-sm-6 ul#replies_navi.nav.nav-tabs li:first-child#ajax_customer_feedbacks_all.active a").click()
#         
#         self.assertEqual(driver.title,u"客服系统")
#         driver.find_element_by_css_selector("div#container.container div.row div.col-sm-12 div.div a.btn.btn-info.pull-right").click()
#         self.assertEqual(driver.title,u"客服系统")
#         driver.find_element_by_css_selector("div#container.container table.table.table-striped tbody tr:first-child td:nth-child(8) a.btn.btn-sm.btn-info").click()
#         time.sleep(1)
#         self.assertEqual(u"确认发券吗？", self.close_alert_and_get_its_text())
        
#         print driver.title
#         if "We're sorry" in driver.title:
#             print "We're sorry, but something went wrong."
#             raise NameError
#         else:
#             pass
#         print driver.title
        #self.assertTrue("", "We're sorry")
        #self.assert_(driver.title, u"客服系统")
        self.assertEqual(driver.title,u"客服系统")
        
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
