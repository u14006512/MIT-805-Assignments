import Shared as shared
data = shared.getData(25000)
counts = data.groupby(['Year', 'District', 'Description']).size().to_dict()
print(counts)