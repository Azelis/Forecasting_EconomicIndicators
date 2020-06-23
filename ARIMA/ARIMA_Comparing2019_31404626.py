from pandas import read_excel
import matplotlib.pyplot as plt
import statsmodels.api as sm  
from statsmodels.tsa.api import ExponentialSmoothing

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

fit_1_train = ExponentialSmoothing(k54d_df[0:-12], seasonal_periods=12, trend='add', seasonal='mul').fit()
k54d_test = k54d_df[-12:]
fcast_1_train = fit_1_train.forecast(12)

mod_train = sm.tsa.statespace.SARIMAX(k54d_df[0:-12], order=(0,1,2), 
                                seasonal_order=(0,1,2,12))
results_train = mod_train.fit(disp=False)
fcast1_arima_train = results_train.get_forecast(steps=12).predicted_mean

plt.title('Forecast 2019 K54D')
k54d_test.plot(color='black', label='Actual', legend=True)
fcast_1_train.plot(color='blue', label='HWM', legend=True)
fcast1_arima_train.plot(color='red', label='ARIMA', legend=True)
plt.show()
