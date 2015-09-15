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
import appobjectwuliu,wuliu_utiltools
class WuliuTestcase08Citylistdividebasearea(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wuliu_utiltools.getwuliuconfigpath()) 
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "uiusername")
        PASS_WORD = conf.get("wuliusection", "uipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqlwuliudb")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        
        self.base_url = WULIU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase08_citylist_dividebasearea(self):
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
        time.sleep(2)
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine+") >a").click()
        
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+str(9)+").active a").click()
        '''
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        self.assertEqual(driver.title, u"物流")
        #driver.find_element_by_link_text(u"新建城市").click()
        #driver.find_elements_by_css_selector("div#container.container a.btn.btn-infos").click()
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-last-child(2).btn-link a").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr td:nth-last-child(2).btn-link a.btn.btn-success
        '''
        time.sleep(1)
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-last-child(2).btn-link a").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        driver.find_element_by_id("address_input").clear()
        driver.find_element_by_id("address_input").send_keys("addmuiltlgraphic")
        

        driver.find_element_by_css_selector("#address_search_bar > div.btn.btn-info").click()
        time.sleep(1)
        driver.find_element_by_id("add_polygon_btn").click()
        
        #driver.find_element_by_id("address_input").clear()
        #driver.find_element_by_id("address_input").send_keys("111")
        #driver.find_element_by_css_selector("#address_search_bar > div.btn.btn-info").click()
        #driver.find_element_by_id("edit_polygon_btn").click()
        
        self.assertEqual(driver.title, u"物流")
        #cursor.execute("UPDATE ims_washing_order SET status_delivery='3' ,STATUS='1' ,fanxidan_id=0 WHERE ordersn='"+ordersn+"'")
        
        #n = cursor.execute("SELECT ordersn ,username,tel,address ,status_delivery,STATUS ,fanxidan_id FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
        #for i in xrange(cursor.rowcount):
        #    ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id = cursor.fetchone()
        #print ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id
        #print driver.title
        '''
        cursor.execute("DELETE FROM  map_cities WHERE gaode_map_code LIKE 'beijinggaode%'")
        #submit to database
        conn.commit()
        cursor.close()
        conn.close()
        '''
        
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
