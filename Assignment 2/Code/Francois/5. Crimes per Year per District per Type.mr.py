from mrjob.job import MRJob
import csv

class MRCrimesPerYearPerDistrictPerType(MRJob):
    def mapper(self, _, line):
        reader = csv.reader(line.splitlines(), quotechar='"', delimiter=',')
        splitted = next(reader)
        district = splitted[11]
        year = splitted[17]
        description = splitted[6] # == type
        try:
            district = int(district)
            year = int(year)
            yield (year, district, description), 1
        except:
            pass
        
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRCrimesPerYearPerDistrictPerType.run()