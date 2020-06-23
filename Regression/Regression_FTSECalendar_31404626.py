from pandas import read_excel
import matplotlib.pyplot as plt


ftse_df_adjusted = read_excel('FTSEdata_31404626.xls', sheet_name='adjusted', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

ftse_df_adjusted.plot(color="blue", label = "adjusted FTSE", legend =True)
plt.title('Adjusted FTSE')
plt.ylabel('UK Footsie 100 share index')
plt.xlabel('Date')
plt.show()
