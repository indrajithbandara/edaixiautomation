#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectops,ops_utiltools
class OpsTestcase04Categorymanage(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectops.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        #conf.read("C:/edaixi_testdata/userdata_ops.conf")
        conf.read(ops_utiltools.getopsconfigpath())
        global CAIWU_URL,USER_NAME,PASS_WORD
        OPS_URL = conf.get("opssection", "uihostname")
        USER_NAME = conf.get("opssection", "uiadminusername")
        PASS_WORD = conf.get("opssection", "uiadminpassword")
        print OPS_URL,USER_NAME,PASS_WORD  
        self.base_url = OPS_URL
        #self.base_url = "http://ops05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_testcase04_categorymanage(self):
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
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        
        #driver.find_element_by_link_text(u"类目管理").click()
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(4)+") a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child("+str(4)+").dropdown ul.dropdown-menu li:nth-child(1) a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_css_selector("li.dropdown.open > ul.dropdown-menu > li > a").click()
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_css_selector("div#container.container a.btn.btn-sm.btn-info").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
#         driver.find_element_by_css_selector("li.dropdown.open > ul.dropdown-menu > li > a").click()
#         driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_id("category_form_name").clear()
        driver.find_element_by_id("category_form_name").send_keys(u"洗内裤")
        #Select(driver.find_element_by_id("category_form_ability_name")).select_by_visible_text(u"快洗")
#         driver.find_element_by_name("commit").click()
#         driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[9]").click()
#         driver.find_element_by_id("category_form_name").clear()
#         driver.find_element_by_id("category_form_name").send_keys(u"洗口罩")
#         driver.find_element_by_name("commit").click()
        
        
        #driver.find_element_by_id("service_category_form_name").clear()
        #driver.find_element_by_id("service_category_form_name").send_keys("addleimu")
#         selectempname=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body form#new_service_category_form.form-horizontal.new_service_category_form div.form-group.select.required.service_category_form_ability_name div.col-sm-8 select#service_category_form_ability_name.select.required.form-control option:nth-child(2)").text
#         Select(driver.find_element_by_id("service_category_form_ability_name")).select_by_visible_text(selectempname)
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info
        #driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[6]").click()
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info").click()
        driver.find_element_by_id("category_form_name").clear()
        driver.find_element_by_id("category_form_name").send_keys(u"洗口罩")
        driver.find_element_by_name("commit").click()
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
