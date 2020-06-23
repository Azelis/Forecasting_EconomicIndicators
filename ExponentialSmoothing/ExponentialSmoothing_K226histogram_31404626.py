from pandas import read_excel
import matplotlib.pyplot as plt

k226_df_all = read_excel('K226data_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df = k226_df_all['2013-01-01':]

plt.figure(1)
plt.subplot(211)
plt.title('K226 and Distribution')
plt.plot(k226_df)
plt.subplot(212)
plt.hist(k226_df)
plt.show()