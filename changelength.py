import sys

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            output_file.write(line)
        else:
            line = line[0:8]
            line += '\n'
            output_file.write(line)

