import sys

reverse = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N', '\n': ''}
p = ''
q = ''
head = sys.argv[3]
tail = sys.argv[4]

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            output_file.write(line)
        else:
            if head in line:
                p += line
                if head in p:
                    p = str(p.split(head)[1])
                    if tail in p:
                        p = str(p.split(tail)[0])
                        p += '\n'
                        output_file.write(p)
                        p = ''
                    if tail not in p:
                        output_file.write(p)
                        p = ''
            if head not in line:
                for i in range(0, int(len(line))):
                    lang = line[i:i + 1]
                    if (lang in reverse):
                        q += reverse[lang]
                line.replace(line, q)
                q = q[::-1]
                q += '\n'
            output_file.write(q)
            q = ''

