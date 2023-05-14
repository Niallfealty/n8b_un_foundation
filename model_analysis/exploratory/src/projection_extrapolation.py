""" Some helper functions for extrapolating trends
"""

from pandas import DataFrame, concat
from statsmodels.tsa.ar_model import AutoReg

def df_extender(df, **cols_to_input):
    ''' Generate a dataframe that extends the input

        df: original dataframe
        cols_to_input: key/val of colnames, lists of data

        everything not in cols_to_input is copied from first val
    '''
    new_cols = [c for c in df.columns if c not in cols_to_input.keys()]
    base_df = DataFrame(cols_to_input,
            columns=df.columns)
    for col in new_cols:
        base_df[col] = df[col].iloc[0]

    return base_df

def extend_ar(grouped_df,
        lags,
        values_col="val",
        year_col="year_id",
        extrapolation_length=10):
    ''' Take a DF grouped by the scenario so we have a single timeseries
        and add an extra @n steps using an AR(lags) model
        don't rely on this for a long extrapolation with further analysis
    '''
    ts_len, df_cols = grouped_df.shape
    final_year_df = grouped_df[year_col].max()
    final_year_predict = final_year_df + extrapolation_length
    new_years = [year for year in range(final_year_df+1, final_year_predict+1)]

    ar_model = AutoReg(grouped_df[values_col].to_numpy(), lags=lags).fit()
    new_datapoints = ar_model.predict(ts_len, ts_len+extrapolation_length-1)
    new_fields = {values_col: new_datapoints, year_col: new_years}

    return concat([grouped_df, 
        df_extender(grouped_df, **new_fields)]
        )
