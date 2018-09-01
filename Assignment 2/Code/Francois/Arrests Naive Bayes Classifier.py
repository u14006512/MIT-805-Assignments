import ast
PATH = './Results/Arrests Likelihood Table.txt'

# https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/
# http://users.sussex.ac.uk/~christ/crs/ml/lec02b.html
# https://towardsdatascience.com/introduction-to-naive-bayes-classification-4cffabb1ae54
# P(C|A1...An) ~ P(C) * P(Ai|C) * ... * P(An|C), Maximum A Posteriority Decision Rule

with open(PATH) as f:
    data = f.readlines()
output = dict() 
data = [x.strip().split('\t') for x in data]
for x in data:
    output[x[0].strip('"')] = ast.literal_eval(x[1])
    
def getPAnC(attributeName, attributeValue):
    kv = output[attributeName][attributeValue]
    return (kv[0] / float(kv[0] + kv[1]), kv[1] / float(kv[0] + kv[1]))
    
pArrestFalse = output["Arrest"]["false"][2]  # P(C), C = false, No Arrest
pArrestTrue = output["Arrest"]["true"][2]    # P(C), C = true, Arrested

domestic = getPAnC("Domestic", "false")
primaryType = getPAnC("Primary Type", "NARCOTICS") # 50772
ward = getPAnC("Ward", "28")
locationDescription = getPAnC("Location Description", "APARTMENT")

probTrue = pArrestTrue * domestic[0] * primaryType[0] * ward[0] * locationDescription[0]
probFalse = pArrestFalse * domestic[1] * primaryType[1] * ward[1] * locationDescription[1]

print(probTrue)
print(probFalse)