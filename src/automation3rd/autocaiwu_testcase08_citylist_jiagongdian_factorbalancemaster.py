#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
import appobjectauto3rd,auto3rd_utiltools

class CaiwuTestcase08CitylistJiagongdianFactoryBalanceMaster(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectauto3rd.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        #conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        conf.read(auto3rd_utiltools.get3rdcaiwupath())
        global CAIWU_URL,MasterUSER_NAME,MasterPASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        MasterUSER_NAME = conf.get("caiwusection", "uimasterusername")
        MasterPASS_WORD = conf.get("caiwusection", "uimasterpassword")
        print CAIWU_URL,MasterUSER_NAME,MasterPASS_WORD
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqlcaiwudb")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        
        self.base_url = CAIWU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase08_citylist_jiagongdian_factorybalance_master(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")
        loginclick=driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center")
        #loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(MasterUSER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(MasterPASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase test_caiwu_testcase08_citylist_jiagongdian_factorybalance_master is ",driver.title
        #self.assertTrue(driver.title, u"财务")
        
        
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(8).active a").click()
        #driver.find_element_by_css_selector("div.container > div > ul > li:nth-child(6) >a").click()

        #self.assertEqual(driver.title, u"财务")
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(9)").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
    
        #self.assertEqual(driver.title, u"财务")
        time.sleep(2)
        driver.find_element_by_css_selector("div.container > div > ul > li:nth-child(1) >a").click()
        #driver.find_element_by_link_text(u"结算管理").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"BJ加工店-长楹天街-店")
        #driver.find_element_by_id("title").send_keys(u"test")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"财务")
        time.sleep(1)
        driver.find_element_by_link_text(u"结算列表").click()
        self.assertEqual(driver.title, u"财务")
        time.sleep(1)
        driver.find_element_by_link_text(u"明细").click()
        self.assertEqual(driver.title, u"财务")
        time.sleep(1)
        driver.find_element_by_link_text(u"审核通过").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认审核通过[\s\S]$")
 
        self.assertEqual(driver.title, u"财务")
                
        shenhetongguo=driver.find_element_by_css_selector("div.container table.table.table-striped tbody tr:last-child td:nth-last-child(2)").text
        print " the shenhetongguo is ",shenhetongguo
        self.assertEqual(shenhetongguo, u"审核通过")
                
        #html body div.container table.table.table-striped tbody tr:last-child td:nth-child(2)
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
