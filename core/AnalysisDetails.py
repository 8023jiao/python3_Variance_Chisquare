#!/usr/bin/env python
# -*- coding:utf-8 -*-

from models.AnalysisModels import MyVarianceModel, MyChiSquareModel
from common.util.myAnalysis import MyChiSquare2way, MyVariance
from scipy.stats import chisqprob
from common.base import my_log
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm
from pandas import DataFrame



def MyVarianceCore(variableOne, variableTwo, table, where):
    df_dropna = MyVarianceModel(variableOne, variableTwo, table, where)
    ret = MyVariance(df_dropna, variableOne, variableTwo)
    return ret


def MyChiSquareCore(variableOne, variableTwo, table, where):
    df_dropna = MyChiSquareModel(variableOne, variableTwo, table, where)
    ret = MyChiSquare2way.run(df_dropna, variableOne, variableTwo)
    return ret


if __name__ == '__main__':
    ret = MyChiSquareCore("P2Q01", "ZYDM", "dc_bys2017_dataandusers", "XLDMA=1")
    print(ret)
