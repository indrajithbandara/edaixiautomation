# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
from selenium.webdriver.support.ui import WebDriverWait 
import appobjectcaiwu,caiwu_utiltools
class CaiwuTestcase00rdt6caiwushiticard(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectcaiwu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        USER_NAME = conf.get("caiwusection", "uirdt6username")
        PASS_WORD = conf.get("caiwusection", "uirdt6password")
        print CAIWU_URL,USER_NAME,PASS_WORD 
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase00_rdt6caiwushiticard(self):
        driver = self.driver
        driver.get(self.base_url + "/")
  
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        self.assertEqual(driver.title,u"财务")
        #driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_css_selector("div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child(2) a").click()
        #driver.find_element_by_link_text(u"优惠券组").click()
        self.assertEqual(driver.title,u"财务")
        #html body div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a
        driver.find_element_by_css_selector("ul.nav.navbar-nav>li:nth-child(2).dropdown>ul.dropdown-menu>li:first-child>a").click()
        self.assertEqual(driver.title,u"财务")
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_css_selector("div.container a.btn.btn-info.col-md-1").click()
        time.sleep(2)
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        self.assertEqual(driver.title,u"财务")
        currenttime=str(time.strftime("%d", time.localtime()))
        starttime=str(time.strftime("%Y-%m-", time.localtime()))
        endtime=str(int(currenttime)+1)
        firsttime=starttime+currenttime
        #firsttime="2015-07-31" #print currenttime#print endtime
        finaltime=starttime+endtime
        print firsttime,finaltime
        
        driver.find_element_by_id("rcard_list_form_title").clear()
        driver.find_element_by_id("rcard_list_form_title").send_keys("testshitika")
        driver.find_element_by_id("rcard_list_form_price").clear()
        driver.find_element_by_id("rcard_list_form_price").send_keys("100")
        
        driver.find_element_by_id("rcard_list_form_apply_department").clear()
        driver.find_element_by_id("rcard_list_form_apply_department").send_keys("tech")
        driver.find_element_by_id("rcard_list_form_applicant").clear()
        driver.find_element_by_id("rcard_list_form_applicant").send_keys("luke")
        driver.find_element_by_id("rcard_list_form_city").clear()
        driver.find_element_by_id("rcard_list_form_city").send_keys("beijing")
        
        driver.find_element_by_id("rcard_list_form_starttime").clear()
        driver.find_element_by_id("rcard_list_form_starttime").send_keys(str(caiwu_utiltools.get_day_of_day(1)))
        
        driver.find_element_by_id("rcard_list_form_endtime").clear()
        driver.find_element_by_id("rcard_list_form_endtime").send_keys(str(caiwu_utiltools.get_day_of_day(5)))
        
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title,u"财务")
        time.sleep(2)
        #driver.find_element_by_link_text(u"编辑").click()
        
        #html body div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-last-child(3) a.btn.btn-sm.btn-info
        
        driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-last-child(3) a.btn.btn-sm.btn-info").click()
        driver.find_element_by_id("rcard_list_form_title").clear()
        driver.find_element_by_id("rcard_list_form_title").send_keys("testshitikaedit")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title,u"财务")
        time.sleep(1)
        
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("test")
        driver.find_element_by_name("commit").click()
        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title,u"财务")
        
        time.sleep(2)
        driver.find_element_by_css_selector("div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child(2) a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.nav.navbar-nav>li:nth-child(2).dropdown>ul.dropdown-menu>li:nth-child(2)>a").click()
        self.assertEqual(driver.title,u"财务")
        time.sleep(1)
        driver.find_element_by_id("sn_code").clear()
        driver.find_element_by_id("sn_code").send_keys("test")
        driver.find_element_by_name("commit").click()
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
