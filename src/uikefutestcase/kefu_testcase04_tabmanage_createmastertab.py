#!/usr/lib/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser,random ,MySQLdb
import appobjectkefu,kefu_utiltools
class KefuTestcase04TabmanageCreateMastertab(unittest.TestCase):
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
        mysqldatabase = conf.get("databaseconn", "mysqlkefudatabase")
        print mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testcase04_tabmanage_createmastertab(self):
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
        time.sleep(1)
        print " the testcase test_kefu_testcase04_tabmanage_createmastertab is ",driver.title
        self.assertEqual(driver.title,u"客服系统")
        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
        global cursor 
        cursor = conn.cursor() 
        cursor.execute("DELETE FROM tags WHERE name LIKE 'addmastertag%' OR  name LIKE 'addsubtag%'")
        #submit to datatbases
        conn.commit()
        cursor.close()
        conn.close()
        
        driver.find_element_by_css_selector("div.container>div.navbar-collapse.collapse.navbar-responsive-collapse>ul.nav.navbar-nav>li:nth-child("+appobjectkefu.kefu_tab_tabmanage+")>a").click()
        self.assertEqual(driver.title,u"客服系统")
        #driver.find_element_by_id("add_tag").click()
        driver.find_element_by_css_selector("div#container.container div.col-sm-4 a#add_tag").send_keys(Keys.ENTER)
        self.assertEqual(driver.title,u"客服系统")
        #html body div#container.container div.col-sm-4 a#add_tag.btn.btn-success
        driver.find_element_by_id("tag_name").clear()
        driver.find_element_by_id("tag_name").send_keys("addmastertagluke"+str(random.randint(1,100)))
        
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[2]/div/input").click()
        driver.find_element_by_name("commit").click()
        #driver.find_element_by_link_text(u"标签管理").click()
        print driver.title
        assert u"客服系统" in driver.title
    
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
