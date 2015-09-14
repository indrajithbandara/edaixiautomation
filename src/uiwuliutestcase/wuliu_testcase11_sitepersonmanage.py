#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
from selenium.webdriver.common.action_chains import ActionChains
import appobjectwuliu,wuliu_utiltools

class WuliuTestcase11SitePersonManage(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wuliu_utiltools.getwuliuconfigpath()) 
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "uiusername")
        PASS_WORD = conf.get("wuliusection", "uipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        self.base_url = WULIU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase11_site_personmanage(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_css_selector("div.container>nav.collapse.navbar-collapse.bs-navbar-collapse>ul.nav.navbar-nav>li:last-child>a").click()
        self.assertEqual(driver.title, u"物流")
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:last-child.active a
#         driver.find_element_by_css_selector("div.container>nav.collapse.navbar-collapse.bs-navbar-collapse>ul.nav.navbar-nav>li:last-child>a").click()
#         
#         driver.find_element_by_id("ordersn").clear()
#         driver.find_element_by_id("ordersn").send_keys("110500367088")
#         driver.find_element_by_name("commit").click()
#         self.assertEqual(driver.title, u"物流")
#         
#         driver.find_element_by_id("seal_sn").clear()
#         driver.find_element_by_id("seal_sn").send_keys("E0000000006")
#         driver.find_element_by_name("commit").click()
#         self.assertEqual(driver.title, u"物流")
#         
#         driver.find_element_by_id("tel").clear()
#         driver.find_element_by_id("tel").send_keys("1888888888")
#         driver.find_element_by_name("commit").click()
#         self.assertEqual(driver.title, u"物流")
        

        driver.find_element_by_id("text").clear()
        driver.find_element_by_id("text").send_keys("1888888888")
        driver.find_element_by_name("commit").click()
        #driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        
#         driver.find_element_by_link_text(u"超时订单").click()
#         self.assertEqual(driver.title, u"物流")
#         driver.find_element_by_id("timeout_qu_list_btn").click()
#         driver.find_element_by_id("timeout_song_list_btn").click()
#         driver.find_element_by_id("warning_qu_list_btn").click()
#         driver.find_element_by_id("warning_song_list_btn").click()
#         self.assertEqual(driver.title, u"物流")
        
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
