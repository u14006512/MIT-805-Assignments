import matplotlib.pyplot as plt

PATH = './Results/2. Crimes per District.txt'

with open(PATH) as f:
    data = f.readlines()
data = [x.strip().split('\t') for x in data]
data = [(int(x[0]), int(x[1])) for x in data]
data.sort(key=lambda tup: tup[0]) 
countsPerDistrict = dict(data)

plt.bar(countsPerDistrict.keys(), countsPerDistrict.values(), color='g')