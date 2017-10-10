#!/usr/bin/env python
# -*- coding:utf-8 -*-


from controllers.CreateHandlers import MyTestHandler
from controllers.AnalysisHandlers import MyVarianceHandler, MyChiSquareHandler

urls = list()

testUrls = [
    (r'/index', MyTestHandler),
]

analysisUrls = [
    (r'/MyVariance', MyVarianceHandler), # 方差
    (r'/MyChiSquare', MyChiSquareHandler), # 卡方
]

urls += testUrls + analysisUrls
