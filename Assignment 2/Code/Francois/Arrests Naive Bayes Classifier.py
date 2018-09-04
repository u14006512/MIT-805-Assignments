import ast
import linecache
import csv
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np
import itertools

# https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/
# http://users.sussex.ac.uk/~christ/crs/ml/lec02b.html
# https://towardsdatascience.com/introduction-to-naive-bayes-classification-4cffabb1ae54
# P(C|A1...An) ~ P(C) * P(Ai|C) * ... * P(An|C), Maximum A Posteriority Decision Rule

class Naive:
    PROBABILITIES_PATH = './Results/Arrests Likelihood Table.txt'
    def __init__(self):
        with open(self.PROBABILITIES_PATH) as f:
            data = f.readlines()
        output = dict() 
        data = [x.strip().split('\t') for x in data]   
        for x in data:
            output[x[0].strip('"')] = ast.literal_eval(x[1])
        self.probabilities = output 

    def getPAnC(self, attributeName, attributeValue):
        kv = self.probabilities[attributeName][attributeValue]
        return {
            True: kv[0] / float(kv[0] + kv[1]),
            False: kv[1] / float(kv[0] + kv[1])
        }

    def getArrestProbabilities(self):
        return {
            True: self.probabilities["Arrest"]["true"][2],
            False: self.probabilities["Arrest"]["false"][2]
        }
        
    def classify(self, instance):
        try:
            pArrestFalse = self.getArrestProbabilities()[False]
            pArrestTrue = self.getArrestProbabilities()[True]  
            
            domestic = str(instance["Domestic"]).lower()
            primaryType = instance["Primary Type"].upper()
            ward = str(instance["Ward"])
            locationDescription = instance["Location Description"].upper()
            #arrest = 
    
            pDomestic = self.getPAnC("Domestic", domestic)
            pPrimaryType = self.getPAnC("Primary Type", primaryType)
            pWard = self.getPAnC("Ward", ward)
            pLocationDescription = self.getPAnC("Location Description", locationDescription)
            
            proportionalProbabilityTrue =  pArrestTrue * pDomestic[True] * pPrimaryType[True] * pWard[True] * pLocationDescription[True]
            proportionalProbabilityFalse = pArrestFalse * pDomestic[False] * pPrimaryType[False] * pWard[False] * pLocationDescription[False]
            
            total = proportionalProbabilityTrue + proportionalProbabilityFalse
            proportionalProbabilityTrue = proportionalProbabilityTrue / total
            proportionalProbabilityFalse = proportionalProbabilityFalse / total
            
            # print((proportionalProbabilityTrue > proportionalProbabilityFalse, instance.setdefault("Arrest", None)))
            return {
                    "Actual" : instance.setdefault("Arrest", None),
                    "Prediction" : proportionalProbabilityTrue > proportionalProbabilityFalse,
                    "TrueProbability" : proportionalProbabilityTrue,
                    "FalseProbability": proportionalProbabilityFalse
            }
        except:
            print('Error reading line!')
            return None
     
class DataReader:
    # PATH = '/home/francois/Source/smaller.csv'
    PATH = '/home/francois/Source/Crimes_-_2001_to_present.csv'

    def __init__(self):
        self._totalLines = self.__lineCount()
        self._currentLine = 2
    def __str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")
    def __lineCount(self):
        f = open(self.PATH, 'rb')
        lines = 0
        buf_size = 1024 * 1024
        read_f = f.raw.read
        buf = read_f(buf_size)
        while buf:
            lines += buf.count(b'\n')
            buf = read_f(buf_size)
        return lines - 1
    def getMax(self):
        return self._totalLines
    
    def getNext(self, isTestSplit = True):
        if self._currentLine >= self._totalLines:
            return None

        line = linecache.getline(self.PATH, self._currentLine)
        self._currentLine = self._currentLine + 1
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        
        if isTestSplit and not int(splitted[0]) % 4 == 0: 
            return # This is a training line item.
        if not isTestSplit and int(splitted[0]) % 4 == 0: 
            return # This is a test line item.
        
        try:
            arrest = self.__str2bool(splitted[8])
            year = int(splitted[17])       
            primaryType = splitted[5]
            locationDescription = splitted[7]
            domestic = self.__str2bool(splitted[9])
            ward = int(splitted[12])
                                
            return {
                "Arrest": arrest,
                "Year": year,
                "Primary Type": primaryType,
                "Location Description": locationDescription,
                "Domestic": domestic,
                "Ward": ward
            }
        except:
            print('Error reading line!')
            return None

def plotConfusionMatrix(cm, classes):
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], '.2f'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Actual (True)')
    plt.xlabel('Predicted (Classification)')

if __name__ == '__main__':
    naive = Naive()
    dataReader = DataReader()
    
    actual = []
    predicted = []
    
    for i in range(dataReader.getMax()): 
        instance = dataReader.getNext()
        if not instance == None:
            print (i)
            result = naive.classify(instance)
            if result == None:
                continue
            predicted.append(result["Prediction"])
            actual.append(result["Actual"])
            # print(result["Actual"] == result["Prediction"])

    print(f'A total of {len(predicted)} instances were processed.')
    conf = metrics.confusion_matrix(actual, predicted)

    plotConfusionMatrix(conf, ["Arrested", "Not Arrested"])

    accuracy = metrics.accuracy_score(actual, predicted)
    precision = metrics.precision_score(actual, predicted)
    f1 = metrics.f1_score(actual, predicted)
    recall = metrics.recall_score(actual, predicted)
    roc_auc = metrics.roc_auc_score(actual, predicted)
    decimals = 3
    
    print(f"Achieved an accuracy of  {100 * accuracy:.{decimals}f}%.")
    print(f"Achieved a  precision of {precision:.{decimals}f}.")
    print(f"Achieved an f1-score of  {f1:.{decimals}f}.")
    print(f"Achieved a  recall of    {recall:.{decimals}f}.")
    print(f"Achieved an roc_auc of   {roc_auc:.{decimals}f}.")



