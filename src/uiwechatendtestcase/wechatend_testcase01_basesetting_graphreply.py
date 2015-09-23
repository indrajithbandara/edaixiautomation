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
import appobjectwechat,wechat_end_utiltools

class WechatTestcase01basesettinggraphreply(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwechat.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wechat_end_utiltools.getwechatendconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_ops.conf")
        global WECHAT_URL,WECHAT_USER_NAME,WECHAT_PASS_WORD
        WECHAT_URL = conf.get("wechatsection", "uihostname")
        WECHAT_USER_NAME = conf.get("wechatsection", "uiusername")
        WECHAT_PASS_WORD = conf.get("wechatsection", "uipassword")
        print WECHAT_URL,WECHAT_USER_NAME,WECHAT_PASS_WORD  
        self.base_url = WECHAT_URL
        #self.base_url = "http://ops05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wechat_testcase01_basesetting_graphreply(self):
        driver = self.driver
        driver.get(self.base_url + "/")


        driver.find_element_by_link_text("login with cas").click()
        time.sleep(1)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(WECHAT_USER_NAME)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(WECHAT_PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        #self.assertEqual(driver.title, u"荣昌微信公众服务平台")
        print " the testcase test_wechat_testcase01_basesetting_defaultkeyword is ",driver.title
        time.sleep(1)
        driver.find_element_by_link_text(u"如果你的浏览器没有自动跳转，请点击此链接").click()
        time.sleep(1)

        driver.find_element_by_css_selector("div.mCSB_container>div.sidebar-nav>div#snav>ul>li:nth-child("+appobjectwechat.wechatend_tab_basesetting+")>a").click()
        #driver.find_element_by_link_text(u"基本设置").click()
        #driver.find_element_by_css_selector(appobjectops.clickPermissionLink).click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.mCSB_container>div.sidebar-nav>div#snav>ul>li:nth-child("+appobjectwechat.wechatend_tab_basesetting_graphreply+")>a").click()
        
        
        print "wechat end  test_wechat_testcase01_basesetting_graphreply testcaesee is ",driver.title
        self.assertEqual(driver.title, u"荣昌微信公众服务平台")
        
        
        #html body ul.nav.nav-tabs li:nth-child(1).active a
        driver.execute_script("$('div[class=emotions]').css('display','block');")
        driver.execute_script("$('div[class=emotions]').attr('style','display:block;');")
        #.attr('style','display:none';)
        driver.execute_script("$('.emotions').attr('style','display:block;');")
        driver.execute_script("$('div[class=emotions]').show();")
        #driver.execute_script("document.getElementsByClassName('emotions').style.display = 'block';")
#         winBeforeHandle = driver.current_window_handle
#         print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
        #.show();
        #.css("display","block");
#         driver.find_element_by_name("keyword").clear()
#         driver.find_element_by_name("keyword").send_keys("dsds")
#         driver.find_element_by_xpath("//button").click()
        
        #html body ul.nav.nav-tabs li:nth-child(2) a
        #driver.find_element_by_link_text(u"添加规则").click()
        #html body ul.nav.nav-tabs li.active a
        driver.find_element_by_css_selector("html>body>ul.nav.nav-tabs>li:nth-child(2)>a").click()
        time.sleep(1)
        driver.find_element_by_css_selector("ul.nav.nav-tabs>li:nth-child(1).active>a").click()
        #driver.find_element_by_link_text(u"管理规则").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"添加规则").click()
        driver.find_element_by_link_text(u"管理规则").click()
        driver.find_element_by_name("keyword").clear()
        driver.find_element_by_name("keyword").send_keys("dsds")
        driver.find_element_by_xpath("//button").click()
        
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
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
