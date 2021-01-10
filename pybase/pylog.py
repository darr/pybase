#!/usr/bin/python
# -*- coding: utf-8 -*-
########################################
# File name : pylog.py
# Create date : 2013-06-20 22:30
# Modified date : 2018-10-20 13:32
# Author : DARREN
# Email : lzygzh@126.com
########################################
from __future__ import division
from __future__ import print_function

import datetime
import sys
import os

from os.path import join, getsize
import operator

if sys.version > '3':
    from pybase import etc
    from pybase import pylog_table
else:
    import etc
    import pylog_table

LOG_LEVEL_DIC = {}
PYLOG_IS_INIT = False

def get_log_level_dic():
    level_dic = {}
    level_dic['all'] = 0
    level_dic['debug'] = 10
    level_dic['info'] = 20
    level_dic['warning'] = 30
    level_dic['error'] = 40
    level_dic['critical'] = 50
    return level_dic

def init_log():
    global LOG_LEVEL_DIC
    global PYLOG_IS_INIT

    LOG_LEVEL_DIC = get_log_level_dic()
    PYLOG_IS_INIT = True

def get_log_file_name():
    return etc.LOG_FILE_NAME

def get_log_file_path():
    return etc.LOG_FILE_PATH

def get_file_log_level():
    return etc.LOG_WRITE_LEVEL

def get_file_db_log_level():
    return etc.LOG_WRITE_DB_LEVEL

def get_print_log_level():
    return etc.LOG_PRINT_LEVEL

def get_print_log_all_info_level():
    return etc.LOG_PRINT_ALL_INFO_LEVEL

def get_log_full_name(log_path=""):
    if log_path:
        full_path = '%s%s' %(log_path, datetime.datetime.now().strftime('%Y-%m-%d'))
    else:
        full_path = '%s%s' %(get_log_name(), datetime.datetime.now().strftime('%Y-%m-%d'))
    return full_path

def get_log_name():
    path = get_log_file_path()
    if not os.path.isdir(path):
        os.makedirs(path)
    return '%s%s' % (path, get_log_file_name())

def write_log(log, log_path=""):
    full_fill_name = get_log_full_name(log_path)
    if os.path.isfile(full_fill_name):
        pass
    else:
        check_dir_size()
        full_fill_name = get_log_full_name(log_path)
    file_object = open(full_fill_name, 'a')
    try:
        file_object.write(log)
    finally:
        file_object.close()
        
def out_put_log2(level, content, log_path="", log_key="log", stack_layer=2, ):
    func_name = sys._getframe(stack_layer).f_code.co_name
    file_name = sys._getframe(stack_layer).f_code.co_filename
    line = sys._getframe(stack_layer).f_lineno
    now_time = datetime.datetime.now()
    log_format = 'LEVEL:%s, LINE:%s, FUNC:%s, FILE:%s, TIME:%s, CONTENT:%s\n'
    #log_format = 'LEVEL:%s, LINE:%s, FUNC:%s, FILE:%s, TIME:%s, CONTENT:%s'
    con = log_format % (level, line, func_name, file_name, now_time, content)

    if is_print_log(level):
        if is_print_log_all_info(level):
            #print(con)
            print_str = con
            sys.stdout.write(print_str)
            sys.stdout.flush()
        else:
            f_name = file_name.split('/')[-1]
            #print("%s line:%s %s" % (f_name, line, content))
            print_str = "%s line:%s %s\n" % (f_name, line, content)
            sys.stdout.write(print_str)
            sys.stdout.flush()

    if is_write_log(level):
        write_log("%s\n" % con, log_path)

def get_description_str(content, stack_layer=2):
    func_name = sys._getframe(stack_layer).f_code.co_name
    file_name = sys._getframe(stack_layer).f_code.co_filename
    line = sys._getframe(stack_layer).f_lineno
    log_format = 'LINE:%s, FUNC:%s, FILE:%s, CONTENT:%s'
    con = log_format % (line, func_name, file_name, content)
    return con

def out_put_log(level, content, log_path="", log_key="log", stack_layer=2,):
    func_name = sys._getframe(stack_layer).f_code.co_name
    file_name = sys._getframe(stack_layer).f_code.co_filename
    line = sys._getframe(stack_layer).f_lineno
    now_time = datetime.datetime.now()
    log_format = 'LEVEL:%s, LINE:%s, FUNC:%s, FILE:%s, TIME:%s, CONTENT:%s\n'
    con = log_format % (level, line, func_name, file_name, now_time, content)

    if is_print_log(level):
        if is_print_log_all_info(level):
            print(con)
        else:
            f_name = file_name.split('/')[-1]
            print("%s line:%s %s" % (f_name, line, content))

    if is_write_log(level):
        write_log(con, log_path)

    if is_write_db_log(level):
        log_table = pylog_table.PylogTable()
        item_dic = {}
        item_dic['level'] = level
        item_dic['line'] = line
        item_dic['func'] = func_name
        item_dic['filename'] = file_name
        item_dic['time'] = now_time
        item_dic['content'] = content
        item_dic['log_key'] = log_key
        log_table.insert(item_dic)

def check_dir_size():
    dir_name = get_log_file_path()
    dir_size = get_dir_size(dir_name)
    if dir_size > 200*1024*1024:
        delete_log_dir()

def get_dir_size(dir_name):
    size = 0
    for root, dirs, files in os.walk(dir_name):
        size += sum([getsize(join(root, name)) for name in files])
    return size

def delete_log_dir():
    dir_name = get_log_file_path()
    delete_file_folder(dir_name)

def delete_file_folder(src):
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass

def debug(content, log_path="",):
    level = 'debug'
    out_put_log(level, content, log_path,)

def auto_test_debug(content, log_path=""):
    level = 'debug'
    out_put_log(level, content, log_path, stack_layer=3)

def error(content, log_path=""):
    level = 'error'
    out_put_log(level, content, log_path)

def auto_test_error(content, log_path=""):
    level = 'error'
    out_put_log(level, content, log_path, stack_layer=3)

def warning(content, log_path=""):
    level = 'warning'
    out_put_log(level, content, log_path)

def info(content, log_path=""):
    level = 'info'
    out_put_log(level, content, log_path)

def auto_test_info(content, log_path=""):
    level = 'info'
    out_put_log(level, content, log_path, stack_layer=3)

def critical(content, log_path=""):
    level = 'critical'
    out_put_log(level, content, log_path)

def condition_value_is_null(content=""):
    error(content)

def is_print_log(log_level):
    global LOG_LEVEL_DIC
    config_log_level = LOG_LEVEL_DIC[get_print_log_level()]
    current_log_level = LOG_LEVEL_DIC[log_level]
    if current_log_level >= config_log_level:
        return True
    return False

def is_print_log_all_info(log_level):
    global LOG_LEVEL_DIC
    config_log_level = LOG_LEVEL_DIC[get_print_log_all_info_level()]
    current_log_level = LOG_LEVEL_DIC[log_level]
    if current_log_level >= config_log_level:
        return True
    return False

def is_write_log(log_level):
    global LOG_LEVEL_DIC
    config_log_level = LOG_LEVEL_DIC[get_file_log_level()]
    current_log_level = LOG_LEVEL_DIC[log_level]
    if current_log_level >= config_log_level:
        return True
    return False

def is_write_db_log(log_level):
    global LOG_LEVEL_DIC
    config_log_level = LOG_LEVEL_DIC[get_file_db_log_level()]
    current_log_level = LOG_LEVEL_DIC[log_level]
    if current_log_level >= config_log_level:
        return True
    return False

def test_compare_value(real_value, expected_value):
    if real_value != expected_value:
        auto_test_error("real:%s expect:%s" % (real_value, expected_value))
    else:
        auto_test_debug("real:%s expect:%s" % (real_value, expected_value))
        
def test_compare_data(real_value, expected_value):
    if not operator.eq(real_value ,expected_value):
        auto_test_error("real:%s expect:%s" % (real_value, expected_value))
    else:
        auto_test_debug("real:%s expect:%s" % (real_value, expected_value))


init_log()
