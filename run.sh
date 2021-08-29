#!/bin/bash

set -ex

mkdir -p build

curl -so build/hsk1.txt https://raw.githubusercontent.com/glxxyz/hskhsk.com/main/data/lists/HSK%20Official%20With%20Definitions%202012%20L1%20freqorder.txt
curl -so build/hsk2.txt https://raw.githubusercontent.com/glxxyz/hskhsk.com/main/data/lists/HSK%20Official%20With%20Definitions%202012%20L2%20freqorder.txt
curl -so build/hsk3.txt https://raw.githubusercontent.com/glxxyz/hskhsk.com/main/data/lists/HSK%20Official%20With%20Definitions%202012%20L3%20freqorder.txt
curl -so build/hsk4.txt https://raw.githubusercontent.com/glxxyz/hskhsk.com/main/data/lists/HSK%20Official%20With%20Definitions%202012%20L4%20freqorder.txt
curl -so build/hsk5.txt https://raw.githubusercontent.com/glxxyz/hskhsk.com/main/data/lists/HSK%20Official%20With%20Definitions%202012%20L5%20freqorder.txt
curl -so build/hsk6.txt https://raw.githubusercontent.com/glxxyz/hskhsk.com/main/data/lists/HSK%20Official%20With%20Definitions%202012%20L6%20freqorder.txt

cat \
    <(echo "# HSK 1") \
    build/hsk1.txt \
    <(echo "# HSK 2") \
    build/hsk2.txt \
    <(echo "# HSK 3") \
    build/hsk3.txt \
    <(echo "# HSK 4") \
    build/hsk4.txt \
    <(echo "# HSK 5") \
    build/hsk5.txt \
    <(echo "# HSK 6") \
    build/hsk6.txt \
    > build/hsk.dirty.txt

python cleanup.py build/hsk.dirty.txt build/hsk.txt
