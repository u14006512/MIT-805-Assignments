import Shared as shared
data = shared.getData(25000)
counts = data.groupby(['Arrest', 'Year']).size().to_dict()

print(counts)