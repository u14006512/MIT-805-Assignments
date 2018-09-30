import matplotlib.pyplot as plt

PATH = './Results/1. Crimes per Year.txt'

with open(PATH) as f:
    data = f.readlines()
data = [x.strip().split('\t') for x in data]
data = [(int(x[0]), int(x[1])) for x in data]
data.sort(key=lambda tup: tup[0]) 
countsPerYear = dict(data)
countsPerYear = {k: v for k, v in countsPerYear.items() if k != 2018}

plt.plot(countsPerYear.keys(), countsPerYear.values(), '-o', color='k')
plt.ylim(200000, 500000)
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.axvline(x=2002, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2004, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2006, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2008, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2010, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2012, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2014, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2016, color='k', linestyle='--', linewidth=0.7)
plt.title('Number of Crimes per year (2001-2017)')
plt.show()