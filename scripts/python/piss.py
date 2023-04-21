import json
import csv

with open ("urination.json", "r") as f:
        data = json.load(f)
        anus = data["related_searches"]

with open ("urine.csv", "w") as f:
        fieldnames = anus[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for name in anus: 
                writer.writerow(name)

print('done monkey')
