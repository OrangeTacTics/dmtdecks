import json
import sys

with open(sys.argv[1]) as infile:
    words = json.load(infile)

with open('data/duplicates.json') as infile:
    updates = json.load(infile)

for key, val in updates.items():
    if val['meaning']:
        words[key]['meaning'] = val
    else:
        del words[key]

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
