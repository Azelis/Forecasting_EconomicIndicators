from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.api import Holt

k226_df_all = read_excel('K226data_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df = k226_df_all['2013-01-01':]

fit_1 = Holt(k226_df).fit(optimized=True)

fcast_1 = fit_1.forecast(12).rename("LES model")
fit_fcast_1 = fit_1.fittedvalues.append(fcast_1).rename("LES")
k226_df.rename("Original Data").plot(color="blue", legend=True)
fit_fcast_1.plot(color='darkorange', legend=True)
plt.title('K226 vs Exponential Smoothing')
plt.show()