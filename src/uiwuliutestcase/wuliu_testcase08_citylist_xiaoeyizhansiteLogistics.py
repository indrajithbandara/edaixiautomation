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
import appobjectwuliu,wuliu_utiltools,random
class WuliuTestcase08CitylistxiaoeyizhansiteLogistics(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()wuliu_testcase08_citylist_xiaoeyizhansiteLogistics
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
    
    def test_wuliu_testcase08_citylist_xiaoeyizhansiteLogistics(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testassse test_wuliu_testcase08_citylist_xiaoeyizhansiteLogistics is ",driver.title
        time.sleep(1)
        self.assertEqual(driver.title, u"物流")
        
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        #driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+str(9)+") >a").click()
        driver.find_element_by_css_selector("div.container > nav > ul > li:nth-child("+appobjectwuliu.wuliutabnine_citylist+") >a").click() 
        #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+str(9)+").active a").click()
        
        self.assertEqual(driver.title, u"物流")
     
        driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(10)").click()
        #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:nth-child(2) td:nth-child(2).btn-link a:nth-child(4).btn.btn-success
    
        self.assertEqual(driver.title, u"物流")
    
        print " the str(random.randint(0,999)) is ",str(random.randint(0,999))
        #driver.find_element_by_link_text(u"新建驿站人员").click()
        driver.find_element_by_css_selector("div#container.container a.btn.btn-info.col-md-1").click()
        
#         telephonenumber="18611110"+str(random.randint(0,999))
#         print " the telephonenumber is ",telephonenumber
        telephonenumber=random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
        print " the telephonenumber is ",telephonenumber
        driver.find_element_by_id("outlet_form_title").clear()
        driver.find_element_by_id("outlet_form_title").send_keys(u"xiaoeyizhantest")
        driver.find_element_by_id("outlet_form_tel").clear()
        driver.find_element_by_id("outlet_form_tel").send_keys(telephonenumber)
        Select(driver.find_element_by_id("outlet_form_area")).select_by_visible_text(u"朝阳区")
        driver.find_element_by_id("outlet_form_address").clear()
        driver.find_element_by_id("outlet_form_address").send_keys(u"朝阳区酒仙桥")
        driver.find_element_by_id("get_pos").click()
        time.sleep(1)
        driver.find_element_by_id("set_move").click()
        time.sleep(1)
        
        driver.execute_script("var doc=document.getElementById('outlet_form_server_outlet_id');doc.setAttribute('style','display:block');")
        
        
        servicesitename=driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order div.panle-body div.orders_container form#new_outlet_form.form-horizontal.new_outlet_form div.form-group.select.optional.outlet_form_server_outlet_id div.col-sm-8 select#outlet_form_server_outlet_id.select.optional.form-control.server_outlet_select option:nth-child(2)").text
        print " the servicesitename is  ",servicesitename
        Select(driver.find_element_by_id("outlet_form_server_outlet_id")).select_by_visible_text(servicesitename)

        driver.find_element_by_name("commit").click()
        time.sleep(2)
        self.assertEqual(driver.title, u"物流")
        #html body div#container.container>table.table.table-striped>tbody>tr:nth-child(2)>td:last-nth-child(2)>a
        #driver.find_element_by_link_text(u"编辑").click()
        
#         driver.find_element_by_css_selector("div#container.container>table.table.table-striped>tbody>tr:nth-child(2)>td:nth-last-child(2)>a:first-child").click()
#         driver.find_element_by_id("outlet_form_title").clear()
#         driver.find_element_by_id("outlet_form_title").send_keys(u"小e驿站test1")
#         driver.find_element_by_name("commit").click()
#         driver.find_element_by_id("title").clear()
#         driver.find_element_by_id("title").send_keys(u"小e驿站test1")
#         driver.find_element_by_name("commit").click()
#         time.sleep(2)
#         self.assertEqual(driver.title, u"物流")
#         driver.find_element_by_xpath("//div[@onclick=\"$('#action_target').val(289); $('#map_box').css('visibility', 'visible');if (true && true){ map_controller.mapObj.setCenter(new AMap.LngLat(116.49463,39.970087))}\"]").click()
#         driver.find_element_by_xpath("//div[@id='map_container']/div/div/div/canvas[2]").click()
#         driver.find_element_by_xpath("//div[@id='map_container']/div/div/div/canvas[2]").click()
#         driver.find_element_by_xpath("//div[@id='map_container']/div/div/div/canvas[2]").click()
#         driver.find_element_by_css_selector("div.pull-right > div.pull-right").click()
#         driver.find_element_by_xpath("//div[@onclick=\"$('#action_target').val(289); $('#map_box').css('visibility', 'visible');if (true && true){ map_controller.mapObj.setCenter(new AMap.LngLat(116.49463,39.970087))}\"]").click()
#         driver.find_element_by_xpath("//div[@id='map_container']/div/div/div/canvas[2]").click()
#         driver.find_element_by_xpath("//div[@id='map_container']/div/div/div/canvas[2]").click()
#         driver.find_element_by_css_selector("div.pull-right > div.pull-right").click()
#         self.assertEqual(driver.title, u"物流")
        
        cursor.execute("DELETE FROM ims_icard_outlet where tel='"+telephonenumber+"'")
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
