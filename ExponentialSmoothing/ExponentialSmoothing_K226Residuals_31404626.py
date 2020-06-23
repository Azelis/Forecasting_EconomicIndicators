from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.api import Holt

k226_df_all = read_excel('K226data_31404626.xls', shee_tname='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df = k226_df_all['2013-01-01':]

fit_1 = Holt(k226_df).fit(optimized=True)

Error_1 = k226_df - fit_1.fittedvalues

plot_acf(Error_1, title='ACF of K226 Residuals', lags=40)
plt.show()
