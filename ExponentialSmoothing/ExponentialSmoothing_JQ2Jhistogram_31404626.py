from pandas import read_excel
import matplotlib.pyplot as plt

jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

plt.figure(1)
plt.subplot(211)
plt.title('JQ2J and Distribution')
plt.plot(jq2j_df)
plt.subplot(212)
plt.hist(jq2j_df)
plt.show()