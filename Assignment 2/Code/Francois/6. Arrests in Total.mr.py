from mrjob.job import MRJob
import csv

class MRArrestsInTotal(MRJob):
    def mapper(self, _, line):
        def str2bool(v):
            return v.lower() in ("yes", "true", "t", "1")
    
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        arrest = splitted[8]
        try:
            if not arrest == 'Arrest':
                yield str2bool(arrest), 1
        except:
            pass 
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRArrestsInTotal.run()