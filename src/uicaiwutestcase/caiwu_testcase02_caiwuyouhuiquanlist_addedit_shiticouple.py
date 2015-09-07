# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,ConfigParser
from selenium.webdriver.support.ui import WebDriverWait 
import  appobjectcaiwu,caiwu_utiltools
class CaiwuTestcase02caiwuYouhuiquanlistAddEditShitiCouple(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = appobjectcaiwu.GetInstance()
        self.driver.implicitly_wait(30)
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_caiwu.conf")
        global CAIWU_URL,USER_NAME,PASS_WORD
        CAIWU_URL = conf.get("caiwusection", "uihostname")
        USER_NAME = conf.get("caiwusection", "uiusername")
        PASS_WORD = conf.get("caiwusection", "uipassword")
        print CAIWU_URL,USER_NAME,PASS_WORD 
        self.base_url = CAIWU_URL
        #Sself.base_url = "http://caiwu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Caiwu_Testcase02_caiwuyouhuiquanlist_addedit_shiticouple(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("div.container h3.text-center.text-primary a.btn.btn-success.text-center").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        self.assertEqual(driver.title,u"财务")
        #driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown a.dropdown-toggle").click()
        #self.assertEqual(driver.title,u"财务")
       #driver.find_element_by_link_text(u"优惠券列表").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a").click()
        self.assertEqual(driver.title,u"财务")
        time.sleep(1)
        #youhuiquan list add function
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_css_selector("div.container a.btn.btn-info.col-md-1").click()
        #starting add youhuiquan account
        driver.find_element_by_id("coupon_list_form_title_alias").clear()
        driver.find_element_by_id("coupon_list_form_title_alias").send_keys(u"优惠券添加新测试")
        driver.find_element_by_id("coupon_list_form_title").clear()
        driver.find_element_by_id("coupon_list_form_title").send_keys(u"优惠券添加新测试账户")
        driver.find_element_by_id("coupon_list_form_totalnum").clear()
        driver.find_element_by_id("coupon_list_form_totalnum").send_keys("11")
        driver.find_element_by_id("coupon_list_form_least_price").clear()
        driver.find_element_by_id("coupon_list_form_least_price").send_keys("110")
        driver.find_element_by_id("coupon_list_form_coupon_price").clear()
        driver.find_element_by_id("coupon_list_form_coupon_price").send_keys("110")
        
        #html body div.container form#new_coupon_list_form.form-horizontal.new_coupon_list_form div.form-group.select.required.coupon_list_form_coupon_type div.col-sm-8 select#coupon_list_form_coupon_type.select.required.form-control option:nth-child(2)
        yuhuiquantypename=driver.find_element_by_css_selector("div.container form#new_coupon_list_form.form-horizontal.new_coupon_list_form div.form-group.select.required.coupon_list_form_coupon_type div.col-sm-8 select#coupon_list_form_coupon_type.select.required.form-control option:nth-child(2)").text
        print yuhuiquantypename
        Select(driver.find_element_by_id("coupon_list_form_coupon_type")).select_by_visible_text(yuhuiquantypename)
        #div.container form#new_coupon_list_form.form-horizontal.new_coupon_list_form div:nth-child(9) div.col-sm-8 select#coupon_list_form_coupon_type.select.required.form-control option:nth-child(2)     
        #time.sleep(1)
        driver.find_element_by_id("coupon_list_form_limit_count").clear()
        driver.find_element_by_id("coupon_list_form_limit_count").send_keys("10")
        driver.find_element_by_id("coupon_list_form_use_limit").clear()
        driver.find_element_by_id("coupon_list_form_use_limit").send_keys("10")
        time.sleep(2)
#         inputs = driver.find_elements_by_tag_name('input')
#         for input in inputs:
#             if input.get_attribute('type') == 'checkbox':
#                 input.click()
#         time.sleep(2)
        #driver.find_element_by_id("coupon_list_form_exclusive_channels_2").click()
#         driver.find_element_by_id("coupon_list_form_exclusive_channels_1").click()
        #driver.find_element_by_id("coupon_list_form_exclusive_channels_3").click()
#         time.sleep(2)
#         checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
#         for checkbox in checkboxes:
#             checkbox.click()
#         time.sleep(2)
        
        currenttime=str(time.strftime("%d", time.localtime()))
        starttime=str(time.strftime("%Y-%m-", time.localtime()))
        endtime=str(int(currenttime)+1)
        firsttime=starttime+currenttime
        #firsttime="2015-07-31" #print currenttime#print endtime
        finaltime=starttime+endtime
        
        #time.sleep(3)
        driver.find_element_by_id("coupon_list_form_starttime").clear()
        driver.find_element_by_id("coupon_list_form_starttime").send_keys(str(caiwu_utiltools.get_day_of_day(1)))
        driver.find_element_by_id("coupon_list_form_endtime").clear()
        driver.find_element_by_id("coupon_list_form_endtime").send_keys(str(caiwu_utiltools.get_day_of_day(3)))
        
        
        #youxiaoqiname=driver.find_element_by_xpath("/html/body/div[2]/form/div[13]/div/select/option[2]").text
        print firsttime,finaltime
        #youxiaoqiname=driver.find_element_by_css_selector("div.container form#new_coupon_list_form.form-horizontal.new_coupon_list_form div.form-group.select.optional.coupon_list_form_validity_type div.col-sm-8 select#coupon_list_form_validity_type.select.optional.form-control option:first-child").text
        #Select(driver.find_element_by_id("coupon_list_form_validity_type")).select_by_visible_text(u"相对有效期")
        #print youxiaoqiname
        #Select(driver.find_element_by_id("coupon_list_form_validity_type")).select_by_visible_text(youxiaoqiname)
        #driver.find_element_by_id("coupon_list_form_validity_type").send_keys(youxiaoqiname)
        #driver.implicitly_wait(10)
        
        driver.find_element_by_id("coupon_list_form_apply_department").clear()
        driver.find_element_by_id("coupon_list_form_apply_department").send_keys(u"技术测试部")
        
        driver.find_element_by_id("coupon_list_form_applicant").clear()
        driver.find_element_by_id("coupon_list_form_applicant").send_keys("luke")
        
        pingleiname=driver.find_element_by_css_selector("div.container form#new_coupon_list_form.form-horizontal.new_coupon_list_form div.form-group.select.optional.coupon_list_form_category_id div.col-sm-8 select#coupon_list_form_category_id.select.optional.form-control option:nth-child(2)").text
        print " the pingleiname is ",pingleiname
        Select(driver.find_element_by_id("coupon_list_form_category_id")).select_by_visible_text(pingleiname)
        
#         youhuiquangrpname=driver.find_element_by_css_selector("div.container form#new_coupon_list_form.form-horizontal.new_coupon_list_form div.form-group.select.optional.coupon_list_form_coupon_group_id div.col-sm-8 select#coupon_list_form_coupon_group_id.select.optional.form-control option:nth-child(2)").text
#         print " the youhuiquangrpname is ",youhuiquangrpname
#         Select(driver.find_element_by_id("coupon_list_form_coupon_group_id")).select_by_visible_text(youhuiquangrpname)
#         
        Select(driver.find_element_by_id("coupon_list_form_city_id")).select_by_visible_text(u"北京")
        driver.find_element_by_id("coupon_list_form_channel").clear()
        driver.find_element_by_id("coupon_list_form_channel").send_keys("website")
        
        #driver.find_element_by_name("commit").click()
        driver.find_element_by_xpath("/html/body/div[2]/form/input").click()
        #WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container div.info-div div.col-md-6 div.panel.panel-primary.checkout-order div.panel-heading").is_displayed()) 

        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title,u"财务")
        
        
        shitcoupleresult=driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-child(6)").text
  
        print " the shitcoupleresult is ",shitcoupleresult
        self.assertEqual(shitcoupleresult,u"实体优惠码")
        #shitcoupleresult
        #driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-child(11) a:first-child.btn.btn-sm.btn-info").click()
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/table/tbody/tr[20]/td[11]/a[1]").click()
        #html body div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:nth-last-child td:nth-last-child(4) a:first-child.btn.btn-sm.btn-info
        #youhuiquan list edit function
        time.sleep(1)
        driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr:first-child td:nth-last-child(4) a:first-child").click()
        #driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("coupon_list_form_title_alias").clear()
        driver.find_element_by_id("coupon_list_form_title_alias").send_keys("asassedi")
        driver.find_element_by_id("coupon_list_form_title").clear()
        driver.find_element_by_id("coupon_list_form_title").send_keys("asasasasss")
        driver.find_element_by_name("commit").click()
        #self.assert_(driver.title, u"财务")
        self.assertEqual(driver.title,u"财务")
        print driver.title
        #self.assert_(expr, msg)
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
