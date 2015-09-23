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
#s@two-dimension code
class WechatTestcase01basesettingdefaultkeyword(unittest.TestCase):
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
    
    def test_wechat_testcase01_basesetting_defaultkeyword(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #html body div#container.container h3.text-center.text-primary a.btn.btn-success.text-center
        #driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        #loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
#         loginclick=driver.find_element_by_css_selector(appobjectwechat.permloginClickButton)
#         ActionChains(driver).double_click(loginclick).perform()
#         driver.find_element_by_id("username").clear()
#         driver.find_element_by_id("username").send_keys(USER_NAME)
#         driver.find_element_by_id("password").clear()
#         driver.find_element_by_id("password").send_keys(PASS_WORD)
#         driver.find_element_by_id("login-submit").click()

#         self.assertEqual(driver.title, u"e袋洗城市运营后台")
        time.sleep(1)
        driver.find_element_by_link_text("login with cas").click()
        time.sleep(1)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(WECHAT_USER_NAME)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(WECHAT_PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase test_wechat_testcase01_basesetting_defaultkeyword is ",driver.title
        time.sleep(1)
        driver.find_element_by_link_text(u"如果你的浏览器没有自动跳转，请点击此链接").click()
        time.sleep(1)
        
        #html body div.content-main table#frametable tbody tr td.content-left.mCustomScrollbar._mCS_11 div#mCSB_11.mCustomScrollBox.mCS-dark-thin div.mCSB_container div.sidebar-nav div#snav ul:first-child.snav li:nth-child(1).snav-header.open a
        driver.find_element_by_css_selector("div.mCSB_container>div.sidebar-nav>div#snav>ul>li:nth-child("+appobjectwechat.wechatend_tab_basesetting+")>a").click()
        #driver.find_element_by_link_text(u"基本设置").click()
        #driver.find_element_by_css_selector(appobjectops.clickPermissionLink).click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.mCSB_container>div.sidebar-nav>div#snav>ul>li:nth-child("+appobjectwechat.wechatend_tab_basesetting_defaultkeywords+")>a").click()
        #driver.find_element_by_css_selector("div.content-main table#frametable tbody tr td.content-left.mCustomScrollbar._mCS_11 div#mCSB_11.mCustomScrollBox.mCS-dark-thin div.mCSB_container div.sidebar-nav div#snav ul:first-child.snav li:nth-child("+appobjectwechat.wechatend_tab_basesetting_defaultkeywords+").snav-header.open a").click()
        #driver.find_element_by_link_text(u"默认关键字").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | main | ]]
        
        #driver.execute_script("var doc=document.getElementsByClassName('modal hide fade');doc.setAttribute('aria-hidden','');")
        driver.execute_script("$('#myModal').show();")
        #driver.execute_script("$('.emotions')[0].style.display = 'block';")
        #driver.execute_script("document.getElementsByClassName('emotions')[0].style.display='block';")
        #driver.execute_script("$('.button.btn.btn-success.edit-word').bind('click');")
        driver.switch_to_frame("main") 
        #document.getElementsByClassName("emotions").style.display="block";
        #html body div.main table.table.table-bordered tbody tr td button.btn.btn-success.edit-word
        driver.find_element_by_css_selector("div.main>table.table.table-bordered>tbody>tr:last-child>td:last-child>button.btn.btn-success.edit-word").click()
        #driver.find_element_by_xpath("//button").click()
        time.sleep(2)
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("aaaa")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        time.sleep(1)
        self.assertEqual(u"保存成功", self.close_alert_and_get_its_text())
        time.sleep(1)
        self.assertEqual(driver.title, u"荣昌微信公众服务平台")
        
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
