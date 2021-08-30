import json
import sys


classname = sys.argv[1]
try:
    filename = sys.argv[2]
except:
    filename = 'output/words.json'


with open(filename) as infile:
    words = json.load(infile)

new_words = {}

for key, word in words.items():
    if classname in word['classes']:
        new_words[key] = word

print(json.dumps(new_words, indent=4, ensure_ascii=False))
