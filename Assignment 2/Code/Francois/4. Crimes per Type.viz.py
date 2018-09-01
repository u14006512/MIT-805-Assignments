import matplotlib.pyplot as plt
PATH = './Results/4. Crimes per Type.txt'

with open(PATH) as f:
    data = f.readlines()
data = [x.strip().split('\t') for x in data]
data = [(x[0], int(x[1])) for x in data]
data.sort(key=lambda tup: tup[1]) 
counts = dict(data)
print(counts)
plt.bar(counts.keys(), counts.values(), color='g')