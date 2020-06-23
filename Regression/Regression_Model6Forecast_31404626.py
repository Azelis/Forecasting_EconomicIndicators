from pandas import read_excel
import matplotlib.pyplot as plt
import pandas as pd
from numpy import sqrt
from statsmodels.formula.api import ols
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.api import Holt
import copy

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
k226_df = read_excel('K226data_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
ftse_df = read_excel('FTSEdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

series_df = pd.concat([ftse_df, eafv_df, k226_df, jq2j_df], axis=1,join='inner')
series_df.columns = ['ftse', 'eafv', 'k226','jq2j']
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


lm_6 = 'ftse ~ eafv + k226 + jq2j + D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + time' 
results_6 = ols(lm_6, data=series_df).fit()



############################ Model
Final_result_6 = results_6
b0 = Final_result_6.params.Intercept
b1 = Final_result_6.params.eafv
b2 = Final_result_6.params.k226
b3 = Final_result_6.params.jq2j
b4 = Final_result_6.params.D1
b5 = Final_result_6.params.D2
b6 = Final_result_6.params.D3
b7 = Final_result_6.params.D4
b8 = Final_result_6.params.D5
b9 = Final_result_6.params.D6
b10 = Final_result_6.params.D7
b11 = Final_result_6.params.D8
b12 = Final_result_6.params.D9
b13 = Final_result_6.params.D10
b14 = Final_result_6.params.D11
b15 = Final_result_6.params.time

fit_1 = ExponentialSmoothing(eafv, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_1 = fit_1.forecast(12).rename("eafv forecast")

fit_2 = Holt(k226).fit(optimized=True)
fcast_2 = fit_2.forecast(12).rename("k226 forecast")

fit_3 = ExponentialSmoothing(jq2j, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_3 = fit_3.forecast(12).rename("jq2j forecast")

a1 = fit_1.fittedvalues
a2 = fit_2.fittedvalues
a3 = fit_3.fittedvalues

F=copy.deepcopy(a1)
for i in range(len(a1)):
    F[i] = b0 + a1[i]*b1 + a2[i]*b2 + a3[i]*b3 + D1[i]*b4 + D2[i]*b5 + D3[i]*b6 + \
    D4[i]*b7 + D5[i]*b8 + D6[i]*b9 + D7[i]*b10 + D8[i]*b11 + D9[i]*b12 + \
    D10[i]*b13 + D11[i]*b14 + time[i]*b15
    
v1=fcast_1
v2=fcast_2
v3=fcast_3
v4=D1[0:12]
v5=D2[0:12]
v6=D3[0:12]
v7=D4[0:12]
v8=D5[0:12]
v9=D6[0:12]
v10=D7[0:12]
v11=D8[0:12]
v12=D9[0:12]
v13=D10[0:12]
v14=D11[0:12]
v15=list(range((len(time)+1),(len(time)+13)))

E=copy.deepcopy(v1)
for i in range(len(v1)):
    E[i] = b0 + v1[i]*b1 + v2[i]*b2 + v3[i]*b3 + v4[i]*b4 + v5[i]*b5 + v6[i]*b6 + \
    v7[i]*b7 + v8[i]*b8 + v9[i]*b9 + v10[i]*b10 + v11[i]*b11 + v12[i]*b12 + \
    v13[i]*b13 + v14[i]*b14 + v15[i]*b15

K=F.append(E)
############################



Error_1 = ftse - F

MSE=sum(Error_1**2)*1.0/len(F)
LowerE = E - 1.646*sqrt(MSE)
UpperE = E + 1.646*sqrt(MSE)

LowerE.plot(color="blue", label="Lower bound", legend =True)
UpperE.plot(color="green", label="Upper bound", legend =True)
ftse.plot(color='black', label='Actual', legend=True)
K.plot(color='red', label='Regression Forecast', legend=True)
plt.title('Model 4. Regression forecast FTSE with time')
plt.show()
