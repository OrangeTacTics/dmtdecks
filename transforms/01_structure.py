import typing as t
from dataclasses import dataclass
import json
import sys


def syllables(pinyin):
    parts = []
    current_part = []
    for i in range(len(pinyin)):
        ch = pinyin[i]
        current_part.append(ch)
        if ch.isnumeric():
            parts.append(''.join(current_part))
            current_part = []

    return parts


def pretty_syllables(pinyin, pinyin2):
    result = []
    parts = syllables(pinyin)

    for part in parts:
        length = len(part) - 1
        result.append(pinyin2[:length])
        pinyin2 = pinyin2[length:]
    return result


words = []

@dataclass
class Word:
    simple: str
    trad: str
    pinyin: t.List[str]
    pinyin2: t.List[str]
    meaning: str
    hsk: int
    duplicate: bool

    def display(self) -> str:
        result = []
        for char, syl in zip(word.simple, word.pinyin):
            result.append(f'<ruby>{char}<rt>{syl}</rt></ruby>')
        return ''.join(result)


current_hsk_level = 0

with open(sys.argv[1]) as infile:
    for line in infile:
        if line.startswith('#'):
            current_hsk_level += 1
            continue

        simple, trad, pinyins, pinyin2s, meaning = line.strip().split('\t')

        pinyins = [p.strip() for p in pinyins.split(',')]
        pinyin2s = [p.strip() for p in pinyin2s.split(',')]

        dupliate = len(pinyins) > 1

        for pinyin, pinyin2 in zip(pinyins, pinyin2s):
            words.append(Word(
                simple=simple,
                trad=trad,
                pinyin=pretty_syllables(pinyin, pinyin2),
                pinyin2=syllables(pinyin),
                meaning=meaning,
                hsk=current_hsk_level,
                duplicate=dupliate,
            ))


out_json = {}

for i, word in enumerate(words, start=1):
    out_json[i] = {
        'hsk': word.hsk,
        'duplicate': word.duplicate,
        'simplified': word.simple,
        'traditional': word.trad,
        'pinyin': ' '.join(word.pinyin),
        'pinyin2': ' '.join(word.pinyin2),
        'meaning': word.meaning,
    }
    if i == 2000:
        break

with open(sys.argv[2], 'w') as outfile:
    json.dump(out_json, outfile, indent=4, ensure_ascii=False)
