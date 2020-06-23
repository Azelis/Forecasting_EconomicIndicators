from pandas import read_excel
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

k226_df_all = read_excel('K226data_31404626.xls', shee_tname='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)

k226_df_ses = pd.DataFrame(k226_df_all["2013-01-01":])
k226_df_ses.reset_index(inplace=True)
k226_df_ses['year'] = [d.year for d in k226_df_ses.Date]
k226_df_ses['month'] = [d.strftime('%b') for d in k226_df_ses.Date]
years = k226_df_ses['year'].unique()

sns.cubehelix_palette(len(years))

mycolors=sns.cubehelix_palette(len(years))
for i, y in enumerate(years):
    if i >= 0:   
        plt.xlabel('Date')
        plt.title('K226 Seasonal Data')
        plt.plot('month', 'Yt', data=k226_df_ses.loc[k226_df_ses.year==y, :], color=mycolors[i], label=y)
        plt.text(k226_df_ses.loc[k226_df_ses.year==y, :].shape[0]-.9, 
                 k226_df_ses.loc[k226_df_ses.year==y, 'Yt'][-1:].values[0], 
                 y, fontsize=12, color=mycolors[i])
plt.show()
