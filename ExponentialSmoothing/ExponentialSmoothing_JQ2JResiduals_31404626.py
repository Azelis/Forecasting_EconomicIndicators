from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from numpy import log, exp
from statsmodels.graphics.tsaplots import plot_acf

jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

jq2j_log =  log(jq2j_df)

fit_3 = ExponentialSmoothing(jq2j_log, seasonal_periods=12, trend='add', seasonal='mul').fit()

Error_3 = jq2j_df - exp(fit_3.fittedvalues)

plt.title('Time plot of JQ2J Residuals')
Error_3.plot(label='JQ2J Residuals', legend=True, color="black")
plot_acf(Error_3, title='ACF of JQ2J Residuals', lags=50)
plt.show()