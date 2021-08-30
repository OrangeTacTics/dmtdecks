import json
import sys

with open(sys.argv[1]) as infile:
    words = json.load(infile)

with open('data/meanings.json') as infile:
    updates = json.load(infile)


def word_by_key(key):
    return [w for w in words if w['index'] == int(key)][0]

for word in words:
    key = word['index']
    if key in updates:
        word['meaning'] = updates[key]['meaning']

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
