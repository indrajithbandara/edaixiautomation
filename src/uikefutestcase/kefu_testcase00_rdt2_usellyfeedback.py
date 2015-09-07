# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectkefu
class KefuTestcase00rdt2usellyfeedbackl(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectkefu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_kefu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        KEFU_URL = conf.get("kefusection", "uihostname")
        USER_NAME = conf.get("kefusection", "rdt2uiusername")
        PASS_WORD = conf.get("kefusection", "rdt2uipassword")
        print KEFU_URL,USER_NAME,PASS_WORD  
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase00_rdt2_usellyfeedback(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(1)
        self.assertEqual(driver.title,u"客服系统")

        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child(3)>a").click()
        #driver.find_element_by_link_text(u"反馈总列表").click()
        #driver.find_element_by_link_text(u"踢").click()
        
#         print driver.title
#         if "We're sorry" in driver.title:
#             print "We're sorry, but something went wrong."
#             raise NameError
#         else:
#             pass
#         print driver.title
        #self.assertTrue("", "We're sorry")
        #self.assert_(driver.title, u"客服系统")
        
#         driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child(5)>a").click() 
#         self.assertEqual(driver.title,u"客服系统")
        
        driver.find_element_by_id("content").clear()
        driver.find_element_by_id("content").send_keys("hell,changyonghuifu")
        driver.find_element_by_name("commit").click()
        print driver.title
        assert u"客服系统" in driver.title
        time.sleep(2)
        
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child a").click()
        #self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确定删除[\s\S]$")
        self.assertEqual(driver.title,u"客服系统")
        
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
