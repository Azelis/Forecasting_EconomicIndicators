from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 
fit_1 = ExponentialSmoothing(k54d_df, seasonal_periods=12, trend='add', seasonal='mul').fit()

fcast_1 = fit_1.forecast(12).rename("Holt-Winter's model")
fit_fcast_1 = fit_1.fittedvalues.append(fcast_1).rename("HWM")
k54d_df.rename("Original Data").plot(color="blue", legend=True)
fit_fcast_1.plot(color='darkorange', legend=True)
plt.title('K54D vs Exponential Smoothing')
plt.show()