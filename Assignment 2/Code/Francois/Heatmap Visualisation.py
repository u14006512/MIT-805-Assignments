import folium
from folium.plugins import HeatMap
import linecache
import csv
from datetime import datetime

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")
        
LOCATION = '/home/francois/Source/smaller.csv'
LOCATION = '/home/francois/Source/Crimes_-_2001_to_present.csv'
lines = 6683206

rng = [x + 2 for x in range(lines-1)]
data = []
for i in rng:
    if (i % 10 != 0): continue
    if (i >= len(rng)): break
    line = linecache.getline(LOCATION, rng[i])
    reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
    splitted = next(reader)
    try:
        lat = float(splitted[19])
        lng = float(splitted[20])
        arrest = str2bool(splitted[8])
        domestic = str2bool(splitted[9])
        primaryType = splitted[5]
        year = int(splitted[17])
        locationDescription = splitted[7]
        ward = int(splitted[12])
        ts = datetime.strptime(splitted[2], '%m/%d/%Y %I:%M:%S %p')
        data.append((lat, lng, arrest, domestic, primaryType, year, locationDescription, ward, ts))
    except:
        pass

filteredData = [x for x in data if x[5] >= 2001 and x[5] < 2006]
filteredData = [x for x in data if x[5] >= 2006 and x[5] < 2012]
filteredData = [x for x in data if x[5] >= 2012 and x[5] < 2019]
filteredData = [x for x in data if x[4] == 'ASSAULT']
filteredData = [x for x in data if x[6] == 'GAS STATION']
filteredData = [x for x in data if x[2] == False]
filteredData = [x for x in data if x[2] == True]
filteredData = [x for x in data if x[7] == 28 and x[6] == 'GAS STATION'] 
filteredData = [x for x in data if x[7] == 28 and x[4] == 'BURGLARY' and x[5] > 2010] 

m = folium.Map([41.8281, -87.6298], zoom_start=12, tiles = "Stamen Terrain")
hm_wide = HeatMap([(x[0], x[1]) for x in filteredData], min_opacity=0.025, radius=10.5, blur=23, max_zoom=1)
m.add_child(hm_wide)
m.save("overallmap.html")








#filteredData =  data #[x for x in data if x[2] == False]
#filteredData.sort(key=lambda tup: (tup[8]))
#index = [x[8].strftime('%Y-%m-%d') for x in filteredData]
#hm = folium.plugins.HeatMapWithTime([(x[0], x[1]) for x in filteredData], index, auto_play=True)
#m = folium.Map([41.8281, -87.6298], zoom_start=10, tiles = "Stamen Terrain")
#m.add_child(hm)
#m.save("overallmap.html")




