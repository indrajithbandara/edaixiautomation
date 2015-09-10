#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait 
import ConfigParser
import caiwu_edaixi_mysql
import appobjectcaiwu,caiwu_utiltools
class CaiwuTestcase01Caiwuordermanagementkoukuan(unittest.TestCase):
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
        #self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase01_caiwuordermanagementkoukuan(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        driver.implicitly_wait(20)
        self.assertEqual(driver.title,u"财务")
        #driver.find_element_by_link_text(u"财务单管理").click()
        driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:first-child a").click()
        driver.find_element_by_id("settlement_search_form_ordersn").clear()
        driver.find_element_by_id("settlement_search_form_ordersn").send_keys(caiwu_edaixi_mysql.ordersnnumber)
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title,u"财务")
        
        ordernumber=driver.find_element_by_css_selector("div.container>div#content div.panel.panel-primary>table.table.table-striped.list-table>tbody>tr:first-child>td:nth-child(3)>a").text
        print " the ordernumber is :",ordernumber
        driver.find_element_by_link_text(ordernumber).click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container div.info-div div.col-md-6 div.panel.panel-primary.checkout-order div.panel-heading").is_displayed()) 
    
        driver.find_element_by_id("remark_content").clear()
        driver.find_element_by_id("remark_content").send_keys("hello,testing")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title,u"财务")
        huiyuancardnum=driver.find_element_by_css_selector("div.container div.info-div div.col-md-6 div.panel.panel-primary.checkout-order div.panle-body div.orders_container table.table.table-striped tbody tr:nth-child(6) td:nth-child(4) a").text
        print " the huiyuancardnum is :",huiyuancardnum
        
        driver.find_element_by_link_text(huiyuancardnum).click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed())
        
        #driver.find_element_by_link_text(u"扣 款").click()
        driver.find_element_by_css_selector("div.container > a:last-child").click()
        self.assertEqual(driver.title,u"财务")
                
        winBeforeHandle = driver.current_window_handle
        #print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        #print "winHandles==",winHandles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
        #print driver.title 
        
        driver.find_element_by_id("icard_koukuan_form_money").clear()
        driver.find_element_by_id("icard_koukuan_form_money").send_keys("10")
        driver.find_element_by_id("btnOn").click()
        #self.assert_(driver.title, u"财务")
        self.assertEquals(driver.title,u"财务")
        caiwu_edaixi_mysql.getcloseconn()
        
        koukuansuccess=driver.find_element_by_css_selector("div.container div.alert.fade.in.alert-success").text
        
        print " the koukuansuccess is ",koukuansuccess
        #self.assertEqual(koukuansuccess,u"扣款成功")
        assert u"扣款成功" in koukuansuccess
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
