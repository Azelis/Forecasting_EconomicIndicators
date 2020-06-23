from pandas import read_excel
import matplotlib.pyplot as plt

K226_df_adjusted = read_excel('K226data_31404626.xls', sheet_name='adjusted', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

K226_df_adjusted.plot(label="Calendar Adjusted EAFV", color="black", legend =True)
plt.title('EAFV Calendar Adjusted')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()