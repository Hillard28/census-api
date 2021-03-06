'''
Early work in progress. To access the Census data dictionary, visit:
https://api.census.gov/data.html
'''
# For loading data if you want to skip all the previous inputs
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
        url = self.root_url + src + '/variables.json'
        
        # Pull data and convert to dataframe
        request = requests.get(url).json()
        
        data = request['variables']
        
        return data
    
    # Request Census data
    def get_data(self, source = 'acs1', year = 2019, variables = '', geographical_level = '', geographies = '', all = True):
        # Set directory based on year and ACS survey selected
        if 'acs' in source:
            src = year + '/acs/' + source + '?'
        elif 'sf' in source:
            src = year + '/dec/' + source + '?'
        else:
            src = year + '/' + source + '?'
        # If variables input as list, break into comma-delimited string
        if type(variables) is list or type(variables) is tuple:
            var = 'get=' + ','.join(variables)
        else:
            var = 'get=' + variables
        # Calculate number of variables
        var_cnt = var.count(',') + 1
        # Replace spaces in geographic scope
        geographical_level = geographical_level.replace(' ', '%20')
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
        data = [
            [
                int(element) if element is not None
                and element.isdigit()
                and index < var_cnt
                else None if element is not None
                and '-' in element
                and element.replace('-','').isdigit()
                and index < var_cnt
                else element
                for index, element in enumerate(entry)
            ] for entry in request
        ]
        
        return data








