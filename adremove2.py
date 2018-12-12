import sys

p = ''
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
            else:
                output_file.write(line)

