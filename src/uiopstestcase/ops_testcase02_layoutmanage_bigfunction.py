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
import appobjectops,ops_utiltools
class OpsTestcase02LayoutManageBigFunction(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectops.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(ops_utiltools.getopsconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiadminusername")
        PASS_WORD = conf.get("opssection", "uiadminpassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase02_layoutmanage_bigfunction(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        #driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:first-child.dropdown ul.dropdown-menu li:nth-child(2) a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div#container.container a.btn.btn-sm.btn-info.col-md-1").click()
       
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("banner_title").clear()
        driver.find_element_by_id("banner_title").send_keys("bigbutton")
        
        linktypename=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body form#new_banner.form-horizontal.new_banner div:nth-child(3).form-group.select.optional.banner_website_type div.col-sm-8 select#banner_website_type.select.optional.form-control option:nth-child(2)").text
        
        Select(driver.find_element_by_id("banner_website_type")).select_by_visible_text(linktypename)
        driver.find_element_by_id("banner_description").clear()
        driver.find_element_by_id("banner_description").send_keys("hello")
        
        driver.find_element_by_id("banner_inner_url").clear()
        driver.find_element_by_id("banner_inner_url").send_keys("http://localhost.cn")
        
        driver.find_element_by_id("banner_inner_title").clear()
        driver.find_element_by_id("banner_inner_title").send_keys("hello")
        #driver.find_element_by_id("banner_ios").clear()
        driver.find_element_by_id("banner_ios").send_keys("C:\edaixi_testdata\edaixi_ops_banner1.jpg")
        #driver.find_element_by_id("banner_android").clear()
        driver.find_element_by_id("banner_android").send_keys("C:\edaixi_testdata\edaixi_ops_banner2.jpg")
        #driver.find_element_by_id("banner_web").clear()
        driver.find_element_by_id("banner_web").send_keys("C:\edaixi_testdata\edaixi_ops_banner3.jpg")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body table.table.table-striped tbody tr:first-child td:last-child a:nth-child(2).btn.btn-sm.btn-info").click()
        driver.find_element_by_id("banner_description").clear()
        driver.find_element_by_id("banner_description").send_keys("hello1111")
        
        driver.find_element_by_id("banner_inner_url").clear()
        driver.find_element_by_id("banner_inner_url").send_keys("http://localhost.cn")
        
        driver.find_element_by_id("banner_inner_title").clear()
        driver.find_element_by_id("banner_inner_title").send_keys("hello")
        
        driver.find_element_by_name("commit").click()
        
        #driver.find_element_by_link_text(u"删除").click()

        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        downactivename=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body table.table.table-striped tbody tr:first-child td:last-child a:first-child").text
        print downactivename
        if downactivename == u"下线":
           driver.find_element_by_link_text(u"下线").click()
           time.sleep(2)
           self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认下线[\s\S]$")
           self.assertEqual(driver.title, u"e袋洗城市运营后台")
           driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>div.pnale-body>table.table.table-striped>tbody>tr:first-child>td:last-child>a:last-child").click()
           time.sleep(2)
           self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除图片[\s\S]$")
        elif downactivename == u"激活":
           driver.find_element_by_link_text(u"激活").click()
           time.sleep(2)
           self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认激活[\s\S]$")
           self.assertEqual(driver.title, u"e袋洗城市运营后台")
           driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>div.pnale-body>table.table.table-striped>tbody>tr:first-child>td:last-child>a:nth-child(3)").click()
           time.sleep(2)
           self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除图片[\s\S]$")
        else:
           pass
           driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>div.pnale-body>table.table.table-striped>tbody>tr:first-child>td:last-child>a:nth-child(3)").click()
           time.sleep(2)
           self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除图片[\s\S]$")
        
        
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
