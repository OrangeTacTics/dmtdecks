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

    def display(self) -> str:
        result = []
        for char, syl in zip(word.simple, word.pinyin):
            result.append(f'<ruby>{char}<rt>{syl}</rt></ruby>')
        return ''.join(result)


with open('hsk.txt') as infile:
    for line in infile:
        if '#' in line:
            idx = line.index('#')
            line = line[:idx]

        if not line.strip():
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
                pinyin = pinyin.strip()
                pinyin2 = pinyin2.strip()
                meaning = meaning.strip()
                words.append(Word(
                    simple=simple,
                    trad=trad,
                    pinyin=pretty_syllables(pinyin, pinyin2),
                    meaning=meaning,
                ))

with open('out.csv', 'w') as outfile:
    fieldnames = [
        'key',
        'display',
        'simplified',
        'traditional',
        'pinyin',
        'meaning',
        'tts_text',
        'tts_audio',
    ]

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    for i, word in enumerate(words):
        if i == 100:
            break
        writer.writerow({
            'key': f"{word.simple} [{' '.join(word.pinyin)}]",
            'display': word.display(),
            'simplified': word.simple,
            'traditional': word.trad,
            'pinyin': ' '.join(word.pinyin),
            'meaning': word.meaning,
            'tts_text': word.simple,
            'tts_audio': '',
        })
