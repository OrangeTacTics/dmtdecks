import json
import sys


with open(sys.argv[1]) as infile:
    words = json.load(infile)


order = []
with open('data/order.json') as infile:
    order = [int(id) for [id, _word] in json.load(infile)]


def key(word):
    id = word['index']
    try:
        return order.index(id)
    except:
        return len(order) + id

words.sort(key=key)


with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)

