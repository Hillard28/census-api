'''
Early work in progress. To access the Census data dictionary, visit:
https://api.census.gov/data.html
'''
# For loading data if you want to skip all the previous inputs
import numpy as np
import pandas as pd
import requests

class Census(object):
    
    # Set root URL for making queries
    root_url = 'https://api.census.gov/data/'
    
    # Create census object and assign API key
    def __init__(self, key=None):
        self.key = None
        if key is not None:
            self.key = str(key)
        if self.key is None:
            print('You will be limited to 500 queries per IP address')
        elif len(self.key) < 32:
            print('You may not have entered a valid API key')
    
    # Pulls all variable names from survey with descriptions
    def get_dict(self, survey = 'acs1', year = 2019):
        # Set directory based on ACS survey selected
        if survey == 'acs1':
            src = year + '/acs/acs1'
        elif survey == 'acs5':
            src = year + '/acs/acs5'
        
        # Construct query URL
        url = self.root_url + src + '/profile/variables.json'
        
        # Pull data and convert to dataframe
        request = requests.get(url).json()
        
        data = pd.DataFrame(request['variables'])
        
        return data
    
    # American Community Survey data
    def get_acs(self, acs = 'acs1', year = 2019, variables = '', geographical_level = '', geographies = '', all = True):
        # Set directory based on year and ACS survey selected
        if acs == 'acs5':
            src = year + '/acs/acs5?'
        else:
            src = year + '/acs/acs1?'
        # If variables input as list, break into comma-delimited string
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        # Enter geographic scope and target subset
        if all == False:
            geo = 'for=' + geographical_level + ':' + geographies
        else:
            geo = 'for=' + geographical_level + ':*'
        # Construct URL for query
        if self.key is not None:
            url = self.root_url + src + var + '&' + geo + '&key=' + self.key
        else:
            url = self.root_url + src + var + '&' + geo
        
        # Send request and convert data to dataframe format
        request = requests.get(url).json()
        
        data = pd.DataFrame(request[1:], columns = request[0])
        
        return data
    
    # Decennial Census data
    def get_dec(self, dec = 'sf1', year = 2010, variables = '', geographical_level = '', geographies = '', all = True):
        # Set directory based on year and Decennial Census Survey selected
        src = year + '/dec/' + dec + '?'
        # If variables input as list, break into comma-delimited string
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        # Enter geographic scope and target subset
        if all == False:
            geo = 'for=' + geographical_level + ':' + geographies
        else:
            geo = 'for=' + geographical_level + ':*'
        # Construct URL for query
        if self.key is not None:
            url = self.root_url + src + var + '&' + geo + '&key=' + self.key
        else:
            url = self.root_url + src + var + '&' + geo
        
        # Send request and convert data to dataframe format
        request = requests.get(url).json()
        
        data = pd.DataFrame(request[1:], columns = request[0])
        
        return data
    
    # County Business Profile survey data
    def get_cbp(self, year = 2010, variables = '', geographical_level = '', geographies = '', all = True):
        # Set directory based on year of survey
        src = year + '/cbp?'
        # If variables input as list, break into comma-delimited string
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        # Enter geographic scope and target subset
        if all == False:
            geo = 'for=' + geographical_level + ':' + geographies
        else:
            geo = 'for=' + geographical_level + ':*'
        # Construct URL for query
        if self.key is not None:
            url = self.root_url + src + var + '&' + geo + '&key=' + self.key
        else:
            url = self.root_url + src + var + '&' + geo
        
        # Send request and convert data to dataframe format
        request = requests.get(url).json()
        
        data = pd.DataFrame(request[1:], columns = request[0])
        
        return data

