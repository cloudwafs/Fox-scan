#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import os
import sys
import logging
import json
import base64
import requests
import urllib2
import ssl
# from models import MySQLHander
import xml.etree.cElementTree as ET
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


SPIDER_HEADER = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)" \
                " Version/6.0 Mobile/10A5376e Safari/8536.25"}


def getrootpath():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path[:path.rfind("/")]


class XMLDOM(object):    
    def __init__(self):
        xml = ET.parse("{0}/config.xml".format(getrootpath()))
        self.tree = xml.getroot()

    def GetElementByName(self, name):
        return self.tree.find(name).text

#ensure HTTPAdapter to spider https
class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1)
class Tools:

    @staticmethod
    def do_sqlmap_options(request):
        options = {}
        for key in request.keys():
            if request[key] == "True":
                options[key] = request[key]
        return options

    @staticmethod
    def dict2base64(dictobj):
        return base64.b64encode(json.dumps(dictobj))

    @staticmethod
    def base642json(string):
        return json.loads(base64.b64decode(string))



if __name__ == '__main__':
    t = Tools()
    t.SpiderGetLink("http://fengxuan.com/webapp/discuz2.5/forum.php")