from pandas import read_excel
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.tsa.api import Holt
from statsmodels.graphics.tsaplots import plot_acf
import copy

ftse_df = read_excel('FTSEdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
k226_df = read_excel('K226data_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

series_df = pd.concat([ftse_df, k226_df], axis=1,join='inner')
series_df.columns = ['ftse', 'k226']

series_df_2 = copy.deepcopy(series_df['2010-01-01':])
ftse_2 = series_df_2.ftse
k226_2 = series_df_2.k226
series_df_2["Time"] = range(1,len(series_df_2)+1)
time_2 = series_df_2.Time

lm_9 = 'ftse_2 ~ k226_2 + time_2' 
results_9 = ols(lm_9, data=series_df['2010-01-01':]).fit()

fit_1_10 = Holt(k226_2).fit(optimized=True)
fcast_1_10 = fit_1_10.forecast(12).rename("k226 forecast")

Final_result_9 = results_9
b0_10 = Final_result_9.params.Intercept
b2_10 = Final_result_9.params.k226_2
b4_10 = Final_result_9.params.time_2

a2_10 = fit_1_10.fittedvalues

F_10=copy.deepcopy(a2_10)
for i in range(len(a2_10)):
    F_10[i] = b0_10 + a2_10[i]*b2_10 + time_2[i]*b4_10

Error_10_2 = ftse_2 - F_10


plt.title('Time plot of model 9. Regression Residuals 2010')
Error_10_2.plot(label='Regression Residuals', legend=True, color="black")
plt.show()

plot_acf(Error_10_2, title='ACF of model 9. Regression Residuals 2010', lags=40)
plt.show()