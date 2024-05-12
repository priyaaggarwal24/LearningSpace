import csv
import json

print("Read laureates csv, filter records where the name starts with character 'A' and write to json")
with open('laureates.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    laureates = list(reader)
    print(f"Total records: {len(laureates)}")

laureates_A = []
for laureate in laureates:
    if laureate["name"].startswith("A"):
        laureates_A.append(laureate)

print(f"Records with name starting with 'A': {len(laureates_A)}")

with open('laureates_a.json', 'w') as jsonFile:
    json.dump(laureates_A, jsonFile, indent=4)
