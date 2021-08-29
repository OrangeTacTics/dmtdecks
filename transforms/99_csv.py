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

    for i, word in enumerate(words.values()):
        if i == 100:
            break
        writer.writerow({
            'key': f"{word['simplified']} [{word['pinyin']}]",
            'display': to_display(word),
            'simplified': word['simplified'],
            'traditional': word['traditional'],
            'pinyin': word['pinyin'],
            'meaning': word['meaning'],
            'tts_text': word['traditional'],
            'tts_audio': '',
        })
