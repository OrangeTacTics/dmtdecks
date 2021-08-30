import json
import sys


def is_number(word):
    return word['simplified'] in '一ニ三四五六七八九十百千 万億兆'


def is_counter(word):
    return 'measure word' in word['meaning'] or '(mw ' in word['meaning']

def is_grammar(word):
    return word['simplified'] in [
        '的',
        '了',
    ]


def is_pronoun(word):
    return word['simplified'] in '我们你您他她它'


with open(sys.argv[1]) as infile:
    words = json.load(infile)

for word in words.values():
    classes = []
    if is_number(word):
        classes.append('NUMBER')

    if is_counter(word):
        classes.append('COUNTER')

    if is_grammar(word):
        classes.append('GRAMMAR')

    if is_pronoun(word):
        classes.append('PRONOUN')

    word['classes'] = classes

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
