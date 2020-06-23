from pandas import read_excel
import matplotlib.pyplot as plt

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 
plt.figure(1)
plt.subplot(211)
plt.title('K54D and Distribution')
plt.plot(k54d_df)
plt.subplot(212)
plt.hist(k54d_df)
plt.show()