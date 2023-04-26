""" Business logic of wrapper around API
"""
from requests import get

import json
import pandas as pd

CONFIG_PATH = "config.json"

config = json.load(CONFIG_PATH)

# Loads the base url for calling the API
base_url = config["api_url"]

# Creates the target URL, indicators, in this instance
# maybe create a url formatter for these? depends on how many we're likely to need
target = base_url + "/indicators/"

def get_next_batch(target):
    response = requests.get(target)
    j = response.json()
    return j['nextPage'], pd.json_normalize(j['data'])

def get_data_page_iterator(target):
    while target != None:
        #call the API for the next page
        target, df = get_next_batch(target)
        yield df

def pull_paginated_data_to_df(target_url):
    ''' pull all paged data into a dataframe '''
    initial_response = get(target_url)
    return pd.concat(get_data_page_iterator(initial_response))

print(pull_paginated_data_to_df(target))

import sys
sys.exit()

# Get the response, which includes the first page of data as well as information on pagination and number of records
response = requests.get(target)

# Converts call into JSON
j = response.json()

# Converts JSON into a pandas DataFrame.
df = pd.json_normalize(j['data']) # pd.json_normalize flattens the JSON to accomodate nested lists within the JSON structure

# Loop until there are new pages with data
while j['nextPage'] != None:
    # Reset the target to the next page
    target = j['nextPage']

    #call the API for the next page
    response = requests.get(target)

    # Convert response to JSON format
    j = response.json()

    # Store the next page in a data frame
    df_temp = pd.json_normalize(j['data'])

    # Append next page to the data frame
    df = df.append(df_temp)
