import ast
import matplotlib.pyplot as plt

PROBABILITIES_PATH = './Results/Arrests Likelihood Table.txt'
with open(PROBABILITIES_PATH) as f:
    data = f.readlines()
output = dict() 
data = [x.strip().split('\t') for x in data]   
for x in data:
    output[x[0].strip('"')] = ast.literal_eval(x[1])
probabilities = output
probabilities = probabilities["Domestic"]
probabilities = [(v, k) for k, v in probabilities.items()]
probabilities.sort(key=lambda tup: (tup[0][2]), reverse=True)
probabilities = probabilities[:10]
probabilities = [(x[1], x[0][0] / (x[0][0] + x[0][1])) for x in probabilities]
probabilities.sort(key=lambda tup: (tup[1]))

x = ['Non-Domestic', 'Domestic'] #[x[0] for x in probabilities]
y = [x[1] * 100 for x in probabilities]
plt.barh(x, y, color='#777777')
plt.xlabel('Percentage arrests made (%)')
plt.axvline(x=15, color='k', linestyle='--', linewidth=0.5)
plt.axvline(x=25, color='k', linestyle='--', linewidth=0.5)
plt.show()





