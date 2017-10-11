#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from controllers.HomeHandlers import BaseHandler
from common.base import result, MyGuid, my_datetime, Config, my_log

from core.AnalysisDetails import MyVarianceCore, MyChiSquareCore


class MyVarianceHandler(BaseHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.asynchronous_get()

    def _get(self):
        variableOne = self.get_argument('variableOne', None)
        variableTwo = self.get_argument('variableTwo', None)
        where = self.get_argument('where', None)
        table = self.get_argument('table', None)
        if all([variableOne, variableTwo, where, table]):
            where = where[1:-1]
            status = 2000
            try:
                returnValue = MyVarianceCore(variableOne, variableTwo, table, where)
            except Exception as e:
                my_log.error(e)
                status = 4002
                returnValue = ""
            return json.dumps(result(status=status, value=returnValue))
        else:
            return json.dumps(result(status=4002, value=""))


class MyChiSquareHandler(BaseHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.asynchronous_get()

    def _get(self):
        variableOne = self.get_argument('variableOne', None)
        variableTwo = self.get_argument('variableTwo', None)
        where = self.get_argument('where', None)
        table = self.get_argument('table', None)
        if all([variableOne, variableTwo, where, table]):
            where = where[1:-1]
            status = 2000
            try:
                returnValue = MyChiSquareCore(variableOne, variableTwo, table, where)
                for i in returnValue:
                    returnValue[i] = str(returnValue[i])
            except Exception as e:
                my_log.error(e)
                status = 4002
                returnValue = ""
            return json.dumps(result(status=status, value=returnValue))
        else:
            return json.dumps(result(status=4002, value=""))
