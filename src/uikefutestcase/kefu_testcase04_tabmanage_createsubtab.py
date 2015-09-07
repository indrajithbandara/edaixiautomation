# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser ,random
import appobjectkefu
class KefuTestcase04TabmanageCreatesubtab(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectkefu.GetInstance()
        #self.driver.implicitly_wait(30)
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_kefu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        KEFU_URL = conf.get("kefusection", "uihostname")
        USER_NAME = conf.get("kefusection", "uiusername")
        PASS_WORD = conf.get("kefusection", "uipassword")
        print KEFU_URL,USER_NAME,PASS_WORD  
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase04_tabmanage_createsubtab(self):
        driver = self.driver
        #driver.get(self.base_url + "/orders/new")
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        
        print driver.title
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child(4)>a").click()
        self.assertEqual(driver.title,u"客服系统")
        #driver.find_element_by_id("add_tag").click()
        
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered tbody tr:first-child td:nth-child(3) a#add_tag_1").send_keys(Keys.ENTER)
        #driver.find_element_by_css_selector("div#container.container div.col-sm-4 a#add_tag").send_keys(Keys.ENTER)
        #html body div#container.container div.col-sm-4 a#add_tag.btn.btn-success
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_id("tag_name").clear()
        driver.find_element_by_id("tag_name").send_keys("addsubtagluke"+str(random.randint(1,100)))
        
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[2]/div/input").click()
        driver.find_element_by_name("commit").click()
        #driver.find_element_by_link_text(u"标签管理").click()
        print driver.title
        assert u"客服系统" in driver.title


    
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
