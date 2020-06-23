from pandas import read_excel
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

jq2j_df = read_excel('JQ2Jdata_31404626.xls', sheet_name='data', header=0, 
              index_col=0, squeeze=True, parse_dates=True)


jq2j_df_ses = pd.DataFrame(jq2j_df)
jq2j_df_ses.reset_index(inplace=True)
jq2j_df_ses['year'] = [d.year for d in jq2j_df_ses.Date]
jq2j_df_ses['month'] = [d.strftime('%b') for d in jq2j_df_ses.Date]
years = jq2j_df_ses['year'].unique()

sns.cubehelix_palette(len(years))

mycolors=sns.cubehelix_palette(len(years))
for i, y in enumerate(years):
    if i > 0:        
        plt.xlabel('Date')
        plt.title('JQ2J Seasonal Data')
        plt.plot('month', 'Yt', data=jq2j_df_ses.loc[jq2j_df_ses.year==y, :], color=mycolors[i], label=y)
        plt.text(jq2j_df_ses.loc[jq2j_df_ses.year==y, :].shape[0]-.9, 
                 jq2j_df_ses.loc[jq2j_df_ses.year==y, 'Yt'][-1:].values[0], 
                 y, fontsize=12, color=mycolors[i])
plt.show()