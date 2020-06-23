from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from numpy import log, exp

jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

jq2j_log =  log(jq2j_df)

fit_3 = ExponentialSmoothing(jq2j_log, seasonal_periods=12, trend='add', seasonal='mul').fit()

fcast_3 = exp(fit_3.forecast(12).rename("Holt-Winter's model"))
fit_fcast_3 = exp(fit_3.fittedvalues).append(fcast_3).rename("HWM")
jq2j_df.rename("Original Data").plot(color="blue", legend=True)
fit_fcast_3.plot(color='darkorange', legend=True)
plt.title('JQ2J vs Exponential Smoothing')
plt.show()
