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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.

class CaiwuTestcase08CitylistJiagongdianFactoryBalanceBranch(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectauto3rd.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        #conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        conf.read(auto3rd_utiltools.get3rdcaiwupath())
        global CAIWU_URL,BranchUSER_NAME,BranchPASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqlcaiwudb
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        BranchUSER_NAME = conf.get("caiwusection", "uibranchusername")
        BranchPASS_WORD = conf.get("caiwusection", "uibranchpassword")
        print CAIWU_URL,BranchUSER_NAME,BranchPASS_WORD
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqlcaiwudb = conf.get("databaseconn", "mysqlcaiwudb")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqlcaiwudb
        
        self.base_url = CAIWU_URL
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase08_citylist_jiagongdian_factorybalance_branch(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")
#html body div.container h3.text-center.text-primary a.btn.btn-success.text-center
        loginclick=driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(BranchUSER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(BranchPASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase test_caiwu_testcase08_citylist_jiagongdian_factorybalance_branch is ",driver.title
        #self.assertEqual(driver.title, u"财务")
        time.sleep(2)

        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlcaiwudb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        #cursor.execute("DELETE FROM outlet_order_cleaning_details")
        #conn.commit()
#         cursor.execute("DELETE FROM outlet_order_cleanings")
#         conn.commit()
#         
#         cursor.close()
#         conn.close()
        
        #html body div.navbar.navbar-default.navbar-static-top div.container div.navbar-collapse.collapse.navbar-responsive-collapse ul.nav.navbar-nav li a
#         driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(8).active a").click()
        driver.find_element_by_css_selector("div.container > div > ul > li:nth-child(6) >a").click()

        self.assertEqual(driver.title, u"财务")
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(9)").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
    
        #self.assertEqual(driver.title, u"财务")
        #html body div.navbar.navbar-default.navbar-static-top 
        #driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-last-child(2)>a").click()
        #driver.find_element_by_link_text(u"结算管理").click()
        time.sleep(1)
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"BJ加工店-长楹天街-店")
        driver.find_element_by_name("commit").click()
        
        time.sleep(1)
        driver.find_element_by_link_text(u"结算").click()
        self.assertEqual(driver.title, u"财务")
        #driver.find_element_by_css_selector("div.container>tbody>tr:last-child(2)>td:last-child(2)>a:first-child").click()
        print str(auto3rd_utiltools.get_day_of_day(1))
        #validator some null exception
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_start_time").send_keys("")
#         #driver.find_element_by_link_text("6").click()
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").send_keys("")
#         driver.find_element_by_name("commit").click()
#         
#         time.sleep(1)
#         
#         winBeforeHandle = driver.current_window_handle
#         #print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         #print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
#         print " the winBeforeHandle, winHandles is  ",winBeforeHandle, winHandles
#         
#         validrornullname=driver.find_element_by_class_name("div.container>div.alert.fade.in.alert-danger").text
#         print " the validrornullname is ",validrornullname
        
        driver.find_element_by_id("outlet_jiesuan_form_jiesuan_start_time").send_keys(str(auto3rd_utiltools.today()))
        #driver.find_element_by_link_text("6").click()
        driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").send_keys(str(auto3rd_utiltools.get_day_of_day(8)))
        driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").click()
        
        #driver.find_element_by_link_text("20").click()
        
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_start_time").click()
#         driver.find_element_by_link_text("7").click()
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").click()
#         driver.find_element_by_link_text("10").click()
        time.sleep(2)
        #driver.refresh()
        driver.execute_script("window.scrollBy(0,200)","")
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_start_time").clear()
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_start_time").send_keys(str(auto3rd_utiltools.get_day_of_day(-7)))
#         #driver.find_element_by_link_text("6").click()
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").clear()
#         driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").send_keys(str(auto3rd_utiltools.get_day_of_day(3)))
        time.sleep(1)
        driver.find_element_by_id("outlet_jiesuan_form_jiesuan_end_time").click()
        #WebDriverWait(driver, 3).until(lambda driver : driver.title.lower().startswith(u"python"))
        #WebDriverWait(driver, 3).until(lambda driver : driver.refresh())
        driver.execute_script("var doc=document.getElementById('ui-datepicker-div');doc.setAttribute('style','display:block');")
        
        #WebDriverWait(driver, 3).until(EC.title_contains(u"财务"))
        time.sleep(1)
        #driver.find_element_by_name("commit").click()
        #driver.find_element_by_link_text(u"生成结算单").click()
        driver.find_element_by_css_selector("div.container div.orders_container form#jiesuan_form.form-horizontal.new_outlet_jiesuan_form button.button.btn.btn-info.pull-right").click()

        self.assertEqual(driver.title, u"财务")
#         winBeforeHandle = driver.current_window_handle
#         print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
#                 
        time.sleep(1)
        driver.find_element_by_link_text(u"提交审核").click()
        time.sleep(1)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认提交审核[\s\S]$")
        #driver.find_element_by_link_text(u"明细").click()
        #driver.find_element_by_css_selector("div.btn.btn-success").click()
        self.assertEqual(driver.title, u"财务")
        daishenhe=driver.find_element_by_css_selector("div.container table.table.table-striped tbody tr:last-child td:nth-last-child(2)").text
        print " the daishenhe is ",daishenhe
        self.assertEqual(daishenhe, u"待审核")
          
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
