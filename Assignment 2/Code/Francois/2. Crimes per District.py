import Shared as shared
import matplotlib.pyplot as plt

data = shared.getData(25000)
countsPerDistrict = data.groupby('District').size().to_dict()
# INDEX 11
print(countsPerDistrict)
plt.bar(countsPerDistrict.keys(), countsPerDistrict.values(), color='g')