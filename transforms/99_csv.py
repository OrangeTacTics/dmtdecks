import dragonmapper.transcriptions

import sys
import json
import csv


with open(sys.argv[1]) as infile:
    words = json.load(infile)



def to_display(word):
    result = []
    for char, syl in zip(word['simplified'], word['pinyin'].split(' ')):
        result.append(f'<ruby>{char}<rt>{syl}</rt></ruby>')
    return ''.join(result)


with open(sys.argv[2], 'w') as outfile:
    fieldnames = [
        'id',
        'display',
        'simplified',
        'traditional',
        'pinyin',
        'zhuyin',
        'meaning',
        'tts_text',
        'tts_audio',
    ]

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)


    for i, word in enumerate(words.values()):
        if i == 100:
            break
        writer.writerow({
            'id': f"{word['simplified']} [{word['pinyin']}]",
            'display': to_display(word),
            'simplified': word['simplified'],
            'traditional': word['traditional'],
            'pinyin': word['pinyin'],
            'zhuyin': dragonmapper.transcriptions.pinyin_to_zhuyin(word['pinyin']),
            'meaning': word['meaning'],
            'tts_text': dragonmapper.transcriptions.pinyin_to_zhuyin(word['pinyin']),
            'tts_audio': '',
        })