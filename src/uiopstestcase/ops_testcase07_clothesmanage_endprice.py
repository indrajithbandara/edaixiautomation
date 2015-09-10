# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser
import random
import appobjectops
class OpsTestcase07clothesmanageendprice(unittest.TestCase):
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
    
    def test_ops_testcase07_clothesmanageendprice(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        #self.assert_(driver.title, u"e袋洗城市运营后台")
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
                
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(7)+") a").click()
        driver.implicitly_wait(10)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_css_selector("div.container>div>ul.nav.navbar-nav>li:nth-child("+str(7)+").dropdown>ul.dropdown-menu>li:nth-child(2)>a").send_keys(Keys.ENTER)
        #driver.find_element_by_css_selector("div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li:nth-child("+str(7)+").dropdown ul.dropdown-menu li:nth-child(2) a").send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        print driver.title
        
        randomstr=str(random.randint(0,999999))
        print randomstr
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_css_selector("div#container.container a.btn.btn-info.btn-sm").send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("yiwu_price_form_cloth_name").clear()
        driver.find_element_by_id("yiwu_price_form_cloth_name").send_keys(u"Test帽子夸张"+randomstr)
        driver.find_element_by_id("yiwu_price_form_cloth_price").clear()
        driver.find_element_by_id("yiwu_price_form_cloth_price").send_keys("100")
        driver.find_element_by_id("yiwu_price_form_cloth_yuanjia").clear()
        driver.find_element_by_id("yiwu_price_form_cloth_yuanjia").send_keys("120")
        driver.find_element_by_id("yiwu_price_form_wash_deadline_dian").clear()
        driver.find_element_by_id("yiwu_price_form_wash_deadline_dian").send_keys("11")
        driver.find_element_by_id("yiwu_price_form_wash_deadline_chang").clear()
        driver.find_element_by_id("yiwu_price_form_wash_deadline_chang").send_keys("11")
        cityna=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body form#new_yiwu_price_form.form-horizontal.new_yiwu_price_form div.form-group.select.required.yiwu_price_form_city_id div.col-sm-8 select#yiwu_price_form_city_id.select.required.form-control option:nth-child(2)").text
        Select(driver.find_element_by_id("yiwu_price_form_city_id")).select_by_visible_text(cityna)
        
        pinleina=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.pnale-body form#new_yiwu_price_form.form-horizontal.new_yiwu_price_form div.form-group.select.required.yiwu_price_form_category_id div.col-sm-8 select#yiwu_price_form_category_id.select.required.form-control option:nth-child(2)").text
        Select(driver.find_element_by_id("yiwu_price_form_category_id")).select_by_visible_text(pinleina)
    
        print cityna,pinleina
        driver.find_element_by_id("yiwu_price_form_smart_key").clear()
        driver.find_element_by_id("yiwu_price_form_smart_key").send_keys(randomstr)
        
        driver.find_element_by_name("commit").click()
        
        
        addinfo=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print " the addinfo is ",addinfo
        
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        randomstr2=str(random.randint(0,999999))
        print randomstr2
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child
        #driver.find_element_by_link_text(u"编辑").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child").send_keys(Keys.ENTER)
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        driver.find_element_by_id("yiwu_price_form_cloth_name").clear()
        driver.find_element_by_id("yiwu_price_form_cloth_name").send_keys(u"羽绒服1"+randomstr2)
        driver.find_element_by_id("yiwu_price_form_smart_key").clear()
        driver.find_element_by_id("yiwu_price_form_smart_key").send_keys("22")
        driver.find_element_by_name("commit").click()
        
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        time.sleep(1)
        #driver.find_element_by_id("yiwu_price_form_smart_key").clear()
        #driver.find_element_by_id("yiwu_price_form_smart_key").send_keys(randomstr2)
        #driver.find_element_by_name("commit").click()
        
        updateinfo=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print " the updateinfo is ",updateinfo
        assert u"衣物价格已更新" in updateinfo
        time.sleep(2)
        #html body div#container.container table.table.table-bordered.table-striped tbody tr td a.btn.btn-sm.btn-danger
        driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child").send_keys(Keys.ENTER)
        #driver.find_element_by_link_text(u"删除").click()
        #self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #print driver.switch_to_alert().text
        time.sleep(2)
        driver.switch_to_alert().accept()
        #self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除衣物价格[\s\S]$")
        
        #html body div#container.container div.alert.fade.in.alert-error
        deleteinfo=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-error").text
#         print deleteinfo
        print " the deleteinfo is ",deleteinfo
        #self.assertEqual(deleteinfo, u"衣物价格删除成功")
        assert u"衣物价格删除成功" in deleteinfo
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
       # 衣物价格已更新  衣物价格删除成功
    
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
