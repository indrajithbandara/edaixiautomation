# -*- coding: utf-8 -*-
#encoding:utf-8 xl
import httplib,urllib
import unittest,json
import ConfigParser

class send_sms(unittest.TestCase):
    def setUp(self):
        #self.widget = Widget('The widget')
        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_open.conf")
        global OPEN_URL,pay_order_url,pay_order_params
        OPEN_URL = conf.get("openserversection", "openurl")
        pay_order_url = conf.get("openserversection", "open_pay_order_url")
        pay_order_params = conf.get("openserversection", "open_pay_order_params")
        print " OPEN_URL,pay_order_url,pay_order_params is ",OPEN_URL,pay_order_url,pay_order_params
        httpClient = None
        #self.httpClient = httplib.HTTPConnection('open13.edaixi.cn', 81, timeout=10)
        self.httpClient = httplib.HTTPConnection(OPEN_URL, 81, timeout=10)
    def tearDown(self):
        #self.widget.dispose()
        #self.widget = None
        #self.f.close()
        self.httpClient.close()

    def test_send_sms(self):
        try:
            
            f=open(pay_order_params)
            strcreateoder=json.load(f) 
            print strcreateoder
         
            params = urllib.urlencode(strcreateoder)
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            
            self.httpClient.request('POST', pay_order_url, params, headers)
    
            #response是HTTPResponse对象
            response = self.httpClient.getresponse()
            print response.status
            statucode=response.status
            print response.read()
            if statucode=='200' or statucode=='201':
                print "The get_order_list status is 200 or 201"
            else:
                raise "The get_order_list has exception"
                print response.reason
                print response.read()
            #self.assertEqual(statucode, 200,'incorrect default size')
        except Exception, e:
            print e
        #finally:
            #if self.httpClient:
               #self.httpClient.close()
               

