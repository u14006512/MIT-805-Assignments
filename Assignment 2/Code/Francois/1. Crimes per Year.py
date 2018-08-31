import Shared as shared
import matplotlib.pyplot as plt

data = shared.getData(25000)
countsPerYear = data.groupby('Year').size().to_dict()

print(countsPerYear)
plt.bar(countsPerYear.keys(), countsPerYear.values(), color='g')