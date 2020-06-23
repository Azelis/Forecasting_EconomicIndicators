from pandas import read_excel
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm  
from statsmodels.graphics.tsaplots import plot_acf

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
  
mod = sm.tsa.statespace.SARIMAX(k54d_df, order=(0,1,2), 
                                seasonal_order=(0,1,2,12))
results = mod.fit(disp=False)

fit1_arima = results.get_prediction(start=pd.to_datetime('2001-02-01'), dynamic=False)

Error_1 = k54d_df['2001-02-01':] - fit1_arima.predicted_mean

plot_acf(Error_1, title='ACF of K54D ARIMA model', lags=40)
plt.show()

Error_1.plot(color="black", title='Time plot of K54D ARIMA Residuals')
plt.show()


