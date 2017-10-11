#!/usr/bin/env python
# -*- coding:utf-8 -*-


from common.util.mySqlalchemy import sqlalchemy_engine
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
    df = pd.read_sql(sql, sqlalchemy_engine)
    df_dropna = df
    return df_dropna
