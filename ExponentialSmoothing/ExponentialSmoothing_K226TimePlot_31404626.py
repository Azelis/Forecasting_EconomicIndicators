from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

########################## Data Preparation
k226_df_all = read_excel('K226data_31404626.xls', shee_tname='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(k226_df_all)

k226_df_all.plot(label="K226",color="blue", legend=True)
result.trend.plot(color="red", legend =True)
plt.title('K226')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()
