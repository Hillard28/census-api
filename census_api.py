'''
Early work in progress. To access the Census data dictionary, visit:
https://api.census.gov/data.html
'''
import numpy as np
import pandas as pd
import requests

class Census(object):
    
    root_url = 'https://api.census.gov/data/'
    
    def __init__(self, key=None):
        self.key = None
        if key is not None:
            self.key = str(key)
        if self.key is None:
            print('You will be limited to 500 queries per IP address')
        elif len(self.key) < 32:
            print('You may not have entered a valid API key')
    
    def get_acs(self, acs = 'acs1', year = 2019, variables = '', geographical_level = '', geographies = '', all = True):
        if acs = 'acs5':
            src = year + '/acs/acs5?'
        else:
            src = year + '/acs/acs1?'
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        if all == False:
            geo = 'for=' + geographical_level + ':' + geographies
        else:
            geo = 'for=' + geographical_level + ':*'
        
        if self.key is not None:
            url = self.root_url + src + var + '&' + geo + '&key=' + self.key
        else:
            url = self.root_url + src + var + '&' + geo
        
        request = requests.get(url).json()
        
        data = pd.DataFrame(request[1:], columns = request[0])
        
        return data
    
    def get_dcs(self, dec = 'sf1', year = 2010, variables = '', geographical_level = '', geographies = '', all = True):
        
        src = year + '/dec/' + dec + '?'
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        if all == False:
            geo = 'for=' + geographical_level + ':' + geographies
        else:
            geo = 'for=' + geographical_level + ':*'
        
        if self.key is not None:
            url = self.root_url + src + var + '&' + geo + '&key=' + self.key
        else:
            url = self.root_url + src + var + '&' + geo
        
        request = requests.get(url).json()
        
        data = pd.DataFrame(request[1:], columns = request[0])
        
        return data
    
    def get_cbp(self, year = 2010, variables = '', geographical_level = '', geographies = '', all = True):
        
        src = year + '/cbp?'
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        if all == False:
            geo = 'for=' + geographical_level + ':' + geographies
        else:
            geo = 'for=' + geographical_level + ':*'
        
        if self.key is not None:
            url = self.root_url + src + var + '&' + geo + '&key=' + self.key
        else:
            url = self.root_url + src + var + '&' + geo
        
        request = requests.get(url).json()
        
        data = pd.DataFrame(request[1:], columns = request[0])
        
        return data
