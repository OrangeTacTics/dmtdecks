import sys
import json
import csv
import os


CARD_COUNT = int(os.getenv('CARD_COUNT'))


with open(sys.argv[1]) as infile:
    words = json.load(infile)

def words_by_hsk(words, i):
    return [w for w in words if w['hsk'] == i]


for i in range(1, 7):
    with open(f'output/kotoba_{i}.csv', 'w') as outfile:
        fieldnames = [
            'Question',
            'Answers',
            'Comment',
            'Instructions',
            'Render as',
        ]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        for word in words_by_hsk(words, i):
            answers = list({
                word['pinyin'],
                word['pinyin'].replace(' ', ''),
                word['pinyin2'],
                word['pinyin2'].replace(' ', ''),
            })
            writer.writerow({
                'Question': word['simplified'],
                'Answers':  ','.join(answers),
                'Comment': word['meaning'],
                'Instructions': 'Type the reading, Comrade',
                'Render as': 'Image',
            })
