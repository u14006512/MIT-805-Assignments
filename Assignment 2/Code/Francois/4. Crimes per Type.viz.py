import matplotlib.pyplot as plt
PATH = './Results/4. Crimes per Type.txt'

with open(PATH) as f:
    data = f.readlines()
data = [x.strip().split('\t') for x in data]
data = [(x[0], int(x[1])) for x in data]
data.sort(key=lambda tup: tup[1]) 
counts = dict(data)
counts = [(key.replace('"', ''), value) for key, value in counts.items()]
counts.sort(key=lambda tup: (tup[1]))
total = sum([x[1] for x in counts])
counts = [(x[0], 100 * x[1] / total) for x in counts]

counts = counts[-10:]
x = [x[0] for x in counts]
y = [x[1] for x in counts]

plt.barh(x, y, color='#777777')
plt.xlabel('Percentage of all crimes')
plt.axvline(x=2.5, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=5.0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=7.5, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=10.0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=12.5, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=15, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=17.5, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=20, color='k', linestyle='--', linewidth=0.5)
#plt.title('Crime types as a percentage of all crimes (2001-2018)')
plt.show()
