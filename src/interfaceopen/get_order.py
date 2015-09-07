# -*- coding: utf-8 -*-
#encoding:utf-8 
import httplib
import unittest

class get_order(unittest.TestCase):
    def setUp(self):
        #self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)
    def tearDown(self):
        #self.widget.dispose()
        #self.widget = None
        self.httpClient.close()

    def test_get_order(self):
        try:
            
            self.httpClient.request('GET', '/client/v1/get_order?user_id=11452&order_id=12173793044055')
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


