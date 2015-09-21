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
class OpsTestcase07clothesmanageminor(unittest.TestCase):
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
    
    def test_ops_testcase07_clothesmanageminor(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print "the testcase test_ops_testcase07_clothesmanageminor is ",driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_clothesmanage+") a").click()
        driver.implicitly_wait(30)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child("+appobjectops.ops_tab_clothesmanage+").dropdown ul.dropdown-menu li:nth-child("+appobjectops.ops_tab_clothesmanage_minor+") a").send_keys(Keys.ENTER)
        
        print " the testcase test_ops_testcase07_clothesmanageminor is ",driver.title
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_link_text(u"洗衣").click()
        #driver.find_element_by_css_selector("div.container.container>ul#myTab.nav.nav-tabs>li:first-child>a").send_keys(Keys.ENTER)
        #driver.find_element_by_link_text(u"新 建").click()
        #html body div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        time.sleep(1)
        #driver.find_element_by_css_selector("div#container.container a.btn.btn-info.btn-sm").click()
        driver.find_element_by_link_text(u"新 建").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("yiwu_constant_form_value").clear()
        driver.find_element_by_id("yiwu_constant_form_value").send_keys("lukebrand")
        pinleiname=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body form#new_yiwu_constant_form.form-horizontal.new_yiwu_constant_form div.form-group.select.required.yiwu_constant_form_category_id div.col-sm-8 select#yiwu_constant_form_category_id.select.required.form-control option:nth-child(2)").text
        Select(driver.find_element_by_id("yiwu_constant_form_category_id")).select_by_visible_text(pinleiname)
        driver.find_element_by_name("commit").click()
    
        print driver.title
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
