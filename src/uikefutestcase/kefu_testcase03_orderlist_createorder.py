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
import PythonDateUtils,appobjectkefu,kefu_utiltools
class KefuTestcase03OrderlistCreateorder(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectkefu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(kefu_utiltools.getkefuconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_kefu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        KEFU_URL = conf.get("kefusection", "uihostname")
        USER_NAME = conf.get("kefusection", "uiusername")
        PASS_WORD = conf.get("kefusection", "uipassword")
        print KEFU_URL,USER_NAME,PASS_WORD  
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase03_orderlist_createorder(self):
        driver = self.driver
        #driver.get(self.base_url + "/orders/new")
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        
        print " the testcase test_kefu_testcase03_orderlist_createorder is ",driver.title,USER_NAME,PASS_WORD
        self.assertEqual(driver.title,u"客服系统")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child(3)>a").click()
        self.assertEqual(driver.title,u"客服系统")
        #html body div#container.container>div#content-container>a.btn.btn-info.col-md-1
        #createorderclick=driver.find_element_by_css_selector("div#container.container>div#content-container>a.btn.btn-info.col-md-1")
        createorderclick=driver.find_element_by_xpath("/html/body/div[2]/div/form/a[1]")
        ActionChains(driver).double_click(createorderclick).perform()
        self.assertEqual(driver.title,u"客服系统")
        
        #driver.find_element_by_css_selector(css_selector)
        #html body div#container.container div.sidebar_container form#new_new_order_form.form-horizontal.new_new_order_form div.form-group.select.required.new_order_form_good div.col-sm-8 select#new_order_form_good.select.required.form-control option
        #html body div#container.container div.sidebar_container form#new_new_order_form.form-horizontal.new_new_order_form div.form-group.select.optional.new_order_form_good div.col-sm-8 select#new_order_form_good.select.optional.form-control option:nth-child(2)
        goodnanemtext=driver.find_element_by_css_selector("div#container.container>div.sidebar_container>form>div>div.col-sm-8>select>option:nth-child(2)").text
        print " the goodnanemtext is ",goodnanemtext
        Select(driver.find_element_by_id("new_order_form_good")).select_by_visible_text(goodnanemtext)
        
        driver.find_element_by_id("new_order_form_totalnum").clear()
        driver.find_element_by_id("new_order_form_totalnum").send_keys("10")
        
        driver.find_element_by_id("new_order_form_coupon_sn").clear()
        driver.find_element_by_id("new_order_form_coupon_sn").send_keys("82170")
        
        Select(driver.find_element_by_id("new_order_form_user_type")).select_by_visible_text(u"客服下单")

        
        driver.find_element_by_id("new_order_form_username").clear()
        driver.find_element_by_id("new_order_form_username").send_keys("testlukeuser")
        
        driver.find_element_by_id("new_order_form_tel").clear()
        driver.find_element_by_id("new_order_form_tel").send_keys("121323232")
        
        Select(driver.find_element_by_id("new_order_form_city")).select_by_visible_text(u"北京")
        #html body div#container.container div.sidebar_container form#new_new_order_form.form-horizontal.new_new_order_form div.form-group.select.required.new_order_form_area div.col-sm-8 select#new_order_form_area.select.required.form-control option:first-child
        cityareaname=driver.find_element_by_css_selector("div#container.container div.sidebar_container form#new_new_order_form.form-horizontal.new_new_order_form div.form-group.select.required.new_order_form_area div.col-sm-8 select#new_order_form_area.select.required.form-control option:first-child").text
        print " the cityareaname is ",cityareaname
        Select(driver.find_element_by_id("new_order_form_area")).select_by_visible_text(cityareaname)
  
        driver.find_element_by_id("new_order_form_address").clear()
        driver.find_element_by_id("new_order_form_address").send_keys("beijingjiangtailu")
        
        #driver.find_element_by_id("new_order_form_washing_date").click()
        #driver.find_element_by_link_text("29").click()
        datestr=str(PythonDateUtils.get_day_of_day(2))
        print " the datestr is ",datestr
        datestrfinalstr=str(datestr[-2:])
        print " the datestrfinalstr is ",datestrfinalstr
        
        driver.find_element_by_id("new_order_form_washing_date").send_keys(datestr)
        driver.find_element_by_link_text(datestrfinalstr).click()
#         time.sleep(1)
#         winBeforeHandle = driver.current_window_handle
#         winHandles = driver.window_handles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
#         driver.find_element_by_id(datestrfinalstr).click()
        time.sleep(1)
        Select(driver.find_element_by_id("new_order_form_washing_time")).select_by_visible_text("08:00-10:00")
        time.sleep(1)
        driver.find_element_by_id("new_order_form_remark").clear()
        driver.find_element_by_id("new_order_form_remark").send_keys("hellodedaixi")
        
        time.sleep(1)
        #driver.find_element_by_name("commit").click()
        #driver.find_element_by_css_selector("input.button.btn.btn-info.btn-style-width").send_keys(Keys.ENTER)
        #html body div#container.container div.alert.fade.in.alert-success
        #createorderresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        #driver.find_element_by_css_selector("input.button.btn.btn-info.btn-style-width").click()
        #driver.find_element_by_xpath("/html/body/div[2]/div/form/input").click()
        driver.execute_script("window.scrollBy(0,200)","")  #
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
        time.sleep(2)
        driver.find_element_by_css_selector("input.button.btn.btn-info.btn-style-width").click()
        #html body div#container.container div.sidebar_container form#new_new_order_form.form-horizontal.new_new_order_form input.button.btn.btn-info.btn-style-width
        #html body div#container.container div.sidebar_container form#new_new_order_form.form-horizontal.new_new_order_form input.button.btn.btn-info.btn-style-width
        self.assertEqual(driver.title,u"客服系统")

        try:  
            wearesorrytext=driver.find_element_by_css_selector("body > div > h1").text
            print " the wearesorrytext result is ",wearesorrytext
            if wearesorrytext in "We're sorry, but something went wrong":
                 raise "We are Sorry"
            else:
            
             finalresult=driver.find_element_by_css_selector("html body div#container.container div.alert.fade.in.alert-success").text
             print " the finalresult is ",finalresult
             assert u"订单已添加" in finalresult
        except Exception,e:  
             #print Exception,":",e 
             pass
             finalresult=driver.find_element_by_css_selector("html body div#container.container div.alert.fade.in.alert-success").text
             print " the finalresult is ",finalresult
             assert u"订单已添加" in finalresult
        self.assertEqual(driver.title,u"客服系统")
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
