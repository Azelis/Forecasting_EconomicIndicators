from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(k54d_df)

k54d_df.plot(label="K54D",color="blue", legend=True)
result.trend.plot(color="red", legend =True)
plt.title('K54D')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()

 