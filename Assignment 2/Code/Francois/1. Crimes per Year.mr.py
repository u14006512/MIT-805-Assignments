from mrjob.job import MRJob
import csv

class MRCrimesPerYear(MRJob):
    def mapper(self, _, line):
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        year = splitted[17]
        try:
            yield int(year), 1
        except:
            pass 
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRCrimesPerYear.run()