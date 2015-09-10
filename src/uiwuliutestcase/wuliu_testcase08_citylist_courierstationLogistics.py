# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
import appobjectwuliu
class WuliuTestcase08CitylistAddEdit(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "uiusername")
        PASS_WORD = conf.get("wuliusection", "uipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqlwuliudb")12121
        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        
        self.base_url = WULIU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase08_citylist_addedit(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")

        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+str(9)+").active a").click()
        
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:last-child").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
    
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        #driver.find_element_by_link_text(u"新建小e驿站").click()
        
        #html body div#container.container a.btn.btn-info.col-md-1
        driver.find_element_by_css_selector("div#container.container a.btn.btn-info.col-md-1").click()
        driver.find_element_by_id("outlet_form_title").clear()
        driver.find_element_by_id("outlet_form_title").send_keys(u"小e驿站test")
        
        driver.find_element_by_id("outlet_form_tel").clear()
        driver.find_element_by_id("outlet_form_tel").send_keys("18701112200")
        
        driver.find_element_by_id("outlet_form_usertel").clear()
        driver.find_element_by_id("outlet_form_usertel").send_keys(u"测试张三")
        
        #html body div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.required.outlet_form_area div.col-sm-8 select#outlet_form_area.select.required.form-control option:nth-child(2)
        outletarea=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.required.outlet_form_area div.col-sm-8 select#outlet_form_area.select.required.form-control option:nth-child(2)").text
        Select(driver.find_element_by_id("outlet_form_area")).select_by_visible_text(outletarea)
        
        driver.find_element_by_id("outlet_form_address").clear()
        driver.find_element_by_id("outlet_form_address").send_keys(u"朝阳区酒仙桥")
        
        driver.find_element_by_id("get_pos").click()
        driver.find_element_by_name("commit").click()
        
        
        #driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_css_selector("div#container.container table.table.table-striped tbody tr:nth-child(2) td:last-child a").click()
        #html body div#container.container table.table.table-striped tbody tr:nth-child(2) td:last-child a.btn.btn-primary.btn-sm
        driver.find_element_by_id("outlet_form_title").clear()
        driver.find_element_by_id("outlet_form_title").send_keys(u"小e驿站test修改")
        driver.find_element_by_name("commit").click()
        
        
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"小e驿站test")
        driver.find_element_by_name("commit").click()
        
        print driver.title
        
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
