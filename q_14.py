# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.

import csv

def csv_file():
    with open('person.csv', 'r') as per:
        reader = csv.DictReader(per)
        for value in reader:
            print(value)

csv_file()