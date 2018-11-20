import sys

reverse = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N', '\n': ''}
p = ''
head = sys.argv[3]
tail = sys.argv[4]

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            output_file.write(line)
        else:
            for i in range(0, int(len(line))):
                lang = line[i:i + 1]
                if (lang in reverse):
                    p += reverse[lang]
            line.replace(line, p)
            p = p[::-1]
            if head in p:
                p = str(p.split(head)[1])
            if tail in p:
                p = str(p.split(tail)[0])
            p += '\n'
            output_file.write(p)
            p = ''

