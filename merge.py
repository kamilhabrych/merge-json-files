import json
import glob


files = []

for file in glob.glob("*.json"):
    files.append(file)
def merge_JsonFiles(filename):
    result = list()
    for item in filename:
        with open(item, 'r') as infile:
            result.extend(json.load(infile))
    with open('merge.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles(files)