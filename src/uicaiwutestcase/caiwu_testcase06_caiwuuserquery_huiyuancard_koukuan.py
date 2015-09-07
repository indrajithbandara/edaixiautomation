# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
from selenium.webdriver.support.ui import WebDriverWait 
import appobjectcaiwu
class CaiwuTestcase06CaiwuuserqueryHuiyuncardKoukuan(unittest.TestCase):
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
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase06_caiwuuserquery_Huiyuncard_Koukuan(self):
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
                #driver.find_element_by_link_text(u"会员卡").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(7).dropdown a.dropdown-toggle").click()
        #driver.find_element_by_link_text(u"会员卡查询").click()
        time.sleep(1)
        self.assertEqual(driver.title, u"财务")
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(7).dropdown ul.dropdown-menu li:first-child a").click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        time.sleep(1)
        self.assertEqual(driver.title, u"财务")
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys("18888888888")
        driver.find_element_by_xpath("(//input[@name='commit'])[2]").click()
        
        huiyuancardnum=driver.find_element_by_css_selector("div.container > table.table.table-bordered.table-striped > tbody > tr:last-child  > td >a").text
        print huiyuancardnum
        driver.find_element_by_link_text(huiyuancardnum).click()
        
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed())
        
        #driver.find_element_by_link_text(u"扣 款").click()
        driver.find_element_by_css_selector("div.container>a:last-child.btn.btn-sm.btn-primary").click()
        
        self.assertEqual(driver.title, u"财务")
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
        
        #useridnum=driver.find_element_by_css_selector("div.container > table.table.table-striped.table-bordered > tbody > tr:last-child  > td >a").text
        #driver.find_element_by_link_text(useridnum).click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed())
        
        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title, u"财务")
   
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
