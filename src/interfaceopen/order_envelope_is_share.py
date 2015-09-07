# -*- coding: utf-8 -*-
#encoding:utf-8 
import httplib,urllib
import unittest

class order_envelope_is_share(unittest.TestCase):
    def setUp(self):
        #self.widget = Widget('The widget')
        httpClient = None
        self.httpClient = httplib.HTTPConnection('open09.edaixi.cn', 81, timeout=10)
    def tearDown(self):
        #self.widget.dispose()
        #self.widget = None
        self.file.close()
        self.httpClient.close()

    def test_order_envelope_is_share(self):
        
        try:
            self.file=open('C:/edaixi_testdata/interface_data/open_order_envelope_is_share.txt','r')
        except IOError:
            print "The file don't exsit,please check it."
            exit()

        try:
            for line in self.file.readlines():
                lineone=line.split()
                print lineone[0]
                print lineone[1]
                params = urllib.urlencode({lineone[0]: lineone[1]})
            
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            
            self.httpClient.request('POST', '/client/v1/get_order_list', params, headers)
    
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




