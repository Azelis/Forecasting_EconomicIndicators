from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

k226_df_all = read_excel('K226data_31404626.xls', shee_tname='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(k226_df_all)

k226_df = k226_df_all['2013-01-01':]

k226_df.plot(label="K226",color="blue", legend=True)
result.trend['2013-01-01':].plot(color="red", legend =True)
plt.title('K226 2013')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()