#!/usr/bin/env python

import sys
sys.path.append('../')

import unittest
import urllib2
import subprocess
import os
import time


class TestProxy(unittest.TestCase):
    def setUp(self):
        self.proxy = subprocess.Popen(['python', 'proxy/proxy.py', '8888'])
        proxy_support = urllib2.ProxyHandler({
            "https": "http://localhost:8888",
            "http": "http://localhost:8888"
        })
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        # make sure the subprocess started listening on the port
        time.sleep(1)

    def tearDown(self):
        os.kill(self.proxy.pid, 15)
        time.sleep(1)
        os.kill(self.proxy.pid, 9)

    def test_get(self):
        url = '//httpbin.org/'
        urllib2.urlopen('http:' + url).read()
        urllib2.urlopen('http:' + url).read()


if __name__ == '__main__':
    unittest.main()
