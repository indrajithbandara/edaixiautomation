# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser,random
#from uiappobject.appobjectops import appobjectops
import appobjectops
class OpsTestcase08rechargereturncrash(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectops.GetInstance()
        #self.driver =SingleWebDriver.getWebDriverInstance(self)
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
    
    def test_ops_testcase08_rechargereturncrash(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector(appobjectops.loginClickButton).click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print driver.title
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        
        #driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+str(8)+") a").click()
        #getWebElementOpsRechargereturncrash(driver).click()
        driver.find_element_by_css_selector(appobjectops.clickRechargeReturncrashLink).click()
        driver.implicitly_wait(10)
        print driver.title
        #driver.find_element_by_css_selector("div#container.container div a.btn.btn-info.btn-info").send_keys(Keys.ENTER)
        driver.find_element_by_css_selector(appobjectops.clickNewButtonRechargeReturncrash).send_keys(Keys.ENTER)
        #html body div#container.container div a.btn.btn-info.btn-info
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_link_text(u"新 建").click()
        print " the str(random.randint(10, 100)) is ",str(random.randint(10, 100))
        driver.find_element_by_id("recharge_setting_form_money_give").clear()
        driver.find_element_by_id("recharge_setting_form_money_give").send_keys(str(random.randint(10,100)))
                                                                                
        driver.find_element_by_id("recharge_setting_form_min").clear()
        driver.find_element_by_id("recharge_setting_form_min").send_keys(str(random.randint(10,100)))
#         driver.find_element_by_id("recharge_setting_form_max").clear()
#         driver.find_element_by_id("recharge_setting_form_max").send_keys("1000")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #addchizhifanxian=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        addchizhifanxian=driver.find_element_by_css_selector(appobjectops.addchizhifanxianResult).text
        print addchizhifanxian
        assert u"返现设置已添加"  in (addchizhifanxian)
        #self.assertEqual(addchizhifanxian, u"返现设置已添加")
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:first-child").send_keys(Keys.ENTER)
        driver.find_element_by_css_selector(appobjectops.clickEditButtonRechargeReturncrash).click()
        #driver.find_element_by_link_text(u"编辑").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        driver.find_element_by_id("recharge_setting_form_min").clear()
        driver.find_element_by_id("recharge_setting_form_min").send_keys(str(random.randint(10, 100)))
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #html body div#container.container div.alert.fade.in.alert-success
        #editchizhifanxian=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        editchizhifanxian=driver.find_element_by_css_selector(appobjectops.editchizhifanxianresult).text
        print editchizhifanxian
        assert u"返现设置已更新" in (editchizhifanxian)
        #self.assertEqual(editchizhifanxian, u"返现设置已更新")
        self.assertEqual(driver.title, u"e袋洗城市运营后台")
        #html body div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child.btn.btn-sm.btn-danger
        #driver.find_element_by_css_selector("div#container.container table.table.table-bordered.table-striped tbody tr:nth-child(2) td:last-child a:last-child").send_keys(Keys.ENTER)
        #driver.find_element_by_link_text(u"删除").click()
        driver.find_element_by_css_selector(appobjectops.clickDeleteButtonRechargeReturncrash).click()
        time.sleep(2)
        #self.assertEqual(u"确认删除", self.close_alert_and_get_its_text())
        self.assertEqual(u"确认删除", self.close_alert_and_get_its_text())
        #driver.find_element_by_link_text(u"城市管理").click()
        #html body div#container.container
        time.sleep(2)
        #deletechizhifanxian=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        deletechizhifanxian=driver.find_element_by_css_selector(appobjectops.deletechizhifanxianresult).text
        print deletechizhifanxian
        assert u"返现设置删除成功" in (deletechizhifanxian)
        #self.assertEqual(deletechizhifanxian, u"返现设置删除成功")
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
