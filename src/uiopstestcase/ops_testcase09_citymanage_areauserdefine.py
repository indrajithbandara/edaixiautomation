# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectops
class OpsTestcase09citymanageareauserdefine(unittest.TestCase):
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
    
    def test_ops_testcase09_citymanageareauserdefine(self):
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
                
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(9)+") a").click()
        driver.implicitly_wait(10)
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_link_text(u"区域").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        winBeforeHandle = driver.current_window_handle
        #print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        #print "winHandles==",winHandles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
                
        #html body div#container.container table.table.table-bordered.table-striped tbody tr td a.btn.btn-sm.btn-danger
        
        passOperation=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(3)>a").text
        print " THE passOperation is ",passOperation
#         driver.find_element_by_link_text(u"添加区域").click()
#         self.assertEqual(driver.title, u"e袋洗城市运营后台")
#         Select(driver.find_element_by_id("area_form_id")).select_by_visible_text(u"平谷区")
#         driver.find_element_by_name("commit").click()
#         self.assertEqual(driver.title, u"e袋洗城市运营后台")
        displayOperation=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(2)>a").text
        print " THE displayOperation is ",displayOperation
        
        kuaixiOperation=driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(1)>a").text
        print " THE kuaixiOperation is ",kuaixiOperation
        
        if passOperation==u"开通":
             driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(3)>a").click()
             time.sleep(2)
             self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认开通[\s\S]$")
             self.assertEqual(driver.title, u"e袋洗城市运营后台")
        elif passOperation ==u"关闭":
             #driver.find_element_by_xpath(u"(//a[contains(text(),'关闭')])[37]").click()
             driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(3)>a").click()
             time.sleep(2)
             self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认关闭[\s\S]$")
             self.assertEqual(driver.title, u"e袋洗城市运营后台")
        if displayOperation==u"打开显示":
             driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(2)>a").click()
             time.sleep(2)
             self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认打开显示[\s\S]$")
             self.assertEqual(driver.title, u"e袋洗城市运营后台")
        elif displayOperation ==u"关闭显示":
             #print " the self.close_alert_and_get_its_text() is ",self.close_alert_and_get_its_text()
             #driver.find_element_by_xpath(u"(//a[contains(text(),'关闭')])[37]").click()
             driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(2)>a").click()
             time.sleep(2)
             self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认关闭显示[\s\S]$")
             self.assertEqual(driver.title, u"e袋洗城市运营后台")
             
        if kuaixiOperation==u"开通":
             driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(1)>a").click()
             time.sleep(2)
             self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认开通[\s\S]$")
             self.assertEqual(driver.title, u"e袋洗城市运营后台")
        elif kuaixiOperation ==u"关闭":
             #print " the self.close_alert_and_get_its_text() is ",self.close_alert_and_get_its_text()
             #driver.find_element_by_xpath(u"(//a[contains(text(),'关闭')])[37]").click()
             driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr>td:nth-last-child(1)>a").click()
             time.sleep(2)
             self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认关闭[\s\S]$")
             self.assertEqual(driver.title, u"e袋洗城市运营后台")
              
#         driver.find_element_by_xpath(u"(//a[contains(text(),'开通')])[19]").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认开通[\s\S]$")
#         driver.find_element_by_xpath(u"(//a[contains(text(),'关闭')])[37]").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认关闭[\s\S]$")
#         self.accept_next_alert = False
#         driver.find_element_by_xpath(u"(//a[contains(text(),'关闭显示')])[19]").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认关闭显示[\s\S]$")
#         driver.find_element_by_xpath(u"(//a[contains(text(),'开通')])[20]").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认开通[\s\S]$")
#         driver.find_element_by_xpath(u"(//a[contains(text(),'关闭')])[38]").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认关闭[\s\S]$")
#         driver.find_element_by_xpath(u"(//a[contains(text(),'关闭显示')])[19]").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认关闭显示[\s\S]$")
#         driver.find_element_by_link_text(u"打开显示").click()
#         self.assertRegexpMatches(self.close_alert_and_get_its_text(), ur"^确认打开显示[\s\S]$")
#         driver.find_element_by_link_text(u"自定义区域").click()
#         
#         self.assertEqual(driver.title, u"e袋洗城市运营后台")
#         driver.find_element_by_id("area_form_name_alias").clear()
#         driver.find_element_by_id("area_form_name_alias").send_keys(u"燕郊")
#         Select(driver.find_element_by_id("area_form_id")).select_by_visible_text(u"通州区")
#         driver.find_element_by_name("commit").click()
#         driver.find_element_by_link_text(u"城市管理").click()
#         driver.find_element_by_link_text(u"区域").click()

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
