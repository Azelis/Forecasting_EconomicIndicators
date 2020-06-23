from pandas import read_excel
import pandas as pd
from statsmodels.formula.api import ols
import copy

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
k226_df = read_excel('K226data_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
ftse_df = read_excel('FTSEdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

series_df = pd.concat([ftse_df, eafv_df, k226_df, jq2j_df, k54d_df], axis=1,join='inner')
series_df.columns = ['ftse', 'eafv', 'k226','jq2j', 'k54d']

series_df_2 = copy.deepcopy(series_df['2010-01-01':])
ftse_2 = series_df_2.ftse
eafv_2 = series_df_2.eafv
k226_2 = series_df_2.k226
jq2j_2 = series_df_2.jq2j
k54d_2 = series_df_2.k54d
series_df_2["Time"] = range(1,len(series_df_2)+1)
time_2 = series_df_2.Time

lm_1 = 'ftse_2 ~ eafv_2 + k226_2 + jq2j_2 + k54d_2 + time_2' 
results_1 = ols(lm_1, data=series_df['2010-01-01':]).fit()
print(results_1.summary()) # AIC 1734

lm_2 = 'ftse_2 ~ eafv_2 + k226_2 + k54d_2 + time_2' 
results_2 = ols(lm_2, data=series_df['2010-01-01':]).fit()
print(results_2.summary()) # AIC 1732

lm_3 = 'ftse_2 ~ eafv_2 + k226_2 + time_2' 
results_3 = ols(lm_3, data=series_df['2010-01-01':]).fit()
print(results_3.summary()) # AIC 1732

lm_4 = 'ftse_2 ~ k226_2 + time_2' 
results_4 = ols(lm_4, data=series_df['2010-01-01':]).fit()
print(results_4.summary()) # AIC 1730