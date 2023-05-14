""" Some tools for computing cumulative stats on data
"""

def find_births_threshold(df,
        births_col="BirthsSingle",
        time_col="Time",
        scenario_col="Variant",
        max_time=200):
    ''' Function to get out the births threshold (in this case to find
        the year in which the last of the next 8Bn are born)
    '''
    df\
        .sort_values([scenario_col, time_col], ascending=True)
        .groupby(scenario_col)\
        .cumsum()
        #.rolling(max_time, center=False, on=time_col)

cumulative_births = un_all_future.sort_values(["Variant","Time"], ascending=True).set_index(["Variant","Time"]).groupby("Variant").BirthsSingle.cumsum().reset_index()

''' plotting
sns.lineplot(df_cum_b, x="Time", y="BirthsSingle", hue="Variant");plt.xlabel("Year"); plt.ylabel("Births");plt.title("Cumulative births from 2023");plt.hlines(y=8_000_000_000,xmin=2022,xmax=2100,color="r",linestyle="dashdot");plt.show()
'''
