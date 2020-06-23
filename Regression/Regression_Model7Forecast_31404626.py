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

lm_7 = 'ftse_2 ~ eafv_2 + k226_2 + jq2j_2 + k54d_2' 
results_7 = ols(lm_7, data=series_df['2010-01-01':]).fit()

fit_1_10 = ExponentialSmoothing(eafv_2, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_1_10 = fit_1_10.forecast(12).rename("eafv forecast")

fit_2_10 = Holt(k226_2).fit(optimized=True)
fcast_2_10 = fit_2_10.forecast(12).rename("k226 forecast")

fit_3_10 = ExponentialSmoothing(jq2j_2, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_3_10 = fit_3_10.forecast(12).rename("jq2j forecast")

fit_4_10 =  ExponentialSmoothing(k54d_2, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_4_10 = fit_4_10.forecast(12).rename("k54d forecast")


############################ Model
Final_result_7 = results_7
b0_10 = Final_result_7.params.Intercept
b1_10 = Final_result_7.params.eafv_2
b2_10 = Final_result_7.params.k226_2
b3_10 = Final_result_7.params.jq2j_2
b4_10 = Final_result_7.params.k54d_2

a1_10 = fit_1_10.fittedvalues
a2_10 = fit_2_10.fittedvalues
a3_10 = fit_3_10.fittedvalues
a4_10 = fit_4_10.fittedvalues

F_10=copy.deepcopy(a1_10)
for i in range(len(a1_10)):
    F_10[i] = b0_10 + a1_10[i]*b1_10 + a2_10[i]*b2_10 + a3_10[i]*b3_10 + a4_10[i]*b4_10

v1_10=fcast_1_10
v2_10=fcast_2_10
v3_10=fcast_3_10
v4_10=fcast_4_10

E_10=copy.deepcopy(v1_10)
for i in range(len(v1_10)):
    E_10[i] = b0_10 + v1_10[i]*b1_10 + v2_10[i]*b2_10 + v3_10[i]*b3_10 + v4_10[i]*b4_10

K_10=F_10.append(E_10)
############################


Error_10 = ftse_2 - F_10

MSE_10=sum(Error_10**2)*1.0/len(F_10)
LowerE_10 = E_10 - 1.646*sqrt(MSE_10)
UpperE_10 = E_10 + 1.646*sqrt(MSE_10)

LowerE_10.plot(color="blue", label="Lower bound", legend =True)
UpperE_10.plot(color="green", label="Upper bound", legend =True)
ftse_2.plot(color='black', label='Actual',legend=True)
K_10.plot(color='red', label='Regression Forecast 2010',legend=True)
plt.title('Model 7. Regression forecast FTSE 2010')
plt.show()

