import csv
from pprint import pprint


def read_csv():
    print("Read all the data from csv file into a dictionary")
    print("A dictionary is a hash table")
    with open("laureates.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        print(f"Field names are {reader.fieldnames}")
        laureates = list(reader)

    print(len(laureates))

    for laureate in laureates:
        if laureate["surname"] == "Einstein":
            pprint(laureate)


if __name__ == '__main__':
    read_csv()
