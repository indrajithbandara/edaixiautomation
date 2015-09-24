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
import wuliu_utiltools,appobjectwuliu
from selenium.webdriver.common.action_chains import ActionChains
class WuliuTestcase08Citylistjiagongdianmanage(unittest.TestCase):
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
    
    def test_wuliu_testcase08_citylist_jiagongdianmanage(self):
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
        print driver.title
        self.assertTrue(driver.title, u"物流")
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click()
        time.sleep(1)
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li.active a
        #html body header.navbar.navbar-default.navbar-static-top div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li.active a
        #html body header.navbar.navbar-default.navbar-static-top div.container>ul.nav.navbar-nav>li:nth-child(8).active a
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(9)").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
    
        self.assertEqual(driver.title, u"物流")
        
        #driver.find_element_by_link_text(u"新建加工店").click()
        driver.find_element_by_css_selector("div#container.container a.btn.btn-info.col-md-1").click()
        self.assertEqual(driver.title, u"物流")
        telephonenumber=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        print " the telephonenumber is ",telephonenumber
        driver.find_element_by_id("outlet_form_title").clear()
        driver.find_element_by_id("outlet_form_title").send_keys("testjiagongdian")
        driver.find_element_by_id("outlet_form_tel").clear()
        driver.find_element_by_id("outlet_form_tel").send_keys(telephonenumber)
        telephonenumber2=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        print " the telephonenumber2 is ",telephonenumber2
        driver.find_element_by_id("outlet_form_usertel").clear()
        driver.find_element_by_id("outlet_form_usertel").send_keys(telephonenumber2)
        Select(driver.find_element_by_id("outlet_form_area")).select_by_visible_text(u"朝阳区")
 #div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.required.outlet_form_area div.col-sm-8 select#outlet_form_area.select.required.form-control option
        driver.find_element_by_id("outlet_form_address").clear()
        driver.find_element_by_id("outlet_form_address").send_keys(u"朝阳区酒仙桥")
#                 Select(driver.find_element_by_id("outlet_form_area")).select_by_visible_text(u"朝阳区")
#         driver.find_element_by_id("outlet_form_address").clear()
#         driver.find_element_by_id("outlet_form_address").send_keys(u"朝阳区酒仙桥")
        time.sleep(2)
        driver.find_element_by_id("get_pos").click()
        time.sleep(1)
        driver.find_element_by_id("set_move").click()
        

        #driver.find_element_by_id("get_pos").click()
        time.sleep(2)
        driver.find_element_by_id("outlet_form_total").clear()
        driver.find_element_by_id("outlet_form_total").send_keys("10")
        
        #driver.find_element_by_id("outlet_form_end_date").click()
        #driver.find_element_by_link_text("6").click()
        print wuliu_utiltools.today()
        driver.find_element_by_id("outlet_form_end_date").clear()
        driver.find_element_by_id("outlet_form_end_date").send_keys(str(wuliu_utiltools.today()))
# 

#         driver.find_element_by_id("capacity_1_is_enabled").click()
#         driver.find_element_by_id("capacity_2_is_enabled").click()
#         driver.find_element_by_id("capacity_3_is_enabled").click()
# #         driver.find_element_by_id("capacity_5_is_enabled").click()
# #         driver.find_element_by_id("capacity_9_is_enabled").click()
#         
#         
# 
#         
#         
# #         driver.find_element_by_id("capacity_1_count").clear()
# #         driver.find_element_by_id("capacity_1_count").send_keys("4")
#         driver.find_element_by_id("capacity_1_count").clear()
#         driver.find_element_by_id("capacity_1_count").send_keys("5")
#         
#         driver.find_element_by_id("capacity_2_count").clear()
#         driver.find_element_by_id("capacity_2_count").send_keys("5")
#         
#         driver.find_element_by_id("capacity_3_count").clear()
#         driver.find_element_by_id("capacity_3_count").send_keys("5")
        
#         startworktime=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 select#outlet_form_operation_time_start.select.optional.form-control.start_time_select option:nth-child(2)")
#         startworktime.is_displayed()
#         print " the startworktime is ",startworktime.is_displayed()
#html body div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 select#outlet_form_operation_time_start.select.optional.form-control.start_time_select option
        #cssSelector1="div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 select#outlet_form_operation_time_start.select.optional.form-control.start_time_select option:nth-child(2)"
        #element = driver.findElement(By.cssSelector(".user-info.right>div>p>a"));
        #element = driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 select#outlet_form_operation_time_start.select.optional.form-control.start_time_select option:nth-child(2)")
#         driver.find_element_by_xpath("//input[@id='s2id_autogen1']").send_keys("00:00")
#         driver.find_element_by_xpath("//input[@id='s2id_autogen1']").click()
        #element= driver.find_element_by_css_selector("select[class='select optional form-control start_time_select']>option[value='1']")
        #ActionChains(driver).move_to_element(element).perform()
#         
#         ActionChains(driver).context_click(element).perform()
# 
#         cssSelector1="select[class='select optional form-control start_time_select']>option[value='1']"
        #driver.find_element_by_css_selector(cssSelector1).click()
#         startimejs="var x = $(\'"+cssSelector1+"\');"
#         driver.execute_script(startimejs)
#         driver.execute_async_script("x.click();")
#         
        #"$(\'select[class='select optional form-control start_time_select']>option[value='1']\').click()"
        #source="/html/body/div[1]/div/div[2]/div/form/div[23]/div/select/option[2]"
        #source="select[class='select optional form-control start_time_select'] > option[value='1']"
        
#         var doc=document.getElementById("outlet_form_operation_time_start");  
#     var citytext=doc.getElementById("city").value; 
#         
        driver.execute_script("var doc=document.getElementById('outlet_form_operation_time_start');doc.setAttribute('style','display:block');")
        
        startworktime=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 select#outlet_form_operation_time_start.select.optional.form-control.start_time_select option:nth-child(2)").text
        print " the startworktime is ",startworktime
        Select(driver.find_element_by_id("outlet_form_operation_time_start")).select_by_visible_text(startworktime)
        #driver.execute_script("$('" + source + "');")
        #driver.execute_script("$('select[class='select optional form-control  tart_time_select']>option[value='1']');")
        #Select(driver.find_element_by_id("s2id_autogen1")).select_by_visible_text("00:00")
        #driver.find_element_by_id("select2-chosen-1").send_keys("00:00")
        #driver.find_element_by_xpath("//input[@id='s2id_autogen1']").send_keys("01:00")
        #webdriver.ActionChains(driver).move_to_element(menu).perform()
        #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","") 
        #Thread.sleep(5000L);
        #driver.execute_script("window.scrollBy(0,200)","")
# JavascriptExecutor j= (JavascriptExecutor)driver;
        #html body div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_end div.col-sm-8 select#outlet_form_operation_time_end.select.optional.form-control.end_time_select option:nth-child(4)
        time.sleep(2)
        #cssSelector2="div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_end div.col-sm-8 select#outlet_form_operation_time_end.select.optional.form-control.end_time_select option:nth-child(4)div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_end div.col-sm-8 select#outlet_form_operation_time_end.select.optional.form-control.end_time_select option:nth-child(4)"
#         cssSelector2="select[class='select optional form-control end_time_select']>option[value='3']"
#         endtimejs="var x = $(\'"+cssSelector2+"\'); x.click();"
#         driver.execute_script(endtimejs)
#         element= driver.find_element_by_css_selector("select[class='select optional form-control end_time_select']>option[value='3']")
#         ActionChains(driver).context_click(element).perform()
# j.executeScript("document.findElementById('123').style.display='block';");      
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_brands div.col-sm-8 select#outlet_form_brands.select.optional.form-control option:first-child").click()
        #driver.find_element_by_xpath("//input[@id='s2id_autogen1']").click()
#         driver.find_element_by_id("s2id_autogen1").send_keys("00:00").is_selected()
        #driver.find_element_by_xpath("//*[@id="+"select2-chosen-1"+"]").send_keys("01:00")
#         driver.find_element_by_id("s2id_autogen1").is_selected()
#         driver.find_element_by_id("s2id_outlet_form_operation_time_start").is_selected()
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 div#s2id_outlet_form_operation_time_start.select2-container.select.optional.form-control.start_time_select a.select2-choice span#select2-chosen-1.select2-chosen").text("00:00")
        #driver.find_element_by_id("s2id_autogen1").send_keys(Keys.ENTER)
        #driver.find_element_by_id("s2id_outlet_form_operation_time_start").click()
        #driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 div#s2id_outlet_form_operation_time_start.select2-container.select.optional.form-control.start_time_select input#s2id_autogen1.select2-focusser.select2-offscreen").click()
        driver.execute_script("var doc=document.getElementById('outlet_form_operation_time_end');doc.setAttribute('style','display:block');")
          
        #time.sleep(2)
        endworktime=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_end div.col-sm-8 select#outlet_form_operation_time_end.select.optional.form-control.end_time_select option:nth-child(3)").text
        print " the endworktime is ",endworktime
        Select(driver.find_element_by_id("outlet_form_operation_time_end")).select_by_visible_text(endworktime)
        #driver.find_element_by_id("s2id_autogen2").clear()
        #driver.find_element_by_id("s2id_autogen2").clear()
#         driver.find_element_by_xpath("//*[@id='s2id_autogen2']").send_keys("02:00")
#         driver.find_element_by_xpath("//input[@id='s2id_autogen2']").send_keys("01:00")
#         driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_brands div.col-sm-8 select#outlet_form_brands.select.optional.form-control option:nth-child(2)").click()
        #driver.find_element_by_id("s2id_autogen2").send_keys("02:00").is_selected()
#         driver.find_element_by_id("s2id_autogen2").is_selected()
#         driver.find_element_by_id("s2id_outlet_form_operation_time_end").is_selected()
        
#         driver.find_element_by_class_name("select2-focusser.select2-offscreen").clear()
#         driver.find_element_by_class_name("select2-focusser.select2-offscreen").send_keys("01:00")
        #driver.find_element_by_id("s2id_autogen2").send_keys("01:00")
        
        #s2id_autogen2
        #jiagongdianbianma="".join(random.choice("0123456789") for i in range(8))
        jiagongdianbianma="".join(random.choice("01234") for i in range(4))
        print " the jiagongdianbianma is ",jiagongdianbianma
        driver.find_element_by_id("outlet_form_bianma").clear()
        driver.find_element_by_id("outlet_form_bianma").send_keys(jiagongdianbianma)
#         driver.find_element_by_id("capacity_5_count").clear()
#         driver.find_element_by_id("capacity_5_count").send_keys("5")
        
        driver.find_element_by_id("capacity_2_is_enabled").click()
        
        driver.find_element_by_id("capacity_2_count").clear()
        driver.find_element_by_id("capacity_2_count").send_keys("5")
                
        driver.find_element_by_id("capacity_2_item").clear()
        driver.find_element_by_id("capacity_2_item").send_keys("115")
# 
#         driver.find_element_by_id("capacity_9_count").clear()
#         driver.find_element_by_id("capacity_9_count").send_keys("5")
        
#         driver.find_element_by_id("outlet_form_can_xiyi").click()
#         driver.find_element_by_id("outlet_form_can_xixie").click()
#         driver.find_element_by_id("outlet_form_can_luxury").click()
##outlet_form_bianma
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        
        
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("outlet_form_usertel").clear()
        driver.find_element_by_id("outlet_form_usertel").send_keys(u"测试张三update")
        
        driver.execute_script("var doc=document.getElementById('outlet_form_operation_time_start');doc.setAttribute('style','display:block');")
        startworktime=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_start div.col-sm-8 select#outlet_form_operation_time_start.select.optional.form-control.start_time_select option:nth-child(3)").text
        print " the startworktime is ",startworktime
        Select(driver.find_element_by_id("outlet_form_operation_time_start")).select_by_visible_text(startworktime)
        
        driver.execute_script("var doc=document.getElementById('outlet_form_operation_time_end');doc.setAttribute('style','display:block');")
        endworktime=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_operation_time_end div.col-sm-8 select#outlet_form_operation_time_end.select.optional.form-control.end_time_select option:nth-child(5)").text
        print " the endworktime is ",endworktime
        Select(driver.find_element_by_id("outlet_form_operation_time_end")).select_by_visible_text(endworktime)
        
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(1)
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("testjiagongdian")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
            
        cursor.execute("DELETE FROM ims_icard_outlet WHERE title LIKE '%testjiagongdian%'")
        conn.commit()
        cursor.close()
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
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
