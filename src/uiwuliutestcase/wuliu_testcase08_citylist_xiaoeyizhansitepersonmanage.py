#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,MySQLdb,random
from selenium.webdriver.common.action_chains import ActionChains
import appobjectwuliu,wuliu_utiltools
class WuliuTestcase08Citylistxiaoeyizhansitepersonmanage(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wuliu_utiltools.getwuliuconfigpath()) 
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase,mysqlrongchangdb
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "uiusername")
        PASS_WORD = conf.get("wuliusection", "uipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqlwuliudb")
        mysqlrongchangdb = conf.get("databaseconn", "mysqlrongchangdb")

        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase,mysqlrongchangdb
        
        self.base_url = WULIU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase08_citylist_xiaoeyizhansitepersonmanage(self):
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
        self.assertEqual(driver.title, u"物流")
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 

        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click()
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+str(9)+").active a").click()
        
        self.assertEqual(driver.title, u"物流")
     
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(11)").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
    
        self.assertEqual(driver.title, u"物流")
    
        driver.find_element_by_css_selector("div#container.container a.btn.btn-info.col-md-1").click()
        userrname="lukejujnjun"+str(random.randint(0,999))
#         telephonenumber="18611111"+str(random.randint(0,999))
#         identitnumber="152528198801280"+str(random.randint(0,999))
        telephonenumber=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        print " the telephonenumber is ",telephonenumber
        #identifiedCardId="152528198801280"+str(random.randint(0,999))
        identifiedCardId=wuliu_utiltools.makeNewIdentifiedCardId()
        print " the identifiedCardId is ",identifiedCardId
        
#         print " the telephonenumber,identitnumber is ",telephonenumber,identitnumber
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_id("courier_form_realname").clear()
        driver.find_element_by_id("courier_form_realname").send_keys(userrname)
        driver.find_element_by_id("courier_form_tel").clear()
        driver.find_element_by_id("courier_form_tel").send_keys(telephonenumber)
        driver.find_element_by_id("courier_form_id_number").clear()
        driver.find_element_by_id("courier_form_id_number").send_keys(identifiedCardId)
        driver.find_element_by_id("courier_form_password").clear()
        driver.find_element_by_id("courier_form_password").send_keys("123456")
        driver.find_element_by_id("courier_form_bank_name").clear()
        driver.find_element_by_id("courier_form_bank_name").send_keys(u"建设银行")
        driver.find_element_by_id("courier_form_bank_card").clear()
        driver.find_element_by_id("courier_form_bank_card").send_keys("9111000029922921113")
        driver.find_element_by_id("courier_form_is_zancun").click()
        driver.find_element_by_id("courier_form_is_owner").click()
                
        
        driver.find_element_by_id("courier_form_start_time").send_keys(str(wuliu_utiltools.get_day_of_day(1)))
        #driver.find_element_by_link_text("21").click()
        driver.find_element_by_id("courier_form_end_time").send_keys(str(wuliu_utiltools.get_day_of_day(5)))
        #driver.find_element_by_link_text("24").click()

        driver.find_element_by_name("commit").click()
      
        time.sleep(1)
        self.assertEqual(driver.title, u"物流")

        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys("luke")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_css_selector("div.col-md-2.input-group > span.input-group-btn > input[name=\"commit\"]").click()
        driver.find_element_by_id("realname").click()
        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys("luke")
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        
        self.assertEqual(driver.title, u"物流")
        #html body div#container.container>div#courier_search_container>table.table.table-striped>tbody>tr:nth-child(2)>td:last-child>a
        driver.find_element_by_css_selector("div#container.container>div#courier_search_container>table.table.table-striped>tbody>tr:nth-child(2)>td:last-child>a").click()
        #driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("courier_form_realname").clear()
        driver.find_element_by_id("courier_form_realname").send_keys("lukejujnjun111")
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        
        cursor.execute("DELETE FROM ims_washing_courier where tel='"+telephonenumber+"'")
        conn.commit()
        cursor.close()
        conn.close()
        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys("luke")
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"超时订单").click()
        driver.find_element_by_id("timeout_qu_list_btn").click()
        driver.find_element_by_id("timeout_song_list_btn").click()
        driver.find_element_by_id("warning_qu_list_btn").click()
        driver.find_element_by_id("warning_song_list_btn").click()
        self.assertEqual(driver.title, u"物流")
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
