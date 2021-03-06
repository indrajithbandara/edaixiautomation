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
import wuliu_utiltools,appobjectwuliu

class WuliuTestcase08CitylistJiagongdianFactoryBalance(unittest.TestCase):
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
    
    def test_wuliu_testcase08_citylist_jiagongdian_factorybalance(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        print " the testcase test_wuliu_testcase08_citylist_jiagongdian_factorybalance is ",driver.title
        self.assertEqual(driver.title, u"物流")
        
        #testdata=appobjectwuliu.testcase08_jiagongdian_forbalantestdata
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        cursor.execute("DELETE FROM outlet_rules")
        conn.commit()
        cursor.close()
        conn.close()
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(8).active a").click()
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child("+str(10)+")").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
        self.assertEqual(driver.title, u"物流")
    
        driver.find_element_by_css_selector("div#container.container >table.table.table-striped> tbody > tr:nth-child(2) > td:nth-last-child(2) > a:last-child").click()
        #div#container.container > tbody > tr:nth-child(2) > td:nth-last-child(2) > a:last-child
        #html body div#container.container table.table.table-striped tbody tr#outlets_279 td a.btn.btn-primary.btn-sm
        self.assertEqual(driver.title, u"物流")
    
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(appobjectwuliu.testcase08_jiagongdian_forbalantestdata)
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("22")

        driver.execute_script("window.scrollBy(0,200)","")  #
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #folloing down to page

        print str(wuliu_utiltools.today())
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(wuliu_utiltools.today()))
        #driver.find_element_by_link_text("6").click()

        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(wuliu_utiltools.get_day_of_day(5)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        
        
        hell=driver.find_element_by_css_selector("div#container.container>div#outlet_rule>table.table.table-striped>tbody>tr:last-child>td:last-child>a").text
        print "the hell rules is ",hell
        #html body div#container.container div#outlet_rule table.table.table-striped tbody tr:last-child td:last-child a.btn.btn-sm.btn-danger
        #driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[4]").click()
        driver.find_element_by_css_selector("div#container.container>div#outlet_rule>table.table.table-striped>tbody>tr:last-child>td:last-child>a").click()
        #print driver.switch_to_alert().text()
        time.sleep(1)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除吗[\s\S]$")
        
        self.assertEqual(driver.title, u"物流")
    
    
        #driver.find_element_by_link_text(u"创建规则").click()
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(appobjectwuliu.testcase08_jiagongdian_forbalantestdata_xiyi)
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("100")
        
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(wuliu_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(wuliu_utiltools.get_day_of_day(5)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
    
        time.sleep(2)

#         driver.find_element_by_id("outlet_rule_form_start_time_display").click()
#         driver.find_element_by_link_text("6").click()
#         driver.find_element_by_id("outlet_rule_form_end_time").click()
#         driver.find_element_by_link_text("20").click()
#         driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(appobjectwuliu.testcase08_jiagongdian_forbalantestdata_xixie)
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(wuliu_utiltools.today()))
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(wuliu_utiltools.get_day_of_day(5)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("2")
        driver.find_element_by_name("commit").click()

        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        
        #Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(u"奢侈品")
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(appobjectwuliu.testcase08_jiagongdian_forbalantestdata)
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(wuliu_utiltools.today()))
#         driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(wuliu_utiltools.get_day_of_day(5)))
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("12")
        
        #driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(wuliu_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(wuliu_utiltools.get_day_of_day(5)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_name("commit").click()
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
