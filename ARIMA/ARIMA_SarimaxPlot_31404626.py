from pandas import read_excel
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

########################## Data Preparation
k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
          
mod = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,2), 
                                seasonal_order=(0,1,2,12))
results = mod.fit(disp=False)

fit1_arima = results.get_prediction(start=pd.to_datetime('2001-02-01'), dynamic=False)


fcast1_arima = results.get_forecast(steps=12)

pred1_ci = fit1_arima.conf_int()
pred2_ci = fcast1_arima.conf_int()

fit_fcast_arima = fit1_arima.predicted_mean.append(fcast1_arima.predicted_mean)
all_conf = pred1_ci.append(pred2_ci)

ax = k54d_df['2001-02-01':].plot(label='Actual')
fit_fcast_arima.plot(ax=ax, label='ARIMA Forecast', title='K54D ARIMA', alpha=.7)

ax.fill_between(all_conf.index,
                all_conf.iloc[:, 0],
                all_conf.iloc[:, 1], color='k', alpha=.2)
plt.legend()
plt.show()
