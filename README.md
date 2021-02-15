# census-api
Tool for accessing data from the Census Bureau's API.  Early work in progress.  As of now, queries output a list of lists as packaged by the Census Bureau (albeit I'm converting string type numbers to integers for the variables selected).  I figured this is a bit more user friendly for tasks like converting to a dataframe than if I formatted into a dict.

The get_dict() call returns a dictionary of variables within a given survey package.  Accelerates lookup of relevant variables, given there are often thousands and having to switch between the web and console is a pain.


You can make up to 500 queries from the API without a key.  To obtain a free key, visit:

https://www.census.gov/data/developers.html


To access the Census data dictionary, visit:

https://api.census.gov/data.html
