#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
from selenium.webdriver.common.action_chains import ActionChains
import appobjectwechat,wechat_end_utiltools
#s@two-dimension code
class OpsTestcase01Permissionmanagepermission(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwechat.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wechat_end_utiltools.getwechatendconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiusername")
        PASS_WORD = conf.get("opssection", "uipassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase01_permissionmanage_permission(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #html body div#container.container h3.text-center.text-primary a.btn.btn-success.text-center
        #driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        #loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        loginclick=driver.find_element_by_css_selector(appobjectwechat.permloginClickButton)
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        time.sleep(2)
        driver.find_element_by_css_selector(appobjectops.clickPermissionLink).click()
        #permissionlinkclick=driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle")
        #ActionChains(driver).double_click(permissionlinkclick).perform()
        #driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle").click()
        #driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:first-child.dropdown ul.dropdown-menu li:first-child a").click()
        #driver.find_element_by_link_text(u"权限管理").click()
        #driver.find_element_by_css_selector("ul.nav.navbar-nav > li:first-child.dropdown > ul.dropdown-menu > li:first-child > a").send_keys(Keys.ENTER)
        #ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        #permissionclick=driver.find_element_by_css_selector("ul.nav.navbar-nav > li:first-child.dropdown > ul.dropdown-menu > li:first-child a")
        #ActionChains.click(permissionclick)
        #ActionChains(driver)..sigle_click(permissionclick).perform()
        #driver.find_element_by_link_text(u"权限管理").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[1]/ul/li[1]/a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.panle-body table.table.table-striped tbody tr:first-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success").click()
        driver.find_element_by_css_selector(appobjectops.clickPermissionButton).click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("worker_is_admin").click()
        driver.find_element_by_id("worker_is_city_manager").click()
        #定位到要右击的元素
        #qqq =driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")
        #对定位到的元素执行鼠标右键操作
        #ActionChains(driver).context_click(qqq).perform()
        driver.find_element_by_css_selector(".btn.btn-info").click()

        print "ops persmission manage assert title is ",driver.title
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
