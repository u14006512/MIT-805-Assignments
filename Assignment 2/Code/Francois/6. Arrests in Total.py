import Shared as shared
import matplotlib.pyplot as plt

data = shared.getData(25000)
counts = data.groupby('Arrest').size().to_dict()

print(counts)
plt.bar(counts.keys(), counts.values(), color='g')