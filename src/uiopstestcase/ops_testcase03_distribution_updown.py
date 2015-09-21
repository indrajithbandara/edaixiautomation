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
class OpsTestcase01DistributionUpDown(unittest.TestCase):
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
    
    def test_ops_testcase03_Distribution_updown(self):
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
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectops.ops_tab_distribution+")>a").send_keys(Keys.ENTER)
        #div#container.container table.table.table-bordered.table-striped tbody tr: td a.btn.btn-sm.btn-danger
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        ##driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[3]/ul/li[3]/a").click()
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a
        downactivename=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a").text
        print " the downactivename is ",downactivename
        
        if downactivename == u"审核":
           driver.find_element_by_link_text(u"审核").click()
           self.assertEqual(driver.title, u"e袋洗城市运营后台")
           driver.find_element_by_link_text(u"同意").click()
           self.assertEqual(driver.title, u"e袋洗城市运营后台")
           #self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认上架这件商品吗[\s\S]$")
        elif downactivename == u"查看":
           driver.find_element_by_link_text(u"查看").click()
           self.assertEqual(driver.title, u"e袋洗城市运营后台")
           #self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认下架这件商品吗[\s\S]$")
        else:
           pass

        #html body div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown.open ul.dropdown-menu li a
#         downactivename=driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child").text
#         print downactivename
#         if downactivename == u"上架":
#            driver.find_element_by_link_text(u"上架").click()
#            self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认上架这件商品吗[\s\S]$")
#         elif downactivename == u"下架":
#            driver.find_element_by_link_text(u"下架").click()
#            self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认下架这件商品吗[\s\S]$")
#         else:
#            pass
    
        #print driver.title
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
