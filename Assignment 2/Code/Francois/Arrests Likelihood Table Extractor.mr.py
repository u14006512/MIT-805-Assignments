from mrjob.job import MRJob
import csv

class MRArrestsPerYear(MRJob):
    def mapper(self, _, line):
        def str2bool(v):
            return v.lower() in ("yes", "true", "t", "1")
        
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        if not splitted[0] == 'ID':
            try:
                # TARGET
                arrest = str2bool(splitted[8])
                
                # FEATURES
                year = int(splitted[17])       
                primaryType = splitted[5]
                locationDescription = splitted[7]
                domestic = str2bool(splitted[9])
                ward = int(splitted[12])
                            
                yield 'Year', (year, arrest)
                yield 'Primary Type', (primaryType, arrest)
                yield 'Location Description', (locationDescription, arrest)
                yield 'Domestic', (domestic, arrest)
                yield 'Ward', (ward, arrest)
                yield 'Arrest', (str(arrest).lower(), arrest)
            except:
                pass
        
    def reducer(self, key, values):
        # (attributeValue, (YES, NO))
        numberOfItems = 0
        output = dict()
        for value in values:
            numberOfItems = numberOfItems + 1
            freq = output.setdefault(value[0], (0,0))
            trueAdd = 1 if value[1] else 0
            falseAdd = 1 if not value[1] else 0
            freq = (freq[0] + trueAdd, freq[1] + falseAdd)
            output[value[0]] = freq
        
        for ikey in output.keys():
            output[ikey] = (output[ikey][0], output[ikey][1], (output[ikey][0] + output[ikey][1]) / numberOfItems)
        
        yield key, output
           
if __name__ == '__main__':
    MRArrestsPerYear.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    