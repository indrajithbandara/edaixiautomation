#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser ,MySQLdb
import PythonDateUtils
from selenium.webdriver.common.by import By
import appobjectkefu,kefu_utiltools
class KefuTestcase03OrderlistCreatefanxiorder(unittest.TestCase):
    
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
        
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqldatabase")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase03_orderlist_createfanxiorder(self):
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
        
        print " the testcase test_kefu_testcase03_orderlist_createfanxiorder is ",driver.title
        #self.assertEqual(driver.title,u"客服系统")
        time.sleep(1)
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_orderlist+")>a").click()
       
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
      
#         n = cursor.execute("SELECT ordersn,fan_id FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
#         #print " the cursor.fetchone() is ",cursor.fetchone()
#         for i in xrange(cursor.rowcount):
#             ordersn,fan_id=cursor.fetchone()
#             #print " the cursor.fetchone() is ",cursor.fetchone()
#         print "ordersn,fan_id is ",ordersn,fan_id
#         
#         global ordernumber
#         cursor.execute("SELECT ordersn,fan_id FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
#         for i in xrange(cursor.rowcount):
#             ordersn,fan_id = cursor.fetchone()
#             #print ordersn,fan_id
#         ordernumber=ordersn
#         global ordersn
#         n = cursor.execute("SELECT ordersn FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
#         for i in xrange(cursor.rowcount):
#             ordersn = cursor.fetchone()
#             ordervrnum=ordersn
#         print ordervrnum
#         cursor.execute("UPDATE ims_washing_order SET status_delivery='3' ,STATUS='1' ,fanxidan_id=0 WHERE ordersn='"+ordersn+"'")

        #This is test data for kefu create fanxidan business
        #ordersn="0723821336144"

        driver.find_element_by_id("order_search_form_ordersn").clear()
        driver.find_element_by_id("order_search_form_ordersn").send_keys(PythonDateUtils.fanxiordersnnumber)
        
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title,u"客服系统")
        print " the PythonDateUtils.fanxiordersnnumber is ",PythonDateUtils.fanxiordersnnumber
        time.sleep(1)
        
        driver.find_element_by_css_selector("div#container.container div#content-container div#content div.panel.panel-primary form.form-horizontal.batch_update table.table.table-striped tbody tr:first-child td:nth-child(2) a").click()
        self.assertEqual(driver.title,u"客服系统")
        driver.find_element_by_css_selector("div#container.container a#fanxi_button.btn.btn-info").click()
        self.assertEqual(driver.title,u"客服系统")
        winBeforeHandle = driver.current_window_handle
        winHandles = driver.window_handles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
                
                
        #datestr=str(PythonDateUtils.get_day_of_day(1))[-2:]
        datestr=str(PythonDateUtils.get_day_of_day(3))
        print " the datestr is ",datestr
        
        driver.find_element_by_id("fanxi_order_form_washing_date").clear()
        driver.find_element_by_id("fanxi_order_form_washing_date").send_keys(datestr)
        driver.find_element_by_id("fanxi_order_form_washing_date").click()
        #driver.find_element_by_link_text(datestr).click()
        fanxiwashingtime=driver.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[8]/td[2]/div/div/select/option[2]").text
        #fanxiwashingtime=driver.find_element_by_css_selector("div#container.container form#new_fanxi_order_form_1039230.form-horizontal.new_fanxi_order_form table.table.table-striped.search-table tbody tr:nth-last-child(4) td:last-child div.form-group.select.required.fanxi_order_form_washing_time div.col-sm-8 select#fanxi_order_form_washing_time.select.required.form-control option:nth-child(2)").text
        print " the fanxiwashingtime is ",fanxiwashingtime
        Select(driver.find_element_by_id("fanxi_order_form_washing_time")).select_by_visible_text(fanxiwashingtime)
        
        driver.find_element_by_id("fanxi_order_form_remark").clear()
        driver.find_element_by_id("fanxi_order_form_remark").send_keys("beijingjiangtailu")
        
        #driver.find_element_by_css_selector("div#container.container form#new_fanxi_order_form_254.form-horizontal.new_fanxi_order_form table.table.table-striped.search-table tbody tr:last-child td:last-child input.button.btn.btn-info.btn-style-width").click()
        driver.find_element_by_xpath("//input[@type='submit']").click()
        #driver.find_elements(By.XPATH, "//input[@type='submit']").click()
        
        self.assertEqual(driver.title,u"客服系统")
        
        createfanxidanresult=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text

        print " the createfanxidanresult is ",createfanxidanresult
        #self.assertEqual(createfanxidanresult,u"客服系统")
        cursor.execute("UPDATE ims_washing_order SET status_delivery='3' ,STATUS='1' ,fanxidan_id=0,fan_id='"+PythonDateUtils.fanstableidnumber+"' WHERE ordersn='"+PythonDateUtils.ordersnnumber+"'")

        #提交到数据库执行
        conn.commit()
        cursor.close()
        conn.close()
        PythonDateUtils.getcloseconn()
    
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
