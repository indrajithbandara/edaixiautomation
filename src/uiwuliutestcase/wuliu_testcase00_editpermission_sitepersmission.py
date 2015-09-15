#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re ,ConfigParser,MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
import appobjectwuliu,wuliu_utiltools
class WuliuTestcase00EditSitePermission(unittest.TestCase):
    def setUp(self):
        #self.verificationErrors=[]
        #self.driver = webdriver.Firefox()
        self.driver = appobjectwuliu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read(wuliu_utiltools.getwuliuconfigpath())   
        #conf.read("C:/edaixi_testdata/userdata_wuliu.conf")
        global WULIU_URL,USER_NAME,PASS_WORD,mysqlhostname,mysqlusername,mysqlpassword,mysqlrongchangdb
        WULIU_URL = conf.get("wuliusection", "uihostname")
        USER_NAME = conf.get("wuliusection", "siteuiusername")
        PASS_WORD = conf.get("wuliusection", "siteuipassword")
        print WULIU_URL,USER_NAME,PASS_WORD  
        self.base_url = WULIU_URL
        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqlrongchangdb  = conf.get("databaseconn", "mysqlrongchangdb")
        
        print mysqlhostname,mysqlusername,mysqlpassword,mysqlrongchangdb
        #self.base_url = "http://wuliu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_testcase00_EditSitePermission(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")

        loginclick=driver.find_element_by_css_selector("div#container.container h3.text-center.text-primary a.btn.btn-success.text-center")
        ActionChains(driver).double_click(loginclick).perform()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        print " the testcase WuliuTestcase00EditSitePermission is ",driver.title
        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        wuliu_utiltools.updateSignNumber()
        driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:nth-child("+appobjectwuliu.wuliutabone+").dropdown a").click()
        self.assertEqual(driver.title, u"物流")      
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]/ul/li[1]/a").click()
        self.assertEqual(driver.title, u"物流")
        driver.find_element_by_id("bagsn").clear()
        driver.find_element_by_id("bagsn").send_keys(wuliu_utiltools.signbagnumber)
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        time.sleep(2)
        #html body div#container.container div.panel.panel-primary p.text-center b#check_in_msg
        qianshouresult=driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>p.text-center>b#check_in_msg").text
        print " the qianshouresult failed  is ",qianshouresult
        if u"签收成功！" in qianshouresult:
            print " sign has been successful  using cuij persmission account ."
        else:
            #assert u"签收失败！" in qianshouresult
        
# qianshou success for 00 permission
         conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqlrongchangdb,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        
        cursor.execute("UPDATE ims_washing_order SET status_delivery='1' ,qianshoudian_id= NULL WHERE bagsn='"+appobjectwuliu.testdata_bagsnnumber+"'")
        conn.commit()
        
#         n = cursor.execute("SELECT ordersn,bagsn,status_delivery,jiagongdian_id,qianshoudian_id  FROM ims_washing_order WHERE bagsn='E0000000006'") 
#         for i in xrange(cursor.rowcount):
#             ordersn ,bagsn,status_delivery,jiagongdian_id,qianshoudian_id = cursor.fetchone()
#         print ordersn ,bagsn,status_delivery,jiagongdian_id,qianshoudian_id
        time.sleep(1)
        driver.find_element_by_id("bagsn").clear()
        driver.find_element_by_id("bagsn").send_keys(appobjectwuliu.testdata_bagsnnumber)
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        qianshouresult=driver.find_element_by_css_selector("div#container.container>div.panel.panel-primary>p.text-center>b#check_in_msg").text
        print " the qianshouresult success is ",qianshouresult
#         assert u"签收成功！" in qianshouresult
        if u"输入的封签号/订单号不存在！" in qianshouresult:
            print " the order number or bagsn is not exsit!. please check database ,thanks"
        else:
            assert u"出库成功" in qianshouresult
        time.sleep(2)

        driver.find_element_by_link_text(u"站点出入库管理").click()
        driver.find_element_by_link_text(u"出库").click()
        driver.find_element_by_id("order_key").clear()
        driver.find_element_by_id("order_key").send_keys(appobjectwuliu.testdata_bagsnnumber)
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")

        time.sleep(2)
#         driver.find_element_by_link_text(u"站点出入库管理").click()
#         driver.find_element_by_link_text(u"出库").click()
#         driver.find_element_by_id("order_key").clear()
#         driver.find_element_by_id("order_key").send_keys("")
#         driver.find_element_by_name("commit").click()
#         zhandianchukuresult=driver.find_element_by_css_selector("html body div#container.container div.panel.panel-primary p.text-center b#check_in_msg").text
#         print " the zhandianchukuresult null is ",zhandianchukuresult
#         assert u"出库成功" in zhandianchukuresult
        
        zhandianchukuresult=driver.find_element_by_css_selector("html body div#container.container div.panel.panel-primary p.text-center b#check_in_msg").text
        print " the zhandianchukuresult null is ",zhandianchukuresult
        if u"输入的封签号不存在！" in zhandianchukuresult:
            print " the order number or bagsn is not exsit!. please check database ,thanks"
        else:
            assert u"出库成功" in zhandianchukuresult
        
        time.sleep(2)
        driver.find_element_by_link_text(u"站点出入库管理").click()
        driver.find_element_by_link_text(u"出入库查询").click()
#         driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        Select(driver.find_element_by_id("in_out_type")).select_by_visible_text(u"出库")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        Select(driver.find_element_by_id("target_type")).select_by_visible_text(u"加工店")
        driver.find_element_by_name("commit").click()
        self.assertEqual(driver.title, u"物流")
        wuliu_utiltools.getcloseconn()
#         driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]/a").click()
#         #driver.find_element_by_css_selector("div.container nav.collapse.navbar-collapse.bs-navbar-collapse ul.nav.navbar-nav li:first-child.active a").click()
#         driver.find_element_by_id("name").clear()
#         driver.find_element_by_id("name").send_keys(u"技术测试账号1")
#         driver.find_element_by_name("commit").click()
#         self.assertEqual(driver.title, u"物流")
#         time.sleep(2)
# 
#         #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped tbody tr:last-child td:last-child div.btn-toolbar a.btn.btn-sm.btn-success
#         driver.find_element_by_css_selector("div#container.container div.panel.panel-primary.checkout-order table.table.table-striped tbody tr:last-child td:last-child div.btn-toolbar a").click()
#         #html body div#container.container div.panel.panel-primary.checkout-order table.table.table-striped.city-table tbody tr:last-child td:last-child a.btn.btn-info.btn-xs
#         driver.find_element_by_id("worker_is_shouyidian").click()
#         driver.find_element_by_id("worker_is_jiagongdian").click()
#         driver.find_element_by_id("worker_is_zb_yunying").click()
#         driver.find_element_by_name("commit").click()
#         #self.asser.assertTrue(driver.title, u"物流111")
#         self.assertEqual(driver.title, u"物流")
        
        

        #driver.get_screenshot_as_file("C:\\edaixi_testdata\\myluke.png")
        
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
