# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:

import csv
def csv_file(filename, csv_value):
    with open(filename, 'w') as per:
        writer = csv.writer(per)
        writer.writerow(['name', 'adderss', 'age'])
        writer.writerows(csv_value)
        
def main():
    person = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
    csv_file('person.csv', person)

if __name__ == "__main__":
    main()
