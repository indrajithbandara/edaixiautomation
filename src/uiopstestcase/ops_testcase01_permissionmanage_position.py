#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
from selenium.webdriver.common.action_chains import ActionChains
import appobjectops, ops_utiltools

class OpsTestcase01PermissionmanagePosition(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectops.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(ops_utiltools.getopsconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiusername")
        PASS_WORD = conf.get("opssection", "uipassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase01_permissionmanage_position(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        #driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        loginclick=driver.find_element_by_css_selector(appobjectops.permloginClickButton)
        #loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        
#         self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle").click()
        driver.find_element_by_css_selector(appobjectops.clickPositionLink).click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("ul.dropdown-menu > li:nth-child(2) > a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_css_selector("div#container.container div#content-container a.btn.btn-info.col-md-1").click()
        driver.find_element_by_css_selector(appobjectops.clickPositionNewButton).click()
        #driver.find_element_by_link_text(u"新建").click()
        print "ops pozition manage assert title is ",driver.title
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        Select(driver.find_element_by_id("position_to_role_position")).select_by_visible_text(u"市场策划")
        Select(driver.find_element_by_id("position_to_role_role_key")).select_by_visible_text(u"市场经理")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[1]").click()
        #driver.find_element_by_css_selector("div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info").click()
        driver.find_element_by_css_selector(appobjectops.clickPositionEditButton).click()
        print driver.title
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        Select(driver.find_element_by_id("position_to_role_role_key")).select_by_visible_text(u"营销中心负责人")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[1]").click()
        #driver.find_element_by_css_selector("div#container.container div#content div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-danger").click()
        driver.find_element_by_css_selector(appobjectops.clickPositionDeleteButton).click()
        time.sleep(2)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除岗位角色映射[\s\S]$")
        #self.assert_(driver.title, u"e袋洗城市运营后台")
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
