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
class WuliuTestcase08Citylistouttimemanage(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wuliu_utiltools.getwuliuconfigpath()) 
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqlwuliudb,mysqlrongchangdb
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "uiusername")
        PASS_WORD = conf.get("wuliusection", "uipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqlwuliudb = conf.get("databaseconn", "mysqlwuliudb")
        
        mysqlrongchangdb  = conf.get("databaseconn", "mysqlrongchangdb")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqlwuliudb,mysqlrongchangdb
        
        self.base_url = WULIU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase08_citylist_outtimemanage(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " testcase test_wuliu_testcase08_citylist_outtimemanage is ",driver.title
        self.assertEqual(driver.title, u"物流")
        
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click()
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+str(9)+").active a").click()
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        
        #driver.find_element_by_link_text(u"新建城市").click()
        #driver.find_elements_by_css_selector("div#container.container a.btn.btn-infos").click()
        time.sleep(1)
        '''
        driver.find_element_by_xpath("/html/body/div/a").click()
        self.assertEqual(driver.title,u"物流")
        cityidname=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.panle-body div.orders_container form#new_map_city.form-horizontal.new_map_city div.form-inputs div.form-group.select.required.map_city_api_city_id div.col-sm-8 select#map_city_api_city_id.select.required.form-control option:nth-child(2)").text
        print " the cityidname is ",cityidname
        
        Select(driver.find_element_by_id("map_city_api_city_id")).select_by_visible_text(cityidname)

        driver.find_element_by_id("map_city_center_lat").clear()
        driver.find_element_by_id("map_city_center_lat").send_keys("-5")

        driver.find_element_by_id("map_city_center_lng").clear()
        driver.find_element_by_id("map_city_center_lng").send_keys("-3")

        driver.find_element_by_id("map_city_search_radius").clear()
        driver.find_element_by_id("map_city_search_radius").send_keys("-5")
        
        driver.find_element_by_id("map_city_gaode_map_code").clear()
        driver.find_element_by_id("map_city_gaode_map_code").send_keys("beijinggaode")
        
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        
        addsuccess=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print " the addsuccess is ",addsuccess
        #shtml body div#container.container>div:nth-child(2)>a.btn.btn-default
        '''
        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+appobjectwuliu.wuliutabnine_citylist+").active a").click()
                 
        time.sleep(2)
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child("+str(4)+")").click()
        #.btn.btn-success

        #sdriver.find_element_by_link_text(u"城市列表").click()
        #driver.find_element_by_link_text(u"超时订单").click()
        time.sleep(1)
        driver.find_element_by_id("timeout_qu_list_btn").click()

        driver.find_element_by_id("timeout_song_list_btn").click()
        driver.find_element_by_id("warning_qu_list_btn").click()
        driver.find_element_by_id("warning_song_list_btn").click()
        
        driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[3]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/ul/li[4]/a").click()
        print " test_wuliu_testcase08_citylist_outtimemanage result ",driver.title
        self.assertEqual(driver.title, u"物流")
        wuliuconn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlwuliudb,charset="utf8")    
        global wuliucursor 
        wuliucursor = wuliuconn.cursor() 
        
        wuliucursor.execute("DELETE FROM  map_cities WHERE gaode_map_code LIKE 'beijinggaode%'")
        
        wuliuconn.commit()
        wuliucursor.close()
        cursor.close()
        wuliuconn.close()
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
