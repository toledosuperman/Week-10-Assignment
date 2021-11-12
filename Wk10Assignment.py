import csv
import json
def make_json(csvFilePath, jsonFilePath):
    salesdata = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['NO']
            salesdata[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(salesdata, indent=4))
csvFilePath = r'SalesJan2009.csv'
jsonFilePath = r'transaction_data.json'
make_json(csvFilePath, jsonFilePath)
