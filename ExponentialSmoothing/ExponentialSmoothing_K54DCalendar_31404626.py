from pandas import read_excel
import matplotlib.pyplot as plt

k54d_df_adjusted = read_excel('K54Ddata_31404626.xls', sheet_name='adjusted', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 
k54d_df_adjusted.plot(label="Calendar Adjusted K54D", color="black", legend =True)
plt.title('K54D Calendar Adjusted')
plt.xlabel('Date')
plt.ylabel('Monthly average of private sector weekly pay')
plt.show()
