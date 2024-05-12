import csv
from datetime import datetime
from pprint import pprint

csvFileName = "laureates.csv"
fileReadMode = "r"

with open(csvFileName, fileReadMode) as csvFile:
    reader = csv.DictReader(csvFile)
    print(f"Field Names: {reader.fieldnames}")
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == 'Einstein':
        birthDate = datetime.strptime(laureate["born"], "%Y-%m-%d")
        nobelPrizeDate = datetime.strptime(laureate["year"], "%Y")
        ageNobelPrize = nobelPrizeDate.year - birthDate.year
        print(f"{laureate['name']} {laureate['surname']}'s age when he received nobel prize is {ageNobelPrize}")