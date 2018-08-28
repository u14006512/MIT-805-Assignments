import Shared as shared
import matplotlib.pyplot as plt

data = shared.getData(250000)
countsPerYear = data.groupby('Year').size().to_dict()

print(countsPerYear)
plt.bar(countsPerYear.keys(), countsPerYear.values(), color='g')