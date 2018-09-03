
# coding: utf-8

# In[14]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')


# In[89]:


chicago = pd.read_csv('Crimes_-_2001_to_present.csv',error_bad_lines=False)


# In[90]:


chicago.head()


# In[91]:


print("Chicago dataset shape", chicago.shape)


# In[92]:


chicago.drop(['Case Number', 'IUCR', 'X Coordinate', 'Y Coordinate',
             'Updated On', 'FBI Code', 'Community Area'], inplace=True, axis=1)


# In[93]:


# dates to datetime format
chicago.Date = pd.to_datetime(chicago.Date, format='%m/%d/%Y %I:%M:%S %p')
# setting the index to be the date will help us a lot later on
chicago.index = pd.DatetimeIndex(chicago.Date)


# In[72]:


block_to_change = list(chicago['Block'].value_counts()[0:].index)
loc_to_change  = list(chicago['Location Description'].value_counts()[0:].index)
desc_to_change = list(chicago['Description'].value_counts()[0:].index)
type_to_change = list(chicago['Primary Type'].value_counts()[0:].index)


# In[73]:


chicago.loc[chicago['Block'].isin(block_to_change) , chicago.columns=='Block'] = 'OTHER'
chicago.loc[chicago['Location Description'].isin(loc_to_change) , chicago.columns=='Location Description'] = 'OTHER'
chicago.loc[chicago['Description'].isin(desc_to_change) , chicago.columns=='Description'] = 'OTHER'
chicago.loc[chicago['Primary Type'].isin(type_to_change) , chicago.columns=='Primary Type'] = 'OTHER'


# In[74]:


chicago['Block']                = pd.Categorical(chicago['Block'])
chicago['Location Description'] = pd.Categorical(chicago['Location Description'])
chicago['Description']          = pd.Categorical(chicago['Description'])
chicago['Primary Type']         = pd.Categorical(chicago['Primary Type'])


# In[96]:


chicago.info()


# In[101]:


plt.figure(figsize=(12,6))
chicago.resample('Y').size().plot(legend=False)
plt.title('Number of crimes per month')
plt.xlabel('Months')
plt.ylabel('Number of crimes')
plt.show()


# In[108]:


crimes_per_month = chicago.resample('M').size()
crimes_per_month.head(10)


# In[109]:


plt.figure(figsize=(12,6))
crimes_per_month.plot(legend=False)
plt.title('Number of crimes per month')
plt.xlabel('Months')
plt.ylabel('Number of crimes')
plt.show()


# In[78]:


plt.figure(figsize=(12,6))
chicago.resample('D').size().rolling(365).sum().plot()
plt.title('Rolling sum of all crimes')
plt.ylabel('Number of crimes')
plt.xlabel('Years')
plt.show()


# In[110]:


crimes_count_date = chicago.pivot_table('ID', aggfunc=np.size, columns='Primary Type', index=chicago.index.date, fill_value=0)
crimes_count_date.index = pd.DatetimeIndex(crimes_count_date.index)


# In[111]:


plo = crimes_count_date.rolling(365).sum().plot(figsize=(12, 30), subplots=True, layout=(-1, 3), sharex=False, sharey=False)


# In[87]:


Types = chicago.groupby([chicago['Primary Type']]).size().sort_values(ascending=True)
Types


# In[113]:


plt.figure(figsize=(8,10))
Types.plot(kind='barh')
plt.title('Number of crimes by type')
plt.ylabel('Crime Type')
plt.xlabel('Number of crimes')
plt.show()


# In[114]:


chicago.groupby([chicago['Location Description']]).size().sort_values(ascending=True)


# In[115]:


plt.figure(figsize=(8,10))
chicago.groupby([chicago['Location Description']]).size().sort_values(ascending=True).plot(kind='barh')
plt.title('Number of crimes by Location')
plt.ylabel('Crime Location')
plt.xlabel('Number of crimes')
plt.show()

