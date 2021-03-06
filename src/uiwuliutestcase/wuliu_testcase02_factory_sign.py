#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
#from pty import CHILD
import appobjectwuliu,wuliu_utiltools
# from uiwuliutestcase import appobjectwuliu
class WuliuTestcase02factorysign(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wuliu_utiltools.getwuliuconfigpath()) 
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqlrongchangdb
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "uiusername")
        PASS_WORD = conf.get("wuliusection", "uipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqlrongchangdb  = conf.get("databaseconn", "mysqlrongchangdb")
        
        print mysqlhostname,mysqlusername,mysqlpassword,mysqlrongchangdb
        
        
        self.base_url = WULIU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase02factory_sign(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase test_wuliu_testcase02factory_sign is ",driver.title
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        
        cursor.execute("UPDATE ims_washing_order SET status_delivery='1' ,qianshoudian_id= NULL WHERE bagsn='"+appobjectwuliu.factorysignnumber+"'")
        conn.commit()
        
     
#         n = cursor.execute("SELECT ordersn,bagsn,status_delivery,jiagongdian_id,qianshoudian_id  FROM ims_washing_order WHERE bagsn='E0000000006'") 
#         for i in xrange(cursor.rowcount):
#             ordersn ,bagsn,status_delivery,jiagongdian_id,qianshoudian_id = cursor.fetchone()
#         print ordersn ,bagsn,status_delivery,jiagongdian_id,qianshoudian_id
        
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(2).dropdown a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabtwo_factorysign+") >a").click()
        
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_css_selector("div.container  > nav > ul > li:nth-child("+appobjectwuliu.wuliutabtwo_factorysign+").dropdown > ul.dropdown-menu > li:first-child > a").click()

        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        #driver.find_element_by_css_selector("div.container>nav.collapse.navbar-collapse.bs-navbar-collapse>ul.nav.navbar-nav>li:nth-child(2)>ul.dropdown-menu>li:first-child>a").click()
        #driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[2]/ul/li[1]/a").click()
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a
        driver.find_element_by_id("bagsn").clear()
        driver.find_element_by_id("bagsn").send_keys(appobjectwuliu.factorysignnumber)
        driver.find_element_by_name("commit").click()
        
        print " after submitted testcase test_wuliu_testcase02factory_sign ",driver.title
        self.assertEqual(driver.title, u"物流")
        #html body div#container.container div.panel.panel-primary p.text-center b#check_in_msg
#         qianshouresult=driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>p.text-center>b#check_in_msg").text
#         print " the qianshouresult is ",qianshouresult
#         
#         assert u"签收成功！" in qianshouresult
#         winBeforeHandle = driver.current_window_handle
#         print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
        #cursor.execute("UPDATE ims_washing_order SET status_delivery='1',qianshoudian_id= NULL WHERE bagsn='E0000000006'")
        #conn.commit()
        #self.assertEqual(driver.title, u"物流")
        
        #html body div#container.container div.panel.panel-primary p.text-center b#check_in_msg
#         qianshousuccess=driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>p.text-center>b#check_in_msg").text
#         #check_in_msg
#         print " the qianshousuccess result is ",qianshousuccess
        
#         self.assertEqual(qianshousuccess, u"签收成功！")
        
        cursor.close()
        conn.close()
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
