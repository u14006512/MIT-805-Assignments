import Shared as shared
data = shared.getData(25000)
counts = data.groupby(['Description']).size().to_dict() # Assumption that Type == Description
print(counts)