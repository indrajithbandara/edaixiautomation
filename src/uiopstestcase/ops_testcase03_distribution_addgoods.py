# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
import appobjectops

class OpsTestcase03DistributionAddgoods(unittest.TestCase):
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
    
    def test_ops_testcase01_Distribution_addgoods(self):
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
                
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(3)+") a").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div#container.container a.btn.btn-info.btn-sm").click()
        #driver.find_element_by_link_text(u"分销系统").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("fenxiao_form_product_name").clear()
        driver.find_element_by_id("fenxiao_form_product_name").send_keys("addgoodsfenxiao")
        
        shitigoodname=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body form#new_fenxiao_form.form-horizontal.new_fenxiao_form div.form-group.select.optional.fenxiao_form_good_id div.col-sm-8 select#fenxiao_form_good_id.select.optional.form-control option:nth-child(3)").text
        #html body div#container.container div.panel.panel-primary div.pnale-body form#new_fenxiao_form.form-horizontal.new_fenxiao_form div.form-group.select.optional.fenxiao_form_good_id div.col-sm-8 select#fenxiao_form_good_id.select.optional.form-control option:nth-child(2)
        print " the shitigoodname is ",shitigoodname

        Select(driver.find_element_by_id("fenxiao_form_good_id")).select_by_visible_text(shitigoodname)
        driver.find_element_by_id("fenxiao_form_product_status").click()
        driver.find_element_by_id("fenxiao_form_start_time").click()
        driver.find_element_by_id("fenxiao_form_product_fenxiao_qudao_1").click()
        driver.find_element_by_id("fenxiao_form_product_fenxiao_qudao_2").click()
        driver.find_element_by_id("fenxiao_form_product_fenxiao_qudao_3").click()
        driver.find_element_by_name("commit").click()
        
        #driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child.btn.btn-sm.btn-info").click()
        #driver.find_element_by_link_text(u"编辑").click()
        #driver.find_element_by_id("fenxiao_form_product_name").clear()
        #driver.find_element_by_id("fenxiao_form_product_name").send_keys("addgoodsfenxiaoediting")
        #driver.find_element_by_name("commit").click()
        
        print " the submit add goods is ",driver.title
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
