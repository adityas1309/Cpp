# Question: Day 34: Convert CSV data to JSON format using Python's built-in modules.
import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

csv_to_json('input.csv', 'output.json')
