from pandas import read_excel
import matplotlib.pyplot as plt

eafv_df = read_excel('EAFVdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

plt.figure(1)
plt.subplot(211)
plt.title('eafv and Distribution')
plt.plot(eafv_df)
plt.subplot(212)
plt.hist(eafv_df)
plt.show()