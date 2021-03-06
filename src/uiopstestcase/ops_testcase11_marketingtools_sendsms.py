#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectops
class OpsTestcase11MarketingToolsSendSms(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectops.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiadminusername")
        PASS_WORD = conf.get("opssection", "uiadminpassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase11_MarketingToolsSendSms(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_MarketingTools+") a").click()
        driver.implicitly_wait(10)
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child("+appobjectops.ops_tab_MarketingTools+").dropdown ul.dropdown-menu li:nth-child(1) a").send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("sms_form_tel").clear()
        driver.find_element_by_id("sms_form_tel").send_keys("18701524517")
        driver.find_element_by_id("sms_form_sms").clear()
        driver.find_element_by_id("sms_form_sms").send_keys("hello rhis is edaixiops")
        driver.find_element_by_name("commit").click()
   
        #smsresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        #print smsresult
        #assert u"发送成功" in (smsresult)
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #smsresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        #print smsresult
        #self.assertEqual(smsresult, u"发送成功")
        #driver.find_element_by_link_text(u"营销工具").click()
        #driver.find_element_by_link_text(u"发送优惠券").click()
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
    
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
