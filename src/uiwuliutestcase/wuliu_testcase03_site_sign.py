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
class WuliuTestcase03sitesign(unittest.TestCase):
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
    
    def test_wuliu_testcase03_site_sign(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        #print driver.title
        #self.assertTrue(driver.title, u"物流")
        time.sleep(2)
        self.assertEqual(driver.title, u"物流")
        #time.sleep(2)
        
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        
#         n = cursor.execute("SELECT washorder.bagsn FROM ims_washing_order AS washorder WHERE washorder.status_delivery=1 AND washorder.bagsn IS NOT NULL ORDER BY washorder.id") 
#         for i in xrange(cursor.rowcount):
#             bagsn= cursor.fetchone()
#         print " the bagsn is ",str(bagsn)[3:-3]
        cursor.execute("UPDATE ims_washing_order SET status_delivery='1' ,status='7' ,jiagongdian_id=NULL,qianshoudian_id= NULL WHERE bagsn='"+appobjectwuliu.factorysignnumber+"'")
#         cursor.execute("UPDATE ims_washing_order SET status_delivery='1' ,status='7' ,jiagongdian_id=NULL,qianshoudian_id= NULL WHERE bagsn='"+str(bagsn)[3:-3]+"'")
        conn.commit()
        
     
#         n = cursor.execute("SELECT ordersn,bagsn,status_delivery,jiagongdian_id,qianshoudian_id  FROM ims_washing_order WHERE bagsn='"+str(bagsn)[3:-3]+"'") 
#         for i in xrange(cursor.rowcount):
#             ordersn ,bagsn,status_delivery,jiagongdian_id,qianshoudian_id = cursor.fetchone()
#         print ordersn ,bagsn,status_delivery,jiagongdian_id,qianshoudian_id
        
        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+appobjectwuliu.wuliutabthree+").dropdown a").click()
        
        self.assertEqual(driver.title, u"物流")
  
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li.dropdown ul.dropdown-menu li a
        #driver.find_element_by_css_selector("div.container>nav.collapse.navbar-collapse.bs-navbar-collapse>ul.nav.navbar-nav>li:nth-child(2)>ul.dropdown-menu>li:first-child>a").click()
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(3).dropdown ul.dropdown-menu li a
        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+appobjectwuliu.wuliutabthree+").dropdown ul.dropdown-menu li a").click()
        #driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[2]/ul/li[1]/a").click()
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a
        driver.find_element_by_id("bagsn").clear()
        driver.find_element_by_id("bagsn").send_keys(appobjectwuliu.factorysignnumber)
        driver.find_element_by_name("commit").click()
        
        print driver.title
        self.assertEqual(driver.title, u"物流")
        #cursor.execute("UPDATE ims_washing_order SET status_delivery='1',qianshoudian_id= NULL WHERE bagsn='E0000000006'")
        #conn.commit()
#         qianshousuccess=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary p.text-center b").text
#         #check_in_msg
#         print "===============qianshousuccess is  ",qianshousuccess
#         #self.assertEqual(qianshousuccess, u"签收成功！")
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
