from pandas import read_excel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

k54d_df = read_excel('K54Ddata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)
 

k54d_df_ses = pd.DataFrame(k54d_df)
k54d_df_ses.reset_index(inplace=True)
k54d_df_ses['year'] = [d.year for d in k54d_df_ses.Date]
k54d_df_ses['month'] = [d.strftime('%b') for d in k54d_df_ses.Date]
years = k54d_df_ses['year'].unique()

sns.cubehelix_palette(len(years))

mycolors=sns.cubehelix_palette(len(years))
for i, y in enumerate(years):
    if i > 0:   
        plt.xlabel('Date')
        plt.title('K54D Seasonal Data')
        plt.plot('month', 'Yt', data=k54d_df_ses.loc[k54d_df_ses.year==y, :], color=mycolors[i], label=y)
        plt.text(k54d_df_ses.loc[k54d_df_ses.year==y, :].shape[0]-.9, 
                 k54d_df_ses.loc[k54d_df_ses.year==y, 'Yt'][-1:].values[0], 
                 y, fontsize=12, color=mycolors[i])
plt.show()