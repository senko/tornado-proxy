#!/usr/bin/env python

import unittest
import urllib2
import subprocess
import os
import time

import tornado.ioloop
import tornado.httpclient

import sys
sys.path.append('../')
from tornado_proxy import run_proxy

class TestStandaloneProxy(unittest.TestCase):
    def setUp(self):
        self.proxy = subprocess.Popen(['python', 'tornado_proxy/proxy.py',
            '8888'])
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

    def test(self):
        base_url = '//httpbin.org/'
        urllib2.urlopen('https:' + base_url + 'get').read()
        urllib2.urlopen('http:' + base_url + 'get').read()
        urllib2.urlopen('https:' + base_url + 'post', '').read()
        urllib2.urlopen('http:' + base_url + 'post', '').read()


class TestTornadoProxy(unittest.TestCase):
    def setUp(self):
        self.ioloop = tornado.ioloop.IOLoop.instance()
        run_proxy(8889, start_ioloop=False)

    def tearDown(self):
        pass

    def test(self):
        def handle_response(resp):
            self.assertIsNone(resp.error)
            self.ioloop.stop()

        tornado.httpclient.AsyncHTTPClient.configure(
            "tornado.curl_httpclient.CurlAsyncHTTPClient")
        client = tornado.httpclient.AsyncHTTPClient()

        req = tornado.httpclient.HTTPRequest('http://httpbin.org/',
            proxy_host='127.0.0.1', proxy_port=8889)
        client.fetch(req, handle_response)
        self.ioloop.start()


if __name__ == '__main__':
    unittest.main()
