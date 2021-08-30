import json
import sys


with open('output/words.json') as infile:
    words = json.load(infile)


with open('data/order.json') as infile:
    old_order = [id for [id, meaning] in json.load(infile)]

num_words = len(words.keys())


def key(pair):
    id, word = pair
    return old_order.index(id)

with open('data/order.json', 'w') as outfile:
    print('[', file=outfile)
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
            print(f'    [{key}, {val}],', file=outfile)
        else:
            print(f'    [{key}, {val}]', file=outfile)
    print(']', file=outfile)

