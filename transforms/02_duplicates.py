import json
import sys

with open(sys.argv[1]) as infile:
    words = json.load(infile)

with open('data/duplicates.json') as infile:
    updates = json.load(infile)

def word_by_key(key):
    return [w for w in words if w['index'] == int(key)][0]

for key, val in updates.items():
    word = word_by_key(key)

    if val['meaning']:
        word['meaning'] = val['meaning']

for word in words:
    del word['duplicate']

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
