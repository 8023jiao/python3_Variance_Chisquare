#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from controllers.HomeHandlers import BaseHandler
from tornado.web import RequestHandler
from common.Base import result, MyGuid, my_datetime, Config, my_log
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor

from core.AnalysisDetails import MyVarianceCore



class MyTestHandler(BaseHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.asynchronous_get()

    def _get(self):
        user = self.get_argument('user', None)
        age = self.get_argument('age', None)
        if age:
            ret = json.dumps(result(status=2000, value="hello : " + user + "age :" + age))
        else:
            ret = json.dumps(result(status=2000, value="hello : " + user))
        return ret

    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        user = self.get_argument('user', None)
        print("post", user)
        ret = json.dumps(result(status=2000, value="hello world!"))
        return ret




