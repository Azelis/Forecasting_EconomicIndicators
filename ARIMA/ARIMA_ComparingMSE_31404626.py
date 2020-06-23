from pandas import read_excel
import pandas as pd
import statsmodels.api as sm  
from statsmodels.tsa.api import ExponentialSmoothing

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
        
mod = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,2), 
                                seasonal_order=(0,1,2,12))
results = mod.fit(disp=False)
fit1_arima = results.get_prediction(start=pd.to_datetime('2001-02-01'), dynamic=False)
Error_1 = k54d_df['2001-02-01':] - fit1_arima.predicted_mean


fit_1 = ExponentialSmoothing(k54d_df, seasonal_periods=12, trend='add', seasonal='mul', damped=False).fit()
fcast_1 = fit_1.forecast(12).rename("Holt-Winter's model")
fit_fcast_1 = fit_1.fittedvalues.append(fcast_1).rename("Holt-Winter's 1")
Error_2 = k54d_df['2001-02-01':] - fit_1.fittedvalues['2001-02-01':]

MSE1 = sum(Error_1 ** 2)*1.0/len(fit1_arima.predicted_mean)
MSE2 = sum(Error_2 ** 2)*1.0/len(fit_1.fittedvalues['2001-02-01':])

print("MSE ARIMA ",MSE1, "MSE HWM: ", MSE2)
