#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectops,ops_utiltools
class OpsTestcase04Categoryedittemplatexishechipin(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
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
    
    def test_ops_testcase04_Categoryedittemplatexishechipin(self):
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
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_Category+") a").click()
        
        #ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+appobjectops.ops_tab_Category+").dropdown ul.dropdown-menu li:nth-child(2) a").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_css_selector("div#container.container ul#myTab.nav.nav-tabs li:nth-child(4) a").click()
        #driver.find_element_by_css_selector("div#container.container ul#myTab.nav.nav-tabs li:first-child a.active").click()
        time.sleep(1)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        #html body div#container.container a.btn.btn-sm.btn-info
        driver.find_element_by_css_selector("div#container.container>a.btn.btn-sm.btn-info").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_id("service_good_form_name").clear()
        driver.find_element_by_id("service_good_form_name").send_keys("xiyileimutemplate")
        driver.find_element_by_id("service_good_form_price").clear()
        driver.find_element_by_id("service_good_form_price").send_keys("100")
        driver.find_element_by_id("service_good_form_unit_name").clear()
        driver.find_element_by_id("service_good_form_unit_name").send_keys("edaixi")
        driver.find_element_by_id("service_good_form_description").clear()
        driver.find_element_by_id("service_good_form_description").send_keys("hellp")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[5]").click()
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info").click()
        driver.find_element_by_id("service_good_form_name").clear()
        driver.find_element_by_id("service_good_form_name").send_keys("xiyileimutemplateaedit")
        driver.find_element_by_id("service_good_form_description").clear()
        driver.find_element_by_id("service_good_form_description").send_keys("hellp11")
        driver.find_element_by_name("commit").click()
                
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
    
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
