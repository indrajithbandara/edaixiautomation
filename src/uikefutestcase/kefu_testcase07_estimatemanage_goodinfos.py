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
class KefuTestcase07EstimatemanageGoodinfos(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectkefu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(kefu_utiltools.getkefuconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_kefu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        KEFU_URL = conf.get("kefusection", "uihostname")
        USER_NAME = conf.get("kefusection", "uiusername")
        PASS_WORD = conf.get("kefusection", "uipassword")
        print KEFU_URL,USER_NAME,PASS_WORD  
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase07_estimatemanage_goodinfos(self):
        driver = self.driver
        #driver.get(self.base_url + "/orders/new")
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        
        print driver.title
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_estimatemanage+")>a").click() 
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div#container.container>ul.nav.navbar-nav.btn-box>li:first-child>a").click()
        self.assertEqual(driver.title,u"客服系统")
        #html body #popover_27181.btn.btn-info.my_popover
        driver.find_element_by_css_selector("div#container.container table.table.table-striped tbody tr:first-child td:nth-child(7) a").click()
        #driver.find_element_by_id("popover_27181").click()
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_id("note").clear()
        driver.find_element_by_id("note").send_keys("pingjiagood")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title,u"客服系统")
        #driver.find_element_by_link_text("714604").click()
        
        driver.find_element_by_css_selector("div#container.container table.table.table-striped tbody tr:first-child td:nth-child(2) a").click()
        #html body div#container.container table.table.table-striped tbody tr:first-child td:nth-child(2) a
        
        print driver.title
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
