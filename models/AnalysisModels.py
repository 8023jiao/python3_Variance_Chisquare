#!/usr/bin/env python
# -*- coding:utf-8 -*-

from statsmodels.formula.api import ols
import statsmodels.api as sm
from common.util.mySqlalchemy import sqlalchemy_engine
from common.Base import my_log
import pandas as pd


def MyVarianceModel(variableOne, variableTwo, table, where):
    sql = "select `{}`, `{}` from {}.{} where {};".format(variableOne, variableTwo, "anadata", table, where)
    df = pd.read_sql(sql, sqlalchemy_engine)
    df_dropna = df.dropna()
    return df_dropna


def MyChiSquareModel(variableOne, variableTwo, table, where):
    sql = "select count(1) as count, {} , {}  from {}.{} where {} group by {}, {} order by {}, {};".format(variableOne,
                                                                                                           variableTwo,
                                                                                                           'anadata',
                                                                                                           table, where,
                                                                                                           variableTwo,
                                                                                                           variableOne,
                                                                                                           variableTwo,
                                                                                                           variableOne)
    countSql = "select count(1) as count from {}.{} where {} ;".format('anadata', table, where)
    df = pd.read_sql(sql, sqlalchemy_engine)
    count = pd.read_sql(countSql, sqlalchemy_engine)
    df_dropna = df
    return df_dropna, count
