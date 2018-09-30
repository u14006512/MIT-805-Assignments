import matplotlib.pyplot as plt
import ast
import numpy as np
PATH = './Results/7. Arrests per Year.txt'

with open(PATH) as f:
    data = f.readlines()
    
data = [x.strip().split('\t') for x in data]
data = [(ast.literal_eval(x[0]), int(x[1])) for x in data]
yearlyPercentages = []
years = set([x[0][1] for x in data])
for year in years:
    yearData = [item for item in data if item[0][1] == year]
    yearData.sort(key=lambda tup: (tup[0][0]))
    notArrested = yearData[0][1]
    arrested = yearData[1][1]
    yearlyPercentages.append((year, 100 * arrested / (arrested + notArrested)))

yearlyPercentages.sort(key=lambda tup: (tup[0]))
yearlyPercentages = dict(yearlyPercentages)
yearlyPercentages = {k: v for k, v in yearlyPercentages.items() if k != 2018}
x = list(yearlyPercentages.keys())
y = list(yearlyPercentages.values())

plt.plot(x, y, '-o', color='k')
plt.ylim(15, 35)
plt.xlabel('Year')
plt.ylabel('Percentage of crimes with arrest (%)')
plt.axvline(x=2002, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2004, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2006, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2008, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2010, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2012, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2014, color='k', linestyle='--', linewidth=0.7)
plt.axvline(x=2016, color='k', linestyle='--', linewidth=0.7)
plt.title('Arrest rate per year (2001-2017)')
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.text(2011, 30, "y = %.2fx + %.2f"%(z[0], z[1]), color="r")
plt.show()
