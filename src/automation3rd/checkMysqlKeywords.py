# coding: utf8
# -*- coding: utf-8 -*-
import time,random
import datetime
import ConfigParser,MySQLdb
import unittest, time, re


class checkMysqlKeywordsClass(unittest.TestCase):
    def setUp(self):
        global dict_data,conn,cursor
        dict_data = {}
        with open('C://edaixi_testdata//mysqlkeyword.txt', 'r') as df:
            for kv in [d.strip().split(' ') for d in df]:
                   dict_data[kv[0]] = kv[1]

        conf = ConfigParser.ConfigParser()
        conf.read("C:/edaixi_testdata/userdata_3rd.conf")
        global validator_table_name_ims_washing_order,mysqlhostname,mysqlusername,mysqlpassword,mysqldatabase
        validator_table_name_ims_washing_order = conf.get("3rdsection", "validator_table_name_ims_washing_order")                           

        mysqlhostname = conf.get("databaseconn", "mysqlhostname")
        mysqlusername = conf.get("databaseconn", "mysqlusername")
        mysqlpassword = conf.get("databaseconn", "mysqlpassword")
        mysqldatabase = conf.get("databaseconn", "mysqlrongchangdb")
        
        print validator_table_name_ims_washing_order
    def test_checkMysqlKeywordsMethod(self):



        conn=MySQLdb.connect(host=mysqlhostname,user=mysqlusername,passwd=mysqlpassword,db=mysqldatabase,charset="utf8")    
        global cloumnname,table_ims_washing_order
        cursor = conn.cursor()
        #table_ims_washing_order="ims_washing_order"
        table_ims_washing_order=validator_table_name_ims_washing_order
#         n = cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name LIKE '"+table_ims_washing_order+"';")
#         for row in cursor.fetchall():
#         #print " the row is ",str(row)[3:-3]
#             cloumnname=str(row)[3:-3]
#             for k in dict_data:
#                 #print " Mysql Keywords dict_data[k] file dict is ",dict_data[k]
#                 #self.assertEqual(dict_data[k], cloumnname)
#                 if dict_data[k]==cloumnname:
#                    print "the table",table_ims_washing_order," has column name ",cloumnname," is exsit on ruby baoliiu keyword"
#                    raise ValueError(" the table has column name exsit on MYSQL Table keywords")
#                    
#                 else:
#                    print ""
#                    pass
    
        databasename="rongchain04"
        n = cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='"+databasename+"';")
        for row in cursor.fetchall():
            #print str(row)
            tablename=str(row)[3:-3]
            #print " test 05 datatbase rongchain04",tablename

            n = cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name LIKE '"+tablename+"';")
            for row in cursor.fetchall():
            #print " the row is ",str(row)[3:-3]
                cloumnname=str(row)[3:-3]
                for k in dict_data:
                #print " Mysql Keywords dict_data[k] file dict is ",dict_data[k]
                #self.assertEqual(dict_data[k], cloumnname)
                   if dict_data[k].lower()==cloumnname.lower():
                      print "the table",tablename," has column name ",cloumnname," is exsit on mysql revise keyword"
                      raise ValueError(" the table has column name exsit on MYSQL Table keywords")
                   else:
                      print ""
                      pass
           
           
if __name__ == "__main__":
    unittest.main()

