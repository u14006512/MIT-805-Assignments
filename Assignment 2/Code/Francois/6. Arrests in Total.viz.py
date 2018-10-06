import matplotlib.pyplot as plt
PATH = './Results/6. Arrests in Total.txt'

with open(PATH) as f:
    data = f.readlines()
data = [x.strip().split('\t') for x in data]
data = [(x[0], int(x[1])) for x in data]
data.sort(key=lambda tup: tup[1]) 
counts = dict(data)
counts['No Arrest'] = counts.pop('false')
counts['Arrest'] = counts.pop('true')

labels = 'No arrest', 'Arrest'
sizes = [counts['No Arrest'], counts['Arrest']]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
#plt.title('Arrests over the entire period (2001 - 2018)')
plt.show()