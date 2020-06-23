from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

fit_1 = ExponentialSmoothing(eafv_df, seasonal_periods=12, trend='add', seasonal='mul').fit()

fcast_1 = fit_1.forecast(12).rename("Holt-Winter's model")
fit_fcast_1 = fit_1.fittedvalues.append(fcast_1).rename("HWM")
eafv_df.rename("Original Data").plot(color="blue", legend=True)
fit_fcast_1.plot(color='darkorange', legend=True)
plt.title('EAFV vs Exponential Smoothing')
plt.show()