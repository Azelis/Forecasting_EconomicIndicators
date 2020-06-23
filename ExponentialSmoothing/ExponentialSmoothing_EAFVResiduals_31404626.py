from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_acf

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)


fit_1 = ExponentialSmoothing(eafv_df, seasonal_periods=12, trend='add', seasonal='mul').fit()

Error_1 = eafv_df - fit_1.fittedvalues

plt.title('Time plot of EAFV Residuals')
Error_1.plot(label='EAFV Residuals', legend=True, color="black")
plot_acf(Error_1, title='ACF of EAFV Residuals', lags=50)
plt.show()