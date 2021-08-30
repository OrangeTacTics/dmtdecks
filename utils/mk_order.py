import os.path
import json
import sys


filename = 'output/words.json'
with open(filename) as infile:
    words = json.load(infile)

num_words = len(words)


def key(word):
    id = word['index']
    class_sorter = '-'.join(sorted(word['classes']))
    if not class_sorter:
        class_sorter = 'ZZZ'
    return (class_sorter, int(id))


assert not os.path.exists('data/order.json'), 'File data/order.json already exists.'

with open('data/order.json', 'w') as outfile:
    print('[', file=outfile)
    for i, word in enumerate(sorted(words, key=key)):
        id = word['index']
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
