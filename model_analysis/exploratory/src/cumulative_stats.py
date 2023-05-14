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
