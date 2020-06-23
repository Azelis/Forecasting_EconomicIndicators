from pandas import read_excel
import pandas as pd
from statsmodels.formula.api import ols

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


series_df["Time"] = range(1,len(series_df)+1)

time = series_df.Time
ftse = series_df.ftse
eafv = series_df.eafv
k226 = series_df.k226
jq2j = series_df.jq2j
k54d = series_df.k54d

################Selecting best regression model
#Original linear model
lm_1 = 'ftse ~ eafv + k226 + jq2j + k54d' 
results_1 = ols(lm_1, data=series_df).fit()
print(results_1.summary())# AIC 3883

#Taking out the most not significant - eafv
lm_2 = 'ftse ~  k226 + jq2j + k54d' 
results_2 = ols(lm_2, data=series_df).fit()
print(results_2.summary())# AIC 3881

#Model improved by AIC, taking out the most not significant - k226
lm_3 = 'ftse ~ jq2j + k54d' 
results_3 = ols(lm_3, data=series_df).fit()
print(results_3.summary())# AIC 3880, e-squared 0.415, to low

#Trying with time variable to improve AIC and have reasonable r-square
lm_4 = 'ftse ~ k54d + eafv + k226 + jq2j + time'
results_4 = ols(lm_4, data=series_df).fit()
print(results_4.summary())# AIC 3847

#Taking out the most not significant - k54d
lm_5 = 'ftse ~ eafv + k226 + jq2j + time'
results_5 = ols(lm_5, data=series_df).fit()
print(results_5.summary())# AIC 3845

#Taking out the most not significant - jq2j
lm_6 = 'ftse ~ eafv + k226 + time'
results_6 = ols(lm_6, data=series_df).fit()
print(results_6.summary())# AIC 3844
