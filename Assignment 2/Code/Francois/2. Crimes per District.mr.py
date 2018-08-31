from mrjob.job import MRJob
import csv

class MRCrimesPerDistrict(MRJob):
    def mapper(self, _, line):
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        district = splitted[11]
        try:
            yield int(district), 1
        except:
            pass
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRCrimesPerDistrict.run()