# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectops
class OpsTestcase11MarketingToolsSendyouhuiquan(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectops.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiadminusername")
        PASS_WORD = conf.get("opssection", "uiadminpassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase11_MarketingToolsSendyouhuiquan(self):
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
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(11)+") a").click()
        driver.implicitly_wait(10)
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_css_selector("div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child("+str(11)+").dropdown ul.dropdown-menu li:nth-child(2) a").send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_link_text(u"发送优惠券").click()
        #driver.find_element_by_id("send_coupon_form_fan_ids").clear()
        driver.find_element_by_id("send_coupon_form_fan_ids").send_keys("C:\\edaixi_testdata\\user1.txt")
        #driver.find_element_by_id("send_coupon_form_coupon_id").clear()
        driver.find_element_by_id("send_coupon_form_coupon_id").send_keys("544")
        driver.find_element_by_name("commit").click()
        #html body div#container.container div.alert.fade.in.alert-success

        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
#         youhuiquanresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
#         print youhuiquanresult
#         assert u"发送成功" in (youhuiquanresult)
        #self.assertAlmostEqual(youhuiquanresult, u"发送成功")
        #self.assertAlmostEqual(first, second, places, msg, delta)
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
