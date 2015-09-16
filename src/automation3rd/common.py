#!/usr/bin/env python  
#coding=utf-8  
'''
Created on Sep 16, 2015
@author: luke 
'''
import os,logging,ConfigParser  
  
  
def load_config(file_name):  
    ''''' 
    Use ConfigParser to parse below configuration file: 
    [selection]: 
    option:value 
    '''  
    config = ConfigParser.ConfigParser()  
    try:  
        if os.path.exists(file_name):  
            config.read(file_name)  
            return config  
    except:  
        file_name," is not exit"  
  
  
def init_log(log_level,log_path):  
    #log leverl value: CRITICAL 50; ERROR 40; WARNING 30; INFO 20; DEBUG 10, NOSET 0;  
    logger = logging.getLogger()  
      
    hdlr = logging.FileHandler(log_path)  
    formatter = logging.Formatter('%(asctime)s [%(levelname)-8s %(module)s:%(lineno)d] %(message)s')  
    hdlr.setFormatter(formatter)  
    logger.addHandler(hdlr)  
    logger.setLevel(log_level)  
  
    return logger  
  
if __name__=="__main__":  
    log=init_log(0,"monitor.log")  
    monitor_cfg=load_config("monitor.cfg")  
    for section in monitor_cfg.sections():  
        log.info("section is "+section)  
        if section=='sys':  
            log.debug("monitor ip:"+monitor_cfg.get(section,'ip'))  