import json
import sys

CLASSES = {}


def cls(fn):
    name = fn.__name__[3:].upper()
    CLASSES[name] = fn


def is_basic(word):
    return word['index'] < 200

@cls
def is_basicgrammar(word):
    meanings = []
    chars = ['的', '是', '不', '了', '有', '没']
    return (
        any(m in word['meaning'].lower() for m in meanings) or
        word['simplified'] in chars
    )

@cls
def is_body(word):
    meanings = ['head', 'feet', 'arms', 'nose', 'eye', 'mouth']
    return (
        any(m in word['meaning'].lower() for m in meanings) or
        word['meaning'] == 'hand' or
        word['meaning'] == 'hair' or
        word['meaning'] == 'leg'
    )


@cls
def is_time(word):
    if not is_basic(word):
        return False
    meanings = ['time', 'hour', 'minute', 'second']
    return (
        any(m in word['meaning'].lower() for m in meanings)
    )

@cls
def is_direction(word):
    meanings = ['north', 'south', 'west']
    return (
        any(m in word['meaning'].lower() for m in meanings) or
        word['meaning'] == 'East'
    )

@cls
def is_basicverb(word):
    if not is_basic(word):
        return False
    verbs = [
        'think', 'feel', 'go', 'come', 'speak', 'talk', 'call', 'drink', 'eat', 'sleep',
        'play', 'see', 'look', 'buy', 'sell',
    ]
    return any(v in word['meaning'].lower() for v in verbs)


@cls
def is_color(word):
    colors = ['white', 'black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'color']
    return (
        any(c == word['meaning'].lower() for c in colors) or
        'red; symbol of success' in word['meaning']
    )


@cls
def is_basicadjective(word):
    if not is_basic(word):
        return False
    adjs = ['big', 'small', 'long', 'short', 'happy', 'sad', 'tired', 'fast', 'slow']
    return any(a in word['meaning'].lower() for a in adjs)


@cls
def is_family(word):
    relatives = [
        'mother', 'father', 'sister', 'brother', 'uncle', 'daughter', 'mom; mum',
        'husband', 'wife',
    ]
    return (
        any(r in word['meaning'].lower() for r in relatives) or
        word['meaning'] == 'son' or
        'Dad' in word['meaning']
    )

@cls
def is_number(word):
    return word['simplified'] in '一ニ三四五六七八九十百千零万億兆'


@cls
def is_counter(word):
    return (
        'measure word' in word['meaning'] or
        'counter word' in word['meaning'] or
        '(mw ' in word['meaning']
    )


@cls
def is_kangxiradical(word):
    return 'Kangxi radical' in word['meaning']


@cls
def is_question(word):
    return (
        '?' in word['meaning'] or
        'a question' in word['meaning'] or
        'no question' in word['meaning']
    )


@cls
def is_pronoun(word):
    return word['simplified'] in '我们你您他她它'


with open(sys.argv[1]) as infile:
    words = json.load(infile)

for word in words:
    classes = []
    for cls_name, cls_predicate in CLASSES.items():
        if cls_predicate(word):
            classes.append(cls_name)

    word['classes'] = sorted(classes)

with open(sys.argv[2], 'w') as outfile:
    json.dump(words, outfile, indent=4, ensure_ascii=False)
