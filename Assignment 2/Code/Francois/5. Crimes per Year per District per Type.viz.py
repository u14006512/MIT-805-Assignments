import ast
PATH = './Results/5. Crimes per Year per District per Type.txt'

with open(PATH) as f:
    data = f.readlines()
    
data = [x.strip().split('\t') for x in data]
data = [(ast.literal_eval(x[0]), int(x[1])) for x in data]

data.sort(key=lambda tup: (tup[0][0], tup[0][1]))
print(data)

# visualisation is going to be a bit more involved here...