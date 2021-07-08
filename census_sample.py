'''
Sample commands
'''
# Create census object
census = census_api.Census('!!!use Census API key here!!!')

# Create dictionary
dict_acs5 = census.get_dict(source = 'acs5', year = '2019')

# Creates acs datasets
acs2019 = census.get_data(
    source = 'acs5',
    year = '2019',
    variables = ['B03001_003E', 'NAME'],
    geographical_level = 'county',
)

# Create dataframe
df_acs2019 = pd.DataFrame(acs2019[1:], columns=acs2019[0])
df_acs2019['FIPS'] = df_acs2019['state'] + df_acs2019['county']
