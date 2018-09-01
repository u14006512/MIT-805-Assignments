import Shared as shared
import matplotlib.pyplot as plt

data = shared.getData(25000)
counts = data.groupby('District').size().to_dict()
# INDEX 11
print(counts)
plt.bar(counts.keys(), counts.values(), color='g')