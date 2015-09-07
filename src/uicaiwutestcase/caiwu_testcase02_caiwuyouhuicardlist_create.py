# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
from selenium.webdriver.support.ui import WebDriverWait 
import appobjectcaiwu
class CaiwuTestcase02CaiwuyouhuicardlistCreate(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectcaiwu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        USER_NAME = conf.get("caiwusection", "uiusername")
        PASS_WORD = conf.get("caiwusection", "uipassword")
        print CAIWU_URL,USER_NAME,PASS_WORD 
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase02_caiwuyouhuicardlist_create(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        #self.assert_(driver.title, u"财务")
        time.sleep(2)
        self.assertEqual(driver.title,u"财务")
        #driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown a.dropdown-toggle").click()
       #driver.find_element_by_link_text(u"优惠券组").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a").click()
        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title,u"财务")
        #driver.find_element_by_link_text(u"生成券").click()
        driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:nth-child(1) td:nth-child(11) a:nth-child(2)").click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        #driver.find_element_by_name("commit").click()
        #print  "size is ",driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:last-child td:nth-child(11) a").len
        time.sleep(1)
        winBeforeHandle = driver.current_window_handle
        winHandles = driver.window_handles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
        driver.find_element_by_css_selector("div.container form.form-horizontal.coupon_list input.button").click()
        #html body div.container form.form-horizontal.coupon_list input.button
        #self.assert_(driver.title, u"财务")
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
