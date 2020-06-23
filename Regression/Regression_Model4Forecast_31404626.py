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
ftse_df = read_excel('FTSEdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

series_df = pd.concat([ftse_df, eafv_df, k226_df], axis=1,join='inner')
series_df.columns = ['ftse', 'eafv', 'k226']
series_df["Time"] = range(1,len(series_df)+1)

time = series_df.Time
ftse = series_df.ftse
eafv = series_df.eafv
k226 = series_df.k226

lm_4 = 'ftse ~ eafv + k226 + time'
results_4 = ols(lm_4, data=series_df).fit()



############################ Model
Final_result_4 = results_4
b0 = Final_result_4.params.Intercept
b1 = Final_result_4.params.eafv
b2 = Final_result_4.params.k226
b4 = Final_result_4.params.time

fit_1 = ExponentialSmoothing(eafv, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_1 = fit_1.forecast(12).rename("eafv forecast")

fit_2 = Holt(k226).fit(optimized=True)
fcast_2 = fit_2.forecast(12).rename("k226 forecast")

a1 = fit_1.fittedvalues
a2 = fit_2.fittedvalues

F=copy.deepcopy(a1)
for i in range(len(a1)):
    F[i] = b0 + a1[i]*b1 + a2[i]*b2 + time[i]*b4
    
v1=fcast_1
v2=fcast_2
v4=list(range((len(time)+1),(len(time)+13)))


E=copy.deepcopy(v1)
for i in range(len(v1)):
    E[i] = b0 + v1[i]*b1 + v2[i]*b2 + v4[i]*b4

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
