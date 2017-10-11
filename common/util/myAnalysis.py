#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scipy.stats import chisqprob
from common.base import my_log
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm
from pandas import DataFrame


def MyVariance(df_dropna, variableOne, variableTwo):
    try:
        # df_dropna = MyVarianceModel(variableOne, variableTwo, table, where)
        flag = 1
        expr = '{}~C({})'.format(variableOne, variableTwo)
        v2sum = 0
        for i in range(len(df_dropna[variableTwo])):
            if (df_dropna[variableTwo]).iloc[0] == (df_dropna[variableTwo]).iloc[i]:
                v2sum += 1
        if v2sum == len(df_dropna[variableTwo]):
            flag = 0

        if flag == 1:
            mod = ols(expr, data=df_dropna).fit()
            anova_table = sm.stats.anova_lm(mod)
            ret = {'df': list(anova_table.df),
                   'sum_sq': list(anova_table.sum_sq),
                   'mean_sq': list(anova_table.mean_sq),
                   'F': list(anova_table.F)[0],
                   'P': list(anova_table.values.T[-1])[0]
                   }
        else:
            ret = {"df": "NAN", "sum_sq": "NAN", "mean_sq": "NAN", "F": "NAN", "P": "NAN"} # P大写

    except Exception as e:
        my_log.error(e)
        ret = {"df": "NAN", "sum_sq": "NAN", "mean_sq": "NAN", "F": "NAN", "P": "NAN"}

    return ret


class MyChiSquare2way():
    def __init__(self):
        pass

    @classmethod
    def run(cls, df_dropna, variableOne, variableTwo):
        try:
            setVariableOne = list(set(df_dropna[variableOne]))
            setvariableTwo = list(set(df_dropna[variableTwo]))

            myNewPandasDict = {}

            for i in setVariableOne:
                myNewPandasSubKeyDataDict = {}

                for j in range(len(df_dropna.index)):
                    if i == df_dropna.iloc[j][variableOne]:
                        myNewPandasSubKeyDataDict[df_dropna.iloc[j][variableTwo]] = df_dropna.iloc[j]["count"]

                myNewPandasDict[i] = myNewPandasSubKeyDataDict
            dataCountValueDataFrame = DataFrame(myNewPandasDict).fillna(0)

            floatNi = []  # 行的和
            floatNj = []  # 列的和
            chisq = 0

            for i in dataCountValueDataFrame.index:
                floatNi.append(dataCountValueDataFrame.ix[i].sum())
            for i in dataCountValueDataFrame.columns:
                floatNj.append(dataCountValueDataFrame[i].sum())

            sumTotal = sum(floatNi)

            Eij = []  # 理论频率， 二维数组

            for i in range(len(dataCountValueDataFrame.index)):

                for j in range(len(dataCountValueDataFrame.iloc[i])):
                    subValue = dataCountValueDataFrame.iloc[i].iloc[j]  # 原始值
                    subEij = floatNi[i] * floatNj[j] / sumTotal  # 理论频率
                    subChisqValue = ((subValue - subEij) * (subValue - subEij)) / float(subEij)

                    # print("=============")
                    # print(subValue)
                    # print(floatNi[i]) # 行的和
                    # print(floatNj[j])
                    # print(subEij)
                    # print(subChisqValue)
                    # print("############")

                    chisq += subChisqValue

            df = (len(floatNi) - 1) * (len(floatNj) - 1)
            P = chisqprob(chisq, df)

            # df 自由度
            # p 显著性
            # 值 pvalue
            # chisq 卡方
            ChiSquare2wayValue = {"chisq": chisq, "df": df, "N": sumTotal, "P": P}
        except Exception as e:
            ChiSquare2wayValue = {"chisq": "NAN", "df": "NAN", "P": "NAN", "N": "NAN"}

        return ChiSquare2wayValue
