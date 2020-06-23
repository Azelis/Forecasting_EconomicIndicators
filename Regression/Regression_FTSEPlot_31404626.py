from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

ftse_df = read_excel('FTSEdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(ftse_df)
ftse_df.plot(color="blue", label = "FTSE", legend=True)
result.trend.plot(color="red", legend =True)
plt.title('FTSE')
plt.xlabel('Date')
plt.ylabel('UK Footsie 100 share index')
plt.show()
