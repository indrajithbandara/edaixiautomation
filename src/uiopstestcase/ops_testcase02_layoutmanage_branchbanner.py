# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OpsTestcase01PermissionmanagePermission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase01_permissionmanage_permission(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        print driver.title

        #self.assert_(driver.title, u"e袋洗城市运营后台")
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_link_text(u"版面管理").click()
        
        driver.find_element_by_link_text(u"顶部banner图片").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_link_text(u"上移").click()
        
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认上移[\s\S]$")
        driver.find_element_by_link_text(u"下移").click()
        
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认下移[\s\S]$")
        driver.find_element_by_xpath(u"(//a[contains(text(),'取消')])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认取消选择[\s\S]$")
        driver.find_element_by_link_text(u"选择").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认选择[\s\S]$")
        
        driver.find_element_by_xpath("//li[2]/a/b").click()

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
