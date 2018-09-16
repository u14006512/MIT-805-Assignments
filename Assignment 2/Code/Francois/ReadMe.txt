This is Python code for MapReduce using the MRJob Python package.
All MapReduce Python scripts are suffixed by .mr.py. All visualization-specific scripts are suffixed by .viz.py. 

There are 2 main categories of jobs:
1. Feature extraction (summary, aggregation, counts, averages, etc., named 1-7), which includes a script to visualise each extractor's results using Matplotlib.
2. The Naive Bayes part. First, the likelihoods are extracted using [Arrests Likelihood Table Extractor.mr.py]. Then, the classifier is tested in [Arrests Naive Bayes Classifier.py].

In the [Results] folder are the results of the feature extractors and the NB likelihoods. These results can be used to visualise.

Below are examples of some of the simpler aggregations (called features), and how to run them from the command line. Change the filename to match your location. The first entry is on the 'smaller.csv' file, which is an extract of the much bigger file, which was used for development purposes:

== Feature 1 - Crimes per Year
python '1. Crimes per Year.mr.py' /home/francois/Source/smaller.csv > './Results/1. Crimes per Year.txt'
python '1. Crimes per Year.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/1. Crimes per Year.txt'

== Feature 2 - Crimes per District
python '2. Crimes per District.mr.py' /home/francois/Source/smaller.csv > './Results/2. Crimes per District.txt'
python '2. Crimes per District.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/2. Crimes per District.txt'

== Feature 3 - Crimes per District per Year
python '3. Crimes per District per Year.mr.py' /home/francois/Source/smaller.csv > './Results/3. Crimes per District per Year.txt'
python '3. Crimes per District per Year.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/3. Crimes per District per Year.txt'

== Feature 4 - Crimes per Type
python '4. Crimes per Type.mr.py' /home/francois/Source/smaller.csv > './Results/4. Crimes per Type.txt'
python '4. Crimes per Type.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/4. Crimes per Type.txt'

== Feature 5 - Crimes per Year per District per Type
python '5. Crimes per Year per District per Type.mr.py' /home/francois/Source/smaller.csv > './Results/5. Crimes per Year per District per Type.txt'
python '5. Crimes per Year per District per Type.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/5. Crimes per Year per District per Type.txt'

== Feature 6 - Arrests in Total
python '6. Arrests in Total.mr.py' /home/francois/Source/smaller.csv > './Results/6. Arrests in Total.txt'
python '6. Arrests in Total.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/6. Arrests in Total.txt'

== Feature 7 - Arrests per Year
python '7. Arrests per Year.mr.py' /home/francois/Source/smaller.csv > './Results/7. Arrests per Year.txt'
python '7. Arrests per Year.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/7. Arrests per Year.txt'

== Arrests Likelihood Table Extractor
python 'Arrests Likelihood Table Extractor.mr.py' /home/francois/Source/smaller.csv > './Results/Arrests Likelihood Table.txt'
python 'Arrests Likelihood Table Extractor.mr.py' /home/francois/Source/Crimes_-_2001_to_present.csv > './Results/Arrests Likelihood Table.txt'


