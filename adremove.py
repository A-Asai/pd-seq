import sys

p = ''
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
                    else:
                        output_file.write(p)
                        p = ''
            else:
                output_file.write(line)

