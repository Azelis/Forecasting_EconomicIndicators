from pandas import read_excel
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

########################## Data Preparation
jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

result = seasonal_decompose(jq2j_df)

jq2j_df.plot(label="JQ2J",color="blue", legend=True)
result.trend.plot(color="red", legend =True)
plt.title('JQ2J')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()
