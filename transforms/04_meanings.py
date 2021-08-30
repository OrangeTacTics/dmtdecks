import json
import sys

with open(sys.argv[1]) as infile:
    words = json.load(infile)

updates = []
for i in range(1, 6+1):
    with open(f'data/meanings.hsk{i}.json') as infile:
        updates.extend(json.load(infile))


def update_by_key(key):
    matches = [w for w in updates if w['index'] == int(key)]
    if matches:
        assert len(matches) == 1
        return matches[0]
    else:
        return None


def word_by_key(key):
    return [w for w in words if w['index'] == int(key)][0]


for word in words:
    key = word['index']
    update = update_by_key(key)
    if update:
        word['meaning'] = update['meaning']

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
