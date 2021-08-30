import json
import os.path

meanings = {}

with open('build/words.01.json') as infile:
    words = json.load(infile)

    for i in range(1, 6+1):
        meanings[i] = [w for w in words if w['hsk'] == i]

    for word in words:
        del word['hsk']
        del word['traditional']
        del word['zhuyin']

for i in range(1, 6+1):
    filename = f'data/meanings.hsk{i}.json'
    assert not os.path.exists(filename), f'{filename} already exists.'

    with open(filename, 'w') as outfile:
        json.dump(meanings[i], outfile, indent=4, ensure_ascii=False)
