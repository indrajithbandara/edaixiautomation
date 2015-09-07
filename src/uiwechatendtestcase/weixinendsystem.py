# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from uiwechatendtestcase import appobjectwechat

class Weixin(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = appobjectwechat.GetInstance()
        self.driver.implicitly_wait(30)
        self.base_url = "http://weixin03.edaixi.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_weixin(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_link_text(u"退出").click()
#         driver.find_element_by_id("username").clear()
#         driver.find_element_by_id("username").send_keys("test")
#         driver.find_element_by_id("password").clear()
#         driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_link_text("login with cas").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"如果你的浏览器没有自动跳转，请点击此链接").click()
        driver.find_element_by_link_text(u"基本设置").click()
        driver.find_element_by_link_text(u"测试用户").click()
#         driver.find_element_by_link_text(u"荣昌e袋洗").click()
#         driver.find_element_by_link_text(u"基本设置").click()
#         driver.find_element_by_link_text(u"基本设置").click()
#         driver.find_element_by_link_text(u"基本设置").click()
        driver.find_element_by_link_text(u"文字回复").click()
        driver.find_element_by_link_text(u"图文回复").click()
        driver.find_element_by_link_text(u"默认关键字").click()
#         driver.find_element_by_link_text(u"默认关键字").click()
#         driver.find_element_by_link_text(u"默认关键字").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"主要业务").click()
#         driver.find_element_by_link_text(u"主要业务").click()
#         driver.find_element_by_link_text(u"主要业务").click()
        driver.find_element_by_link_text(u"基本设置").click()
        driver.find_element_by_link_text(u"默认关键字").click()
        driver.find_element_by_link_text(u"主要业务").click()
        driver.find_element_by_link_text(u"微信优惠券").click()
        driver.find_element_by_link_text(u"发送优惠券").click()
        driver.find_element_by_link_text(u"自定义批量发送").click()
        driver.find_element_by_link_text(u"二维码").click()
        driver.find_element_by_link_text(u"生成二维码").click()
        driver.find_element_by_link_text(u"管理二维码").click()
        driver.find_element_by_link_text(u"小e二维码").click()
        driver.find_element_by_link_text(u"手Q二维码").click()
        driver.find_element_by_link_text(u"扫描统计").click()
        driver.find_element_by_link_text(u"批量创建").click()
        driver.find_element_by_link_text(u"批量修改").click()
        driver.find_element_by_link_text(u"设置").click()
        driver.find_element_by_link_text(u"管理组").click()
        driver.find_element_by_link_text(u"菜单管理").click()
        driver.find_element_by_link_text(u"积分").click()
        driver.find_element_by_link_text(u"积分规则").click()
        driver.find_element_by_link_text(u"红包").click()
        driver.find_element_by_link_text(u"链接红包").click()
        driver.find_element_by_link_text(u"订单红包").click()
        driver.find_element_by_link_text(u"订单红包").click()
        driver.find_element_by_link_text(u"游戏红包").click()
        driver.find_element_by_link_text(u"推荐红包").click()
        driver.find_element_by_link_text(u"电话发券").click()
        driver.find_element_by_link_text(u"物流").click()
        driver.find_element_by_link_text(u"推广").click()
        driver.find_element_by_link_text(u"渠道列表").click()
        driver.find_element_by_link_text(u"渠道列表").click()
        driver.find_element_by_link_text(u"web下单链接").click()
        driver.find_element_by_link_text(u"渠道列表").click()
        driver.find_element_by_link_text(u"推广").click()
        driver.find_element_by_link_text(u"红包").click()
        driver.find_element_by_link_text(u"物流").click()
        driver.find_element_by_link_text(u"物流").click()
        driver.find_element_by_link_text(u"物流").click()
        driver.find_element_by_link_text(u"物流").click()
        driver.find_element_by_link_text(u"物流").click()
        print " weixin end testing is ",driver.title
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
