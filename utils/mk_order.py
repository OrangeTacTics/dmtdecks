import json
import sys


filename = 'output/words.json'
with open(filename) as infile:
    words = json.load(infile)

num_words = len(words.keys())

def key(pair):
    id, word = pair
    return (word['classes'], int(id))


print('[')
for i, (id, word) in enumerate(sorted(words.items(), key=key)):
    simplified = word['simplified']
    while len(simplified) < 5:
        simplified += '　'

    meaning = word['meaning'][:50]
    classes = ' '.join(word['classes'])
    val = json.dumps(f"{simplified} {meaning} {classes}", ensure_ascii=False)

    key = json.dumps(id).rjust(7)

    is_last = i + 1 == num_words
    if not is_last:
        print(f'    [{key}, {val}],')
    else:
        print(f'    [{key}, {val}]')
print(']')
