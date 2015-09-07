# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import appobjectops
class OpsTestcase05PriceClothes(unittest.TestCase):
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
    
    def test_ops_testcase05_PriceClothes(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print "the testcase test_ops_testcase05_PriceClothes is ",driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(5)+") a").click()
        #shtml body div#container.container ul#myTab.nav.nav-tabs li a.active
        #ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        #driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(3).dropdown ul.dropdown-menu li:nth-child(1) a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div#container.container a.btn.btn-sm.btn-info").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
                
        driver.find_element_by_id("supplier_good_form_name").clear()
        driver.find_element_by_id("supplier_good_form_name").send_keys("addleimu")
        driver.find_element_by_id("supplier_good_form_edaixi_price").clear()
        driver.find_element_by_id("supplier_good_form_edaixi_price").send_keys("100")
        driver.find_element_by_id("supplier_good_form_rongchang_price").clear()
        driver.find_element_by_id("supplier_good_form_rongchang_price").send_keys("100")
        driver.find_element_by_id("supplier_good_form_description").clear()
        driver.find_element_by_id("supplier_good_form_description").send_keys("addleimudescription")

        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-info
        #driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[6]").click()
        #sdriver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(5)+") a").click()
        #html body div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:first-child
        driver.find_element_by_css_selector("div#container.container>table.table.table-bordered.table-striped>tbody>tr:nth-child(2)>td:last-child>a:first-child").click()
        #driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child.btn.btn-sm.btn-info").click()
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("supplier_good_form_description").clear()
        driver.find_element_by_id("supplier_good_form_description").send_keys("addleimuedit")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #self.assert_(driver.title, u"e袋洗城市运营后台")  
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child.btn.btn-sm.btn-danger").click()
        time.sleep(2)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除[\s\S]$")
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
