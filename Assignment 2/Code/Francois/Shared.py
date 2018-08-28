import pandas as pd
import sys

def getData(nrows = 50):
    PATH = "F:\Francois\Copy Over\Crimes_-_2001_to_present.csv" # Change yours.
    data = pd.read_csv(PATH, nrows = nrows if nrows > 0 else sys.maxsize)

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