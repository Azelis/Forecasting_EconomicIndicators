from pandas import read_excel
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm  
from statsmodels.tsa.api import ExponentialSmoothing

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

    
mod = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,2), 
                                seasonal_order=(0,1,2,12))
results = mod.fit(disp=False)
fit1_arima = results.get_prediction(start=pd.to_datetime('2001-02-01'), dynamic=False)
fcast1_arima = results.get_forecast(steps=12)
fit_fcast_arima = fit1_arima.predicted_mean.append(fcast1_arima.predicted_mean)

fit_1 = ExponentialSmoothing(k54d_df, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_1 = fit_1.forecast(12).rename("Holt-Winter's model")
fit_fcast_1 = fit_1.fittedvalues.append(fcast_1).rename("Holt-Winter's 1")

plt.title('Forecasting 2020 K54D')
fcast_1.plot(color='blue', label='HWM', legend=True)
fcast1_arima.predicted_mean.plot(color='red', label='ARIMA', legend=True)
plt.show()

plt.title('HWM vs ARIMA, K54D')
fit_fcast_1['2001-02-01':].plot(color='blue', label='HWM', legend=True)
fit_fcast_arima.plot(color='red', label='ARIMA', legend=True)
plt.show()
