import pandas as pd
import sys

def getPath():
    return "/home/francois/Source/Crimes_-_2001_to_present.csv"

def getData(nrows = 50):
    data = pd.read_csv(getPath(), nrows = nrows if nrows > 0 else sys.maxsize)

    data = pd.DataFrame(data[['ID', 
                  'Description', 
                  'Location Description',
                  'Arrest',
                  'Domestic',
                  'District',
                  'Ward',
                  'Beat',
                  'Year']])
    data.Year = data.Year.astype(int)
    return data