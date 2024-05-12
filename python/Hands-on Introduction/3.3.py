import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

EINSTEIN_JSON = json.dumps(EINSTEIN)
print(EINSTEIN_JSON)
EINSTEIN_DICTIONARY = json.loads(EINSTEIN_JSON)
pprint(EINSTEIN_DICTIONARY)
if EINSTEIN_DICTIONARY["motivation"] == EINSTEIN["motivation"]:
    print("JSON module loads and dumps functions are working as expected")

with open("laureates.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    laureates = list(reader)

with open("laureates.json", "w") as json_file:
    json.dump(laureates, json_file, indent=2)
