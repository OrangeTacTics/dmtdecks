import sys


infilename = sys.argv[1]
outfilename = sys.argv[2]

with open(infilename) as infile:
    data = infile.read()

data = data.replace('\ufeff', '').replace('\r', '')

with open(outfilename, 'w') as outfile:
    outfile.write(data)
