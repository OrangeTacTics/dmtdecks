import json
import sys

with open(sys.argv[1]) as infile:
    words = json.load(infile)

with open('data/duplicates.json') as infile:
    updates = json.load(infile)

for key, val in updates.items():
    if val['meaning']:
        words[key]['meaning'] = val['meaning']
    else:
        del words[key]

for word in words.values():
    del word['duplicate']

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
