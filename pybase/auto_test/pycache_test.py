#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pycache_test.py
# Create date : 2019-03-22 11:58
# Modified date : 2019-03-22 13:31
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import sys
import os
sys.path.append("..")
import pycache
import pylog

def _test_download_file():
    url = "http://lzygzh-low.oss-cn-beijing.aliyuncs.com/deep_model/nlp/openai-gpt/openai-gpt-config.json"
    cache_dir = "./data"
    is_cached_before_down, path = pycache.download_file_from_web(url, cache_dir)
    if is_cached_before_down:
        pass
        # the file has been cached before down
    else:
        pass
        # cached the file this time, and can do thing like, decompression or install

    # delete the file down load
    os.system("rm %s" % path)

def test():
    _test_download_file()
