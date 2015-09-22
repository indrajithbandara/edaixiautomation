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

class WuliuTestcase08citylistdiaodupaidanfanxidanYiPandan(unittest.TestCase):
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
    
    def test_wuliu_testcase08citylist_diaodupaidan_fanxidan_yipandan(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        time.sleep(1)
        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase test_wuliu_testcase08citylist_diaodupaidan_fanxidan_yipandan is ",driver.title
        time.sleep(1)
        #self.assertTrue(driver.title, u"物流")
        #self.assertEqual(driver.title, u"物流")
        
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(8).active a").click()
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click()
        
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        
        time.sleep(1)
        driver.find_element_by_link_text(u"新建城市").click()
        #driver.find_elements_by_css_selector("div#container.container a.btn.btn-infos").click()
        #driver.find_element_by_xpath("/html/body/div/a").click()
        cityidname=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary div.panle-body div.orders_container form#new_map_city.form-horizontal.new_map_city div.form-inputs div.form-group.select.required.map_city_api_city_id div.col-sm-8 select#map_city_api_city_id.select.required.form-control option:nth-child(2)").text
        print cityidname
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
        
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        #addsuccess=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        #print addsuccess
        #shtml body div#container.container>div:nth-child(2)>a.btn.btn-default
        
        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+str(9)+").active a").click()
        self.assertEqual(driver.title, u"物流")
        
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a").click()
        #.btn.btn-success
        self.assertEqual(driver.title, u"物流")
        
#         n = cursor.execute("SELECT ordersn ,username,tel,address ,status_delivery,STATUS ,fanxidan_id  FROM ims_washing_order WHERE status_delivery='3' AND ordersn='15072110393738'") 
#         for i in xrange(cursor.rowcount):
#             ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id = cursor.fetchone()
#         print ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id
        
        #print " the ordersn is ",ordersn
        driver.find_element_by_id("order_search_form_ordersn").clear()
        driver.find_element_by_id("order_search_form_ordersn").send_keys(str(wuliu_utiltools.ordersnnumber))
        
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        
        driver.find_element_by_css_selector("div#container.container> div#paidan_list_container> div.panel.panel-primary.tab-content> div>form> table.table> tbody tr:first-child> td:nth-child(2)> a").click()
        #html body div#container.container div#paidan_list_container div.panel.panel-primary.tab-content div#order_1039373 form#form_1039373.single_order_form table.table tbody tr:first-child td:nth-child(2) a
        #cursor.execute("UPDATE ims_washing_order SET status_delivery='3' ,STATUS='1' ,fanxidan_id=0 WHERE ordersn='"+ordersn+"'")
        
        #n = cursor.execute("SELECT ordersn ,username,tel,address ,status_delivery,STATUS ,fanxidan_id FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
        #for i in xrange(cursor.rowcount):
        #    ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id = cursor.fetchone()
        #print ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id
        self.assertEqual(driver.title, u"物流")
        
        print driver.title
        #cursor.execute("DELETE FROM  map_cities WHERE gaode_map_code LIKE 'beijinggaode%'")
        winBeforeHandle = driver.current_window_handle
        print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        print "winHandles==",winHandles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
        
        driver.find_element_by_css_selector("div#container.container a#fanxi_button").click()
        
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        
        #html body div#container.container form#new_fanxi_order_form_1039373.form-horizontal.new_fanxi_order_form table.table.table-striped.search-table tbody tr td div.form-group.select.optional.fanxi_order_form_courier_qu div.col-sm-8 select#fanxi_order_form_courier_qu.select.optional.form-control option
        time.sleep(2)
        diaoduperson=driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[6]/td[2]/div/div/select/option[2]").text
         
        print " the diaoduperson is ",diaoduperson
         
        Select(driver.find_element_by_id("fanxi_order_form_courier_qu")).select_by_visible_text(diaoduperson)
         
        
        fanxiwashingtime=driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[8]/td[2]/div/div/select/option[2]").text
        #fanxiwashingtime=driver.find_element_by_css_selector("div#container.container form#new_fanxi_order_form_1039230.form-horizontal.new_fanxi_order_form table.table.table-striped.search-table tbody tr:nth-last-child(4) td:last-child div.form-group.select.required.fanxi_order_form_washing_time div.col-sm-8 select#fanxi_order_form_washing_time.select.required.form-control option:nth-child(2)").text
        print " the fanxiwashingtime is ",fanxiwashingtime
        Select(driver.find_element_by_id("fanxi_order_form_washing_time")).select_by_visible_text(fanxiwashingtime)
        
        driver.find_element_by_id("fanxi_order_form_remark").clear()
        driver.find_element_by_id("fanxi_order_form_remark").send_keys("beijingjiangtailu")
        
        
        driver.find_element_by_id("fanxi_order_form_washing_date").clear()
        driver.find_element_by_id("fanxi_order_form_washing_date").send_keys(str(wuliu_utiltools.get_day_of_day(1)))
        
        
        #driver.find_element_by_css_selector("div#container.container form#new_fanxi_order_form_254.form-horizontal.new_fanxi_order_form table.table.table-striped.search-table tbody tr:last-child td:last-child input.button.btn.btn-info.btn-style-width").click()
        driver.find_element_by_xpath("//input[@type='submit']").click()
        #/html/body/div[1]/form/table/tbody/tr[11]/td[2]/input
        
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        
        
        daioduconfirm=driver.find_element_by_css_selector("div#container.container div.info-div div.row div.col-md-6 div.panel.panel-primary.checkout-order div.panle-body table.table tbody tr:first-child.success td:nth-child(2) span").text
        #html body div#container.container div.info-div div.row div.col-md-6 div.panel.panel-primary.checkout-order div.panle-body table.table tbody tr:first-child.success td:nth-child(2) span.label.label-primary
        print daioduconfirm
        self.assertEqual(daioduconfirm, u"调度已派单")
        #self.assertEqual(driver.title, u"物流")
 
        cursor.execute("UPDATE ims_washing_order SET fanxidan_id='0',paytype='1',pay_status='1',fan_id='"+wuliu_utiltools.fansfanidnumber+"',status_delivery='3' WHERE ordersn='"+wuliu_utiltools.ordersnnumber+"'")
        conn.commit()
        
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
