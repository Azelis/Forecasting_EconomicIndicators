from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

ftse_df = read_excel('FTSEdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(ftse_df['2010-01-01':])
ftse_df['2010-01-01':].plot(label= "FTSE", color="blue", legend=True)
result.trend.plot(color="red", legend =True)
plt.title('FTSE 2010')
plt.xlabel('Date')
plt.show()
