# -*- coding: utf-8 -*-
#encoding:utf-8 
import httplib,urllib
import unittest,json

class app_status_list(unittest.TestCase):
    def setUp(self):
        #self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)
    def tearDown(self):
        #self.widget.dispose()
        #self.widget = None
        self.httpClient.close()

    def test_app_status_list(self):
        try:
            
            f=open("C://edaixi_testdata//interface_data//open_create_order.json")
            strcreateoder=json.load(f) 
            print strcreateoder
            
            ''''params = urllib.urlencode({'user_id': 'true','user_type': 'true',
                                       'totalnum': 'true','paytype': 'true',
                                       'comment': 'true','order_date': 'true',
                                       'order_time': 'true','order_place': 'true',
                                       'good': 'true','coupon_id': 'true',
                                       'skip_quota_check': 'true','need_detail': 'true'})'''
            params = urllib.urlencode(strcreateoder)
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            
            self.httpClient.request('POST', '/client/v1/create_order', params, headers)
    
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