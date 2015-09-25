# #encoding: utf-8
# import mysql
# __author__ = 'Administrator'
# config={'host':'127.0.0.1',#默认127.0.0.1
#         'user':'root',
#        'password':'root',
#        'port':3306 ,#默认即为3306
#         'database':'test',
#        'charset':'utf8'#默认即为utf8
#        }
# if __name__=="__main__":
#     print(config['host'])
#     cnx =mysql.connector.connect(user=config['user'],password=config['password'],host=config['host'],port=config['port'],database=config['database'])
#     cursor =cnx.cursor()
#     cursor.execute("select * from job")
#     for _row in cursor.fetchall():
#         print(_row[1])
#         pass


#encoding: utf-8
# __author__ = 'Administrator'
# import psycopg2
# import ppygis
# import datetime
# import string
# import sys
# import logging
# import GeowayLogger
# reload(sys)
# #中文错误
# sys.setdefaultencoding( "utf-8" )
# vLog = GeowayLogger.GeowayLogger("c://geoway2.log",logging.DEBUG)
# vLog.start()
# #postgis
# #pgisCon = psycopg2.connect(database="postgis_21_sample",user="postgres",password="")
# pgisCon = psycopg2.connect(database="postgis_21_sample",user="postgres",password="postgres",host="192.98.12.60",port="5432")
# pgisCursor = pgisCon.cursor()
#  
# pgisCursor.execute("create table IF NOT EXISTS  tianditupoi_agg(id integer PRIMARY KEY,geometry GEOMETRY)")
# pgisCursor.execute("create table IF NOT EXISTS  tianditupoi_1( check (id >= 0 and id< 2500001) ) INHERITS (tianditupoi_agg)")
# pgisCursor.execute("create table IF NOT EXISTS  tianditupoi_2( check (id >= 2500001) ) INHERITS (tianditupoi_agg)")
# #创建分区表ID索引
# pgisCursor.execute("CREATE INDEX tianditupoi_1_idindex on tianditupoi_1(id)")
# pgisCursor.execute("CREATE INDEX tianditupoi_2_idindex on tianditupoi_2(id)")
# #创建分区规则
# pgisCursor.execute("CREATE RULE tianditupoi_insert_1 AS ON INSERT TO tianditupoi_agg WHERE (id >= 0 and id < 2500001) DO INSTEAD INSERT INTO tianditupoi_1 VALUES (NEW.id,NEW.geometry)")
# pgisCursor.execute("CREATE RULE tianditupoi_insert_2 AS ON INSERT TO tianditupoi_agg WHERE (id >= 2500001 ) DO INSTEAD INSERT INTO tianditupoi_2 VALUES (NEW.id,NEW.geometry)")
# pgisCon.commit()
# #创建天地图要素分区表，并将数据进行转移
# def fromTdtPoi2TdtPoiAg():
#      #sql_txt = sqlite3.connect("c://POI.tdb")
#      startTime = datetime.datetime.now();
#      cusor = pgisCon.cursor()
#      cusor.execute("select oid,st_astext(geom) as geometry from tianditupoi")
#      #row = cusor.fetchone()
#      i = 0;
#      for _row in cusor.fetchall():
#         #print _row
#         #_p = {"name":_row[1],"address":_row[2],"loc":[_row[9],_row[10]]}
#         #poi.insert(_p)
#         geo ="%s"%(_row[1])
#         istr = 'insert into tianditupoi_agg(id,geometry)values(%d,%s)'%(string.atoi(_row[0]),"'"+geo+"'")
#         i = i+1
#         #logging.info("运行日志：%s"%(istr))
#         #pgisCursor.execute("insert into poi(id,name,address,geometry)values("+(_row[0])+",'"+(_row[1])+"','"+(_row[1])+"',"+ppygis.Point(_row[9], _row[10])+")")
#         pgisCursor.execute(istr)
#         #一千条提交一次
#         if i>= 50000 :
#             pgisCon.commit()
#             print("执行中....")
#             i = 0
#  
#     #最后提交一次
#      pgisCon.commit()
#      endTime = datetime.datetime.now()
#      print("数据导入总耗时：%s描述"%((endTime - startTime).seconds))
#      print("插入完毕...")
#      #更新空间参考ID
#      pgisCursor.execute("update tianditupoi_1 set geometry = ST_SetSRID(geometry,4326)")
#      pgisCursor.execute("update tianditupoi_2 set geometry = ST_SetSRID(geometry,4326)")
#      #创建分区表空间索引
#      pgisCursor.execute("create index tianditupoi2_geo_index on tianditupoi_2 using gist(geometry)")
#      pgisCursor.execute("create index tianditupoi1_geo_index on tianditupoi_1 using gist(geometry)")
#      print("空间索引创建完毕...")
#      pgisCursor.close()
#      pgisCon.commit()
#      pgisCon.close()
#  
# #进行数据导入
# fromTdtPoi2TdtPoiAg()