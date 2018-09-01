from mrjob.job import MRJob
import csv

class MRArrestsPerYear(MRJob):
    def mapper(self, _, line):
        def str2bool(v):
            return v.lower() in ("yes", "true", "t", "1")
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        year = splitted[17]
        arrest = splitted[8]
        try:
            year = int(year)
            yield (arrest, year), 1
        except:
            pass
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRArrestsPerYear.run()