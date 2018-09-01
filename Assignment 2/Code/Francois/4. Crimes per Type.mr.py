from mrjob.job import MRJob
import csv

class MRCrimesPerType(MRJob):
    def mapper(self, _, line):
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        description = splitted[6] # == type

        try:
            if not description == 'Description':
                yield description, 1
        except:
            pass
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRCrimesPerType.run()