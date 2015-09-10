# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
import appobjectauto3rd
import auto3rd_utiltools

class WuliuTestcase08CitylistJiagongdianFactoryBalance(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectauto3rd.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        conf.read(auto3rd_utiltools.get3rdwuliupath())
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
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        cursor.execute("DELETE FROM outlet_rules")
        conn.commit()
        cursor.close()
        conn.close()
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(8).active a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child(8) >a").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(9)").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
        self.assertEqual(driver.title, u"物流")
        #BJ加工店-长楹天街-店
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"BJ加工店-长楹天街-店")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div#container.container >table.table.table-striped> tbody > tr:nth-child(2) > td:nth-last-child(2) > a:last-child").click()
        #div#container.container > tbody > tr:nth-child(2) > td:nth-last-child(2) > a:last-child
        #html body div#container.container table.table.table-striped tbody tr#outlets_279 td a.btn.btn-primary.btn-sm
        self.assertEqual(driver.title, u"物流")
    
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(u"家纺")
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("9")

        print str(auto3rd_utiltools.today())
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(auto3rd_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(auto3rd_utiltools.get_day_of_day(3)))
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
        time.sleep(2)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认删除吗[\s\S]$")
        
        self.assertEqual(driver.title, u"物流")
    
    
        #driver.find_element_by_link_text(u"创建规则").click()
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(u"洗衣")
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("10")
        
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(auto3rd_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(auto3rd_utiltools.get_day_of_day(3)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
    
        time.sleep(2)

#         driver.find_element_by_id("outlet_rule_form_start_time_display").click()
#         driver.find_element_by_link_text("6").click()
#         driver.find_element_by_id("outlet_rule_form_end_time").click()
#         driver.find_element_by_link_text("20").click()
#         driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(u"洗鞋")
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(auto3rd_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(auto3rd_utiltools.get_day_of_day(3)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("2")
        driver.find_element_by_name("commit").click()

        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        
        #Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(u"奢侈品")
        Select(driver.find_element_by_id("outlet_rule_form_category_id")).select_by_visible_text(u"家纺")
        driver.find_element_by_id("outlet_rule_form_discount").clear()
        driver.find_element_by_id("outlet_rule_form_discount").send_keys("8")
        
        driver.find_element_by_id("outlet_rule_form_start_time_display").send_keys(str(auto3rd_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_rule_form_end_time").send_keys(str(auto3rd_utiltools.get_day_of_day(3)))
        #driver.find_element_by_link_text("20").click()
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
    
        
#         driver.get("http://stackoverflow.com/questions/7794087/running-javascript-in-selenium-using-python")
#         driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")

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
