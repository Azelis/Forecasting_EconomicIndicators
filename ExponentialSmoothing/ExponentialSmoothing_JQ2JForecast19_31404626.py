from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from numpy import log, exp

jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

jq2j_log =  log(jq2j_df)

fit_1_train = ExponentialSmoothing(jq2j_log[0:-12], seasonal_periods=12, trend='add', seasonal='mul').fit()

jq2j_test = jq2j_df[-12:]

fcast_1_train = exp(fit_1_train.forecast(12))

plt.title('jq2j Forecast 2019 by split data')  
fcast_1_train.plot(label='Trained Forecast', legend=True, color="red")
jq2j_test.plot(label='Actual', legend=True, color="black")
plt.show()