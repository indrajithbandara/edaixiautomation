#!/usr/lib/python2.7
# -*- coding: utf-8 -*-


f = open('test.txt', 'r')  
print f.read()  
  
f.seek(0)  
print f.read(14)  
  
f.seek(0)  
print f.readline()  
print f.readline()  
  
f.seek(0)  
print f.readlines()  
  
f.seek(0)  
for line in f:  
    print line,  
  
f.close() 


f = open('test.txt', 'r+')  
f.truncate()  
f.write('0123456789abcd')  
  
f.seek(3)  
print f.read(1)  
print f.read(2)  
print f.tell()  
  
f.seek(3, 1)  
print f.read(1)  
  
f.seek(-3, 2)  
print f.read(1)  
  
f.close() 



# coding: utf-8  
f = open('test.txt')  
print '文件名：', f.name  
print '是否处于关闭状态：', f.closed  
print '打开的模式：', f.mode  

