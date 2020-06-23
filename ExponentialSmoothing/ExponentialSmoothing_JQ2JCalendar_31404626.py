from pandas import read_excel
import matplotlib.pyplot as plt

jq2j_df_adjusted = read_excel('JQ2Jdata_31404626.xls', sheet_name='adjusted', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

jq2j_df_adjusted.plot(label="Calendar Adjusted JQ2J", color="black", legend =True)
plt.title('JQ2J Calendar Adjusted')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()