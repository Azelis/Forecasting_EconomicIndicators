from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

########################## Data Preparation
eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(eafv_df)

eafv_df.plot(label="EAFV",color="blue", legend=True)
result.trend.plot(color="red", legend =True)
plt.title('eafv')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()
