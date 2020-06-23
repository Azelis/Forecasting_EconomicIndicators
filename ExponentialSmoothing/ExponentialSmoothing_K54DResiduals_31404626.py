from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_acf

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 
fit_1 = ExponentialSmoothing(k54d_df, seasonal_periods=12, trend='add', seasonal='mul').fit()

Error_1 = k54d_df - fit_1.fittedvalues

plt.title('Time plot of K54D Residuals')
Error_1.plot(label='K54D Residuals', legend=True, color="black")
plot_acf(Error_1, title='ACF of K54D Residuals', lags=50)
plt.show()