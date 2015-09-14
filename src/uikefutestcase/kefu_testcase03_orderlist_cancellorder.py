#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser,MySQLdb
import appobjectkefu,kefu_utiltools
class KefuTestcase03OrderlistCancellorder(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectkefu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(kefu_utiltools.getkefuconfigpath())
        #conf.read("C:/edaixi_testdata/userdata_kefu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        KEFU_URL = conf.get("kefusection", "uihostname")
        USER_NAME = conf.get("kefusection", "uiusername")
        PASS_WORD = conf.get("kefusection", "uipassword")
        print KEFU_URL,USER_NAME,PASS_WORD  
        self.base_url = KEFU_URL
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqldatabase")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase03_orderlist_cancellorder(self):
        driver = self.driver
        #driver.get(self.base_url + "/orders/new")
        driver.get(self.base_url + "/")
        #driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        
        print " the testcase test_kefu_testcase03_orderlist_cancellorder is ",driver.title
        #self.assertEqual(driver.title,u"客服系统")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child(3)>a").click()
        self.assertEqual(driver.title,u"客服系统")
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        n = cursor.execute("SELECT ordersn ,username,tel,address FROM ims_washing_order WHERE status_delivery=1 AND pay_status=1 AND bagsn IS NOT NULL ORDER BY id") 
        for i in xrange(cursor.rowcount):
            ordersn ,username,tel,address = cursor.fetchone()
        print " the ordersn ,username,tel,address is ",ordersn ,username,tel,address
        
        driver.find_element_by_id("order_search_form_ordersn").clear()
        driver.find_element_by_id("order_search_form_ordersn").send_keys(ordersn)
        
        driver.find_element_by_css_selector("input.btn.btn-success.col-md-1").click()
        time.sleep(2)
        self.assertEqual(driver.title,u"客服系统")
        checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
        for checkbox in checkboxes:
            checkbox.click()
        time.sleep(2)
        
        driver.find_element_by_css_selector("div#container.container div#content-container form#new_order_search_form.form-horizontal.new_order_search_form a.btn.btn-danger.col-md-1").click()
        #print driver.switch_to_alert().text
        time.sleep(2)
        driver.switch_to_alert().accept()
        
        winBeforeHandle = driver.current_window_handle
        winHandles = driver.window_handles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
        #该订单已付款，已付款状态，如需退款请建工单！确认取消?
        
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body table.table.table-striped tbody tr:first-child td:last-child form.button_to div input.btn.btn-danger").click()
        time.sleep(2)
        driver.switch_to_alert().accept()
        print driver.title
        #assert "Yahoo!" in driver.titlecursor = db.cursor()

        cursor.execute("UPDATE ims_washing_order SET status_delivery='1' ,STATUS='1'  WHERE ordersn='"+ordersn+"'")
        #提交到数据库执行
        conn.commit()
        cursor.close()
        conn.close()
        self.assertEqual(driver.title,u"客服系统")
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
