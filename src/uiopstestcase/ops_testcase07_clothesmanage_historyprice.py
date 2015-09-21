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
class OpsTestcase07clothesmanagehistoryprice(unittest.TestCase):
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
    
    def test_ops_testcase07_clothesmanageendprice(self):
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
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_clothesmanage+")>a").click()
        driver.implicitly_wait(30)
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_css_selector("ul.nav.navbar-nav>li:nth-child("+str(8)+").dropdown>ul.dropdown-menu>li:nth-child("+str(3)+")>a").click()#.send_keys(Keys.ENTER)
        #driver.find_element_by_css_selector("div.container>div>ul.nav.navbar-nav>li:nth-child("+str(7)+").dropdown>ul.dropdown-menu>li:nth-child("+str(2)+")>a").send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div.container>div>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_clothesmanage+").dropdown>ul.dropdown-menu>li:nth-child("+appobjectops.ops_tab_clothesmanage_historyprice+")>a").send_keys(Keys.ENTER)
        #driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+").dropdown>ul.dropdown-menu>li:nth-child(3)>a").click()#.send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        print driver.title
        #html body div#container.container form table tbody tr td div.input-group select#category_id.form-control option
        pinleiname=driver.find_element_by_css_selector("div#container.container form table tbody tr td:nth-child(2) div.input-group select#category_id.form-control option:nth-child(2)").text
        Select(driver.find_element_by_id("category_id")).select_by_visible_text(pinleiname)
        #html body div#container.container form table tbody tr td div.input-group select#city_id.form-control option
        cityname=driver.find_element_by_css_selector("div#container.container form table tbody tr td:nth-child(4) div.input-group select#city_id.form-control option:nth-child(2)").text
        Select(driver.find_element_by_id("city_id")).select_by_visible_text(cityname)
        print pinleiname,cityname
        #Select(driver.find_element_by_id("city_id")).select_by_visible_text(u"北京")
        driver.find_element_by_id("query_cloth_price").click()
        
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
