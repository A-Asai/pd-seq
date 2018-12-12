import sys

reverse = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N', '\n': ''}
p = ''
q = ''
head = sys.argv[3]

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            output_file.write(line)
        else:
            if head in line:
                p += line
                p = str(p.split(head)[1])
                p = p[0:24]
                p += '\n'
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

