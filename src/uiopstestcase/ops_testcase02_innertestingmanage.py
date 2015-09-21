#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser,random
# from xlwt.antlr import ifelse
import appobjectops,ops_utiltools
class OpsTestcase02innertestingmanage(unittest.TestCase):
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
    
    def test_ops_testcase02_innertestingmanage(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase test_ops_testcase02_innertestingmanage  is  ",driver.title,appobjectops.ops_tab_innertestingmanage
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        #html body div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li.dropdown a.dropdown-toggle
        #driver.find_element_by_css_selector("div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child("+appobjectops.ops_innertestingmanage+").dropdown a.dropdown-toggle").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(appobjectops.ops_tab_innertestingmanage)+")>a").click()
        time.sleep(2)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
#         driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+appobjectops.ops_innertestingmanage+").dropdown ul.dropdown-menu li:first-child a").click()
#         time.sleep(1)
        
        #driver.find_element_by_css_selector("div#container.container a.btn.btn-sm.btn-info.col-md-1").click()
        #html body div#container.container div.panel.panel-primary div.pnale-body table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child
        #driver.find_element_by_link_text(u"内测管理").click()
        driver.find_element_by_link_text(u"添 加").click()
        driver.find_element_by_id("gray_group_name").clear()
        driver.find_element_by_id("gray_group_name").send_keys(str("innertestname"+str(random.randint(0,999))))
        time.sleep(1)
        driver.find_element_by_name("commit").click()

        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("gray_group_name").clear()
        driver.find_element_by_id("gray_group_name").send_keys(str("innertestnameedit"+str(random.randint(0,99))))
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(2)
        self.assertEqual(u"确认是否删除？", self.close_alert_and_get_its_text())
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_id("search_name").clear()
        driver.find_element_by_id("search_name").send_keys("18888888888")
        
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_link_text(u"添 加").click()
        driver.find_element_by_id("gray_group_name").clear()
        driver.find_element_by_id("gray_group_name").send_keys("innertestnameedit")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_link_text(u"内测成员").click()
        driver.find_element_by_id("add_tel").clear()
        driver.find_element_by_id("add_tel").send_keys("zhangsan")
        driver.find_element_by_id("add_member").click()
        

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
