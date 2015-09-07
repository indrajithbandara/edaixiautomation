# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,string
from selenium.webdriver.support.ui import WebDriverWait 
import appobjectcaiwu
class CaiwuTestcase03CaiwushiticardCreate(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectcaiwu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        USER_NAME = conf.get("caiwusection", "uiusername")
        PASS_WORD = conf.get("caiwusection", "uipassword")
        print CAIWU_URL,USER_NAME,PASS_WORD 
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase03_caiwushiticard_create(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        self.assertEqual(driver.title, u"财务")
        
        #driver.find_element_by_link_text(u"实体卡").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(3).dropdown a.dropdown-toggle").click()
        #driver.find_element_by_link_text(u"实体卡列表").click()
        self.assertEqual(driver.title, u"财务")
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(3).dropdown ul.dropdown-menu li:first-child a").click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        time.sleep(1)
        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title, u"财务")
        #driver.find_element_by_link_text(u"生成卡").click()
        driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-child(7) a:nth-child(2).btn.btn-sm.btn-info").click()
        winBeforeHandle = driver.current_window_handle
        winHandles = driver.window_handles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
        time.sleep(1)
        
        #rcard_list_amount
        driver.find_element_by_id("rcard_list_amount").clear()
        driver.find_element_by_id("rcard_list_amount").send_keys("1")
        driver.find_element_by_css_selector("div.container form.form-horizontal.rcard_list input.button").click()
        #driver.find_element_by_name("commit").click()
        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title, u"财务")
        
        shiticardcreate=driver.find_element_by_css_selector("html body div.container div.alert.fade.in.alert-success").text
        print " the shiticardcreate is ",shiticardcreate
        assert u"实体卡生成任务提交成功" in shiticardcreate
        #html body div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:first-child
        createshiticarednum=driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:first-child").text
        print " the createshiticarednum is ",createshiticarednum
        
        createshiticarednumnew=''.join(createshiticarednum.split(' '))
        print " the createshiticarednumnew is ",createshiticarednumnew
        
#         driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(3).dropdown ul.dropdown-menu li:first-child a").click()
#         #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
#         time.sleep(1)
#         #self.assert_(driver.title, u"财务")
#         self.assertEqual(driver.title, u"财务")
#         driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-child(7) a:nth-child(4)").click()
#         winBeforeHandle = driver.current_window_handle
#         winHandles = driver.window_handles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
#         time.sleep(1)
#         driver.find_element_by_id("rcard_recharge_form_from_no").clear()
#         driver.find_element_by_id("rcard_recharge_form_from_no").send_keys(createshiticarednumnew)
#         driver.find_element_by_id("rcard_recharge_form_to_no").clear()
#         driver.find_element_by_id("rcard_recharge_form_to_no").send_keys(createshiticarednumnew)
#         driver.find_element_by_id("rcard_recharge_form_xiaoshoujia").clear()
#         driver.find_element_by_id("rcard_recharge_form_xiaoshoujia").send_keys("100")
#         driver.find_element_by_id("rcard_recharge_form_chongzhijine").clear()
#         driver.find_element_by_id("rcard_recharge_form_chongzhijine").send_keys("100")
#         
#         driver.find_element_by_css_selector("div.container form#new_rcard_recharge_form.form-horizontal.new_rcard_recharge_form input.button.btn.btn-info").click()
#         #html body div.container form#new_rcard_recharge_form.form-horizontal.new_rcard_recharge_form input.button.btn.btn-info
#         
#         chiticardcreate=driver.find_element_by_css_selector("html body div.container div.alert.fade.in.alert-success").text
#         print " the chiticardcreate is ",chiticardcreate
        time.sleep(2)
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(3).dropdown a.dropdown-toggle").click()
        #driver.find_element_by_link_text(u"实体卡列表").click()
        self.assertEqual(driver.title, u"财务")
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(3).dropdown ul.dropdown-menu li:last-child a").click()
        
        driver.find_element_by_id("sn_code").clear()
        driver.find_element_by_id("sn_code").send_keys(createshiticarednumnew)
        #driver.find_element_by_name("commit").click()
        driver.find_element_by_css_selector(".btn.btn-default").click()
        self.assertEqual(driver.title, u"财务")
        
        driver.find_element_by_css_selector("div.container a.btn.btn-sm.btn-info.col-md-1").click()
        #html body div.container a.btn.btn-sm.btn-info.col-md-1
        time.sleep(2)
        winBeforeHandle = driver.current_window_handle
        winHandles = driver.window_handles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)

        
        driver.find_element_by_id("rcard_recharge_form_xiaoshoujia").clear()
        driver.find_element_by_id("rcard_recharge_form_xiaoshoujia").send_keys("100")
        driver.find_element_by_id("rcard_recharge_form_chongzhijine").clear()
        driver.find_element_by_id("rcard_recharge_form_chongzhijine").send_keys("100")
        
        driver.find_element_by_css_selector("div.container form#new_rcard_recharge_form.form-horizontal.new_rcard_recharge_form input.button.btn.btn-info").click()
        
        self.assertEqual(driver.title, u"财务")
        chongzhisuccess=driver.find_element_by_css_selector("div.container div.alert.fade.in.alert-success").text
        print " the chongzhisuccess is ",chongzhisuccess
        #html body div.container div.alert.fade.in.alert-success
        assert u"充值成功" in chongzhisuccess
        
        #self.assertEqual(chongzhisuccess, u"充值成功")
        
        chongzhimoney=driver.find_element_by_css_selector("html body div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-child(4)").text
        print " the chongzhimoney is ",chongzhimoney
        
        chongzhimoneyint=int(float(chongzhimoney))
        print " the chongzhimoneyint is ",chongzhimoneyint
        
        if chongzhimoneyint>0:
            pass
        else:
            raise NameError ("chongzhi money is 0")
        
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
