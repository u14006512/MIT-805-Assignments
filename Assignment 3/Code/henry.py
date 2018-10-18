import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('seaborn')

#Importing the datasets 
chicago = pd.read_csv('Crimes_-_2001_to_present.csv',error_bad_lines=False)
crimeGeo = pd.read_csv('crimeGeo.csv',error_bad_lines=False)

#dropping some columns
chicago.drop(['Case Number', 'IUCR', 'X Coordinate', 'Y Coordinate',
             'Updated On', 'Year', 'FBI Code','Beat','Ward','Location', 'District','Community Area'], inplace=True, axis=1)

			 
# dates to datetime format
chicago.Date = pd.to_datetime(chicago.Date, format='%m/%d/%Y %I:%M:%S %p')

#index set to be the date
chicago.index = pd.DatetimeIndex(chicago.Date)


#top 10 crime locations
loc_to_change  = list(chicago['Location Description'].value_counts().head(10).index)

#if the location is not in top 10, we set it to ignored
chicago.loc[~chicago['Location Description'].isin(loc_to_change) , chicago.columns=='Location Description'] = 'IGNORED'

#setting the columns below to categorical values
chicago['Location Description'] = pd.Categorical(chicago['Location Description'])
chicago['Primary Type']         = pd.Categorical(chicago['Primary Type'])

#crime rates by type and location

#creating pivot_tables
hour_by_location = chicago.pivot_table(values='ID', index='Location Description', columns=chicago.index.hour, aggfunc=np.size).fillna(0)
hour_by_type     = chicago.pivot_table(values='ID', index='Primary Type', columns=chicago.index.hour, aggfunc=np.size).fillna(0)


from sklearn.cluster import AgglomerativeClustering as AC

#scaling the values
def scaling(dataset,axis=0):
    return (dataset - dataset.mean(axis=axis)) / dataset.std(axis=axis)

#plotting heatmaps
def plotting_heatmap(dataset, num=None, cmap='plasma'):
      
    if num is None:
        num = np.arange(dataset.shape[0])
    plt.imshow(dataset.iloc[num,:], cmap=cmap)
    plt.colorbar(fraction=0.03)
    plt.yticks(np.arange(dataset.shape[0]), dataset.index[num])
    plt.xticks(np.arange(dataset.shape[1]))
    plt.grid(False)
    plt.show()
 
#scal the records and plotting_heatmap
def final_plot(dataset, num = None):
   
    scaled_dataset = scale_dataset(dataset.T).T
    if num is None:
        num = AC(4).fit(scaled_dataset).labels_.argsort()
    range = np.min([np.max(scaled_dataset.as_matrnum()), np.abs(np.min(scaled_dataset.as_matrnum()))])
    scaled_dataset = np.clip(scaled_dataset, -1*range, range)
    plotting_heatmap(scaled_dataset, num=num)
    
#First Heatmap
plt.figure(figsize=(15,12))
plt.title('Differences between frequencies of crimes at different hours')
final_plot(hour_by_type)

#Second Heatmap
plt.figure(figsize=(15,7))
plt.title('Crime occurence in 24Hrs at the top 10 crime locations') 
final_plot(hour_by_location)



