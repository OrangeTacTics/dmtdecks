import csv
import typing as t
from dataclasses import dataclass
import json


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
    meaning: str


with open('hsk.txt') as infile:
    for line in infile:
        if line.startswith('#'):
            continue

        line = line.replace('\ufeff', '').strip()
        simple, trad, pinyin, pinyin2, meaning = line.split('\t')

        if len(pretty_syllables(pinyin, pinyin2)) == len(simple):
            words.append(Word(
                simple=simple,
                trad=trad,
                pinyin=pretty_syllables(pinyin, pinyin2),
                meaning=meaning,
            ))

        else:
            meanings = meaning.split('|')
            pinyins = pinyin.split(',')
            pinyins2 = pinyin2.split(',')
            assert len(pinyins) == len(meanings)
            for pinyin, pinyin2, meaning in zip(pinyins, pinyins2, meanings):
                words.append(Word(
                    simple=simple,
                    trad=trad,
                    pinyin=pretty_syllables(pinyin, pinyin2),
                    meaning=meaning,
                ))

with open('out.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['display'])

    for word in words:
        for char, syl in zip(word.simple, word.pinyin):
            writer.writerow({'display': f'<ruby>{char}<rt>{syl}</rt></ruby>'})
