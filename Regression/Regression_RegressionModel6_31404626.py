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
series_df['month'] = series_df.index.month

for x in range(1,13):
    series_df["D"+str(x)] = [0] * len(series_df["Time"])
    series_df["D"+str(x)][series_df["month"]==x] = 1

D1 = series_df.D1
D2 = series_df.D2
D3 = series_df.D3
D4 = series_df.D4
D5 = series_df.D5
D6 = series_df.D6
D7 = series_df.D7
D8 = series_df.D8
D9 = series_df.D9
D10 = series_df.D10
D11 = series_df.D11
time = series_df.Time
ftse = series_df.ftse
eafv = series_df.eafv
k226 = series_df.k226
jq2j = series_df.jq2j
k54d = series_df.k54d

lm_1 = 'ftse ~ eafv + k226 + jq2j + k54d + D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + time' 
results_1 = ols(lm_1, data=series_df).fit()
print(results_1.summary())#AIC 3852

#Improving variables while taking the most not significant
lm_2 = 'ftse ~ eafv + k226 + jq2j + D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + time' 
results_2 = ols(lm_2, data=series_df).fit()
print(results_2.summary())#AIC 3851 and all the varaibles are significant
