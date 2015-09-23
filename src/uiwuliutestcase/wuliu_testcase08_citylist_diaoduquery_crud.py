#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,MySQLdb,wuliu_utiltools
from selenium.webdriver.common.action_chains import ActionChains
import appobjectwuliu
class WuliuTestcase08citylistdiaoduquerycrud(unittest.TestCase):
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
    
    def test_wuliu_testcase08_citylist_diaoduquery_crud(self):
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
  
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child(8).active a").click()
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click()
        time.sleep(1)
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        self.assertEqual(driver.title, u"物流")
        #driver.find_element_by_link_text(u"新建城市").click()
        #driver.find_elements_by_css_selector("div#container.container a.btn.btn-infos").click()
        '''driver.find_element_by_xpath("/html/body/div/a").click()
        time.sleep(1)
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
        time.sleep(1)
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        
        addsuccess=driver.find_element_by_css_selector("div#container.container div.alert.fade.in.alert-success").text
        print addsuccess'''
        #shtml body div#container.container>div:nth-child(2)>a.btn.btn-default
        time.sleep(1)
        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+appobjectwuliu.wuliutabnine_citylist+").active a").click()
                
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(2)").click()
        #.btn.btn-success
        self.assertEqual(driver.title, u"物流")
        
        cursor.execute("UPDATE ims_washing_order SET fanxidan_id='0',status_delivery='3',STATUS='7',paytype='1' WHERE ordersn='"+wuliu_utiltools.ordersnnumber+"'")
        conn.commit()
        
#         n = cursor.execute("SELECT ordersn ,username,tel,address ,status_delivery,STATUS ,fanxidan_id  FROM ims_washing_order WHERE status_delivery='3' AND ordersn='"+wuliu_utiltools.ordersnnumber+"'") 
#         for i in xrange(cursor.rowcount):
#             ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id = cursor.fetchone()
#         print ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id
#         
#         driver.find_element_by_id("order_search_form_ordersn").clear()
#         driver.find_element_by_id("order_search_form_ordersn").send_keys(wuliu_utiltools.ordersnnumber)
        Select(driver.find_element_by_id("order_search_form_delivery_status")).select_by_visible_text(u"客户签收")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        
        
        #html body div#container.container div.checkout-order div.panle-body div.panel.panel-primary form.form-horizontal.batch_update table.table.table-striped tbody tr:first-child td:nth-child(2) a 
        queryordernumber=driver.find_element_by_css_selector("div#container.container div.checkout-order div.panle-body div.panel.panel-primary form.form-horizontal.batch_update table.table.table-striped tbody tr:first-child td:nth-child(2) a ").text
        print " the queryordernumber is ",queryordernumber
        time.sleep(1)
        driver.find_element_by_link_text(queryordernumber).click()
        time.sleep(1)
        winBeforeHandle = driver.current_window_handle
        print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        print "winHandles==",winHandles
        for handle in winHandles:
            if winBeforeHandle != handle:
                driver.switch_to_window(handle)
        driver.find_element_by_xpath("//div[@id='container']/div/div[4]/div/div/div[2]/div/div/button").click()
        time.sleep(2)
        if EC.alert_is_present:
           print("Alert exists")
           alert=self.driver.switch_to_alert()
           #sprint "alert.text",(alert.text)#
           alert.accept
           print("Alert accepted")
        else:
           print("NO alert exists")
           
#         winBeforeHandle = driver.current_window_handle
#         print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
        
        #print " the dialog windows is ",driver.switch_to_alert()
        ''' driver.execute_script("var doc=document.getElementsByClassName('wuliu_form modal fade');doc.setAttribute('aria-hidden','');")
        if EC.alert_is_present:
           print("Alert exists")
           alert=self.driver.switch_to_alert()
           #sprint "alert.text",(alert.text)#
           alert.accept
           print("Alert accepted")
        else:
           print("NO alert exists")
        #driver.switch_to_alert().accept()
        time.sleep(2)
        #Alert alert =driver.switchTo().alert();
        wuliudiaodumodify=driver.find_element_by_css_selector("html body.modal-open div#container.container div.alert.fade.in.alert-success").text
        print " the wuliudiaodumodify is ",wuliudiaodumodify
        time.sleep(1)
#         driver.find_element_by_id("kehu_message_form_username").clear()
#         driver.find_element_by_id("kehu_message_form_username").send_keys(u"监控w23311")
#         driver.find_element_by_id("kehu_message_form_tel").clear()
#         driver.find_element_by_id("kehu_message_form_tel").send_keys("16155555555111")
#         time.sleep(1)
#         driver.find_element_by_css_selector("#new_kehu_message_form_2822532 > div.text-center > input[name=\"commit\"]").click()
#         driver.find_element_by_css_selector("#new_kehu_message_form_2822532 > div.text-center > input[name=\"commit\"]").click()
#         driver.find_element_by_css_selector("#new_kehu_message_form_2822532 > div.text-center > input[name=\"commit\"]").click()
#         time.sleep(1)
#         driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
#         driver.find_element_by_name("commit").click()
        
        time.sleep(1)
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        #driver.find_element_by_css_selector("div#container.container> div#paidan_list_container> div.panel.panel-primary.tab-content> div>form> table.table> tbody tr:first-child> td:nth-child(2)> a").click()
        driver.find_element_by_css_selector("div#container.container div.checkout-order div.panle-body div.panel.panel-primary form.form-horizontal.batch_update table.table.table-striped tbody tr:first-child td:nth-child(2) a").click()
        #html body div#container.container div.checkout-order div.panle-body div.panel.panel-primary form.form-horizontal.batch_update table.table.table-striped tbody tr:first-child td:nth-child(2) a
        #html body div#container.container div#paidan_list_container div.panel.panel-primary.tab-content div#order_1039373 form#form_1039373.single_order_form table.table tbody tr:first-child td:nth-child(2) a
        #cursor.execute("UPDATE ims_washing_order SET status_delivery='3' ,STATUS='1' ,fanxidan_id=0 WHERE ordersn='"+ordersn+"'")
        
        #n = cursor.execute("SELECT ordersn ,username,tel,address ,status_delivery,STATUS ,fanxidan_id FROM ims_washing_order WHERE status_delivery=3 AND fanxidan_id=0 AND bagsn IS NOT NULL  AND id=(SELECT MIN(id) FROM ims_washing_order) ORDER BY id") 
        #for i in xrange(cursor.rowcount):
        #    ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id = cursor.fetchone()
        #print ordersn ,username,tel,address,status_delivery,STATUS ,fanxidan_id
        #print driver.title
        #cursor.execute("DELETE FROM  map_cities WHERE gaode_map_code LIKE 'beijinggaode%'")
#         winBeforeHandle = driver.current_window_handle
#         print "winBeforeHandle==",winBeforeHandle
#         winHandles = driver.window_handles
#         print "winHandles==",winHandles
#         for handle in winHandles:
#             if winBeforeHandle != handle:
#                 driver.switch_to_window(handle)
#         

        #/html/body/div[1]/form/table/tbody/tr[11]/td[2]/input
        '''
        #self.assertTrue(driver.title, u"物流")
        self.assertEqual(driver.title, u"物流")
        cursor.execute("UPDATE ims_washing_order SET fanxidan_id='0',paytype='1',pay_status='1',fan_id='"+wuliu_utiltools.fansfanidnumber+"',status_delivery='3'  WHERE ordersn='"+wuliu_utiltools.ordersnnumber+"'")
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
        wuliu_utiltools.getcloseconn()
        
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
