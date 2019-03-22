#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : pycache.py
# Create date : 2019-03-22 11:57
# Modified date : 2019-03-22 13:32
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os
import shutil
import tempfile
import sys
from io import open

import tarfile
import requests
from tqdm import tqdm

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

if sys.version > '3':
    from pybase import pylog
else:
    import pylog

def _get_file_path(url):
    parsed = urlparse(url)
    if not parsed.netloc or not parsed.path:
        raise ValueError("bad url path %s" % (url))

    bucket_name = parsed.netloc
    file_path = parsed.path
    if file_path.startswith("/"):
        file_path = file_path[1:]
    return bucket_name, file_path

def _get_file_name_from_path(file_path):
    lt = file_path.split('/')
    return lt[-1]

def _get_file_name(url):
    bucket_name, file_path = _get_file_path(url)
    file_name = _get_file_name_from_path(file_path)
    return file_name

def _http_get(url, temp_file):
    req = requests.get(url, stream=True)
    content_length = req.headers.get('Content-Length')
    total = int(content_length) if content_length is not None else None
    progress = tqdm(unit="B", total=total)
    for chunk in req.iter_content(chunk_size=1024):
        if chunk:
            progress.update(len(chunk))
            temp_file.write(chunk)
    progress.close()

def _create_model_dir(cache_dir):
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

def _write_temp_file(url, cache_path):
    with tempfile.NamedTemporaryFile() as temp_file:
        pylog.info("tempfile: %s" %  (temp_file.name))
        _http_get(url, temp_file)
        temp_file.flush()
        temp_file.seek(0)
        pylog.info("copying %s to cache at %s" % (temp_file.name, cache_path))
        with open(cache_path, 'wb') as cache_file:
            shutil.copyfileobj(temp_file, cache_file)

def _check_is_cached_the_file(url, cache_path):
    if not os.path.exists(cache_path):
        pylog.info("not found %s, downloading %s to tempfile" %  (cache_path, url))
        return False
    else:
        pylog.debug("do not need download, exists %s" % cache_path)
        return True

def download_file_from_web(url, cache_dir):
    _create_model_dir(cache_dir)
    filename = _get_file_name(url)
    cache_path = os.path.join(cache_dir, filename)

    if not _check_is_cached_the_file(url, cache_path):
        _write_temp_file(url, cache_path)
        return False, cache_path
    return True, cache_path
