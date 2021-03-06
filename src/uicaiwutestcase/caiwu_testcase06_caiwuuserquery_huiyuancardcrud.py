#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
from selenium.webdriver.support.ui import WebDriverWait 
import appobjectcaiwu, caiwu_utiltools
class CaiwuTestcase06CaiwuuserqueryHuiyuancardcrud(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectcaiwu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        #@conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        conf.read(caiwu_utiltools.getcaiwuconfigpath())
        global CAIWU_URL,USER_NAME,PASS_WORD
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        USER_NAME = conf.get("caiwusection", "uiusername")
        PASS_WORD = conf.get("caiwusection", "uipassword")
        print CAIWU_URL,USER_NAME,PASS_WORD 
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase06_caiwuuserquery_huiyuancardcrud(self):
        driver = self.driver

        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        driver.implicitly_wait(30)
#         self.assertEqual(driver.title, u"财务")
 
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+appobjectcaiwu.caiwu_tab_caiwuuserquery+").dropdown a.dropdown-toggle").click()
        #driver.find_element_by_link_text(u"会员卡查询").click()
        time.sleep(1)
        self.assertEqual(driver.title, u"财务")
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+appobjectcaiwu.caiwu_tab_caiwuuserquery+").dropdown ul.dropdown-menu li:first-child a").click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        self.assertEqual(driver.title, u"财务")
        time.sleep(1)
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys("18888888888")
        driver.find_element_by_xpath("(//input[@name='commit'])[2]").click()
        
        huiyuancardnum=driver.find_element_by_css_selector("div.container > table.table.table-bordered.table-striped > tbody > tr:last-child > td > a").text
        print " the huiyuancardnum is :",huiyuancardnum
        driver.find_element_by_link_text(huiyuancardnum).click()
        #WebDriverWait(driver, 50).until(lambda the_driver: 
                                        #the_driver.find_element_by_css_selector("div.container > table.table.table-striped.table-bordered > tbody > tr:last-child > td > a").is_displayed())
        time.sleep(3)
        useridnum=driver.find_element_by_css_selector("div.container > table.table.table-striped.table-bordered > tbody > tr:last-child > td > a").text
        print " the useridnum is :",useridnum
  
        driver.find_element_by_link_text(useridnum).click()

        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title, u"财务")
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
