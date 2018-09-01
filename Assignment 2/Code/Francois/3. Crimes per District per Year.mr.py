from mrjob.job import MRJob
import csv

class MRCrimesPerDistrictPerYear(MRJob):
    def mapper(self, _, line):
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        district = splitted[11]
        year = splitted[17]
        
        try:
            district = int(district)
            year = int(year)
            yield (district, year), 1
        except:
            pass
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRCrimesPerDistrictPerYear.run()