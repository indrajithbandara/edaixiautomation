#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
import appobjectcaiwu,caiwu_utiltools
class CaiwuTestcase02caiwuYouhuiquanlistQuery(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectcaiwu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        #conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        conf.read(caiwu_utiltools.getcaiwuconfigpath())
        global CAIWU_URL,USER_NAME,PASS_WORD
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        USER_NAME = conf.get("caiwusection", "uiusername")
        PASS_WORD = conf.get("caiwusection", "uipassword")
        print CAIWU_URL,USER_NAME,PASS_WORD 
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_CaiwuTestcase02_caiwuyouhuiquanlist_query(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        self.assertEqual(driver.title,u"财务")
        
        #driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown a.dropdown-toggle").click()
       #driver.find_element_by_link_text(u"优惠券列表").click()
        self.assertEqual(driver.title,u"财务")
        time.sleep(1)
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a").click()
        self.assertEqual(driver.title,u"财务")
        
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"测试")
        driver.find_element_by_xpath("(//input[@name='commit'])[1]").click()
        self.assertEqual(driver.title,u"财务")
        time.sleep(1)
        driver.find_element_by_id("apply_department").clear()
        driver.find_element_by_id("apply_department").send_keys(u"测试")
        driver.find_element_by_xpath("(//input[@name='commit'])[3]").click()
        
#         driver.find_element_by_id("coupon_list_id").clear()
#         driver.find_element_by_id("coupon_list_id").send_keys("533")
#         driver.find_element_by_xpath("(//input[@name='commit'])[2]").click()
#         
        ''''
        bodycontent=driver.find_element_by_xpath("//body").text
        print bodycontent
        if "We're sorry" in bodycontent:
            raise "We're sorry, but something went wrong. excepition" 
        else:
            pass
        '''
        self.assertEqual(driver.title,u"财务")
        
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
