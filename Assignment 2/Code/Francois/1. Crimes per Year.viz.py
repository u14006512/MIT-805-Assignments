import matplotlib.pyplot as plt

PATH = './Results/1. Crimes per Year.txt'

with open(PATH) as f:
    data = f.readlines()
data = [x.strip().split('\t') for x in data]
data = [(int(x[0]), int(x[1])) for x in data]
data.sort(key=lambda tup: tup[0]) 
countsPerYear = dict(data)

plt.bar(countsPerYear.keys(), countsPerYear.values(), color='g')