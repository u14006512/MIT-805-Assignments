import Shared as shared

data = shared.getData(5000)
print(list(data.columns.values)) # prints all the column names.
print(data.describe(include = 'all')) # prints a description of the dataframe