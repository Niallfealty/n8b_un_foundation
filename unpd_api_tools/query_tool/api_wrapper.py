""" Business logic of wrapper around API
"""
from requests import get

import json
import pandas as pd

CONFIG_PATH = "config.json"

with open(CONFIG_PATH, "r") as fp:
    config = json.load(fp)

# Loads the base url for calling the API
base_url = config["api_url"]

# Creates the target URL, indicators, in this instance
# maybe create a url formatter for these? depends on how many we're likely to need
target = base_url + "/indicators/"

def get_next_batch(target):
    ''' Grabs a batch of data
        
        @target is the url to use for this batch/page

        returns the url for the next page and a json_normalized dataframe of response
    '''
    response = get(target)
    j = response.json()
    return j['nextPage'], pd.json_normalize(j['data'])

def get_data_page_iterator(target):
    ''' Takes the url @target and returns an iterator which iterates
        over pages of data from this endpoint.

        @target is the url for the endpoint to download from

        returns a dataframe of the data from the response
    '''
    while target is not None:
        #call the API for the next page
        target, df = get_next_batch(target)
        yield df

def pull_paginated_data_to_df(target_url):
    ''' pull all paged data into a dataframe '''
    return pd.concat(get_data_page_iterator(target_url))

if __name__ == "__main__":
    print(pull_paginated_data_to_df(target))
