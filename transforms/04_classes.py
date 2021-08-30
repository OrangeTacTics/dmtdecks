import json
import sys

CLASSES = {}


def cls(fn):
    name = fn.__name__[3:].upper()
    CLASSES[name] = fn


@cls
def is_number(word):
    return word['simplified'] in '一ニ三四五六七八九十百千 万億兆'


@cls
def is_counter(word):
    return 'measure word' in word['meaning'] or '(mw ' in word['meaning']


@cls
def is_grammar(word):
    return word['simplified'] in [
        '的',
        '了',
    ]


@cls
def is_kangxiradical(word):
    return 'Kangxi radical' in word['meaning']


@cls
def is_question(word):
    return '?' in word['meaning']

@cls
def is_pronoun(word):
    return word['simplified'] in '我们你您他她它'


with open(sys.argv[1]) as infile:
    words = json.load(infile)

for word in words.values():
    classes = []
    for cls_name, cls_predicate in CLASSES.items():
        if cls_predicate(word):
            classes.append(cls_name)

    word['classes'] = sorted(classes)

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
