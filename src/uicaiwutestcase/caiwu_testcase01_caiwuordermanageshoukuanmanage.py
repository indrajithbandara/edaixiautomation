# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait 
import ConfigParser,MySQLdb
import caiwu_edaixi_mysql 
import appobjectcaiwu


class CaiwuTestcase01Caiwuordermanagementshoukuanmanagei(unittest.TestCase):
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
        #self.base_url = "http://caiwu05.edaixi.cn:81/"
        #file.close()

        self.base_url = CAIWU_URL
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase01_caiwuordermanagement_shoukuanmanage(self):
        driver = self.driver
        driver.get(self.base_url + "/")
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
        # null to query order
        Select(driver.find_element_by_id("settlement_search_form_pay_status")).select_by_visible_text(u"已付款")
        Select(driver.find_element_by_id("settlement_search_form_caiwu_status")).select_by_visible_text(u"未收款")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title,u"财务")
        time.sleep(2)
        driver.find_element_by_css_selector("tr:first-child > td:first-child.s_id > input[type=\"checkbox\"]").click()
        
        ordernumberconfirm=driver.find_element_by_css_selector("div#content > div.panel.panel-primary > table.table.table-striped.list-table > tbody > tr:first-child > td:nth-child(3) > a").text
        print " the ordernumberconfirm is ",ordernumberconfirm
        #html body div.container div#content > div.panel.panel-primary > table.table.table-striped.list-table > tbody > tr:first-child > td:nth-child(3) > a
        driver.find_element_by_css_selector("#piliang_queren_shoukuan > input[name=\"commit\"]").click()
          
#         winBeforeHandle = driver.current_window_handle
#         #print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         #print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
#         #print driver.title 
        time.sleep(1)
        successconfirmshoukuan=driver.find_element_by_css_selector("div.container div.alert.fade.in.alert-success").text
        
        print " the successconfirmshoukuan is ",successconfirmshoukuan
        assert u"成功确认收款" in successconfirmshoukuan
        #self.assertEqual(chongzhisuccess,u"充值成功")
        
                # ordernumber to query order
        driver.find_element_by_id("settlement_search_form_ordersn").clear()
        driver.find_element_by_id("settlement_search_form_ordersn").send_keys(ordernumberconfirm)
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        #html body div.container div#content div.panel.panel-primary table.table.table-striped.list-table tbody tr td span.label.label-danger
        shoukuanstatus=driver.find_element_by_css_selector("div#content > div.panel.panel-primary > table.table.table-striped.list-table > tbody > tr:first-child > td:nth-last-child(3) > span").text
        print shoukuanstatus
        #assert u"已收款" in shoukuanstatus
        self.assertEqual(shoukuanstatus,u"已收款")
        #html body div.container div.alert.fade.in.alert-success
        
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
