import sys

with open(sys.argv[1],'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            line = line[:-14]
            line = line.replace(':','_')
            line += '\t'
            line.strip('>')
        output_file.write(format(line.strip('>')))
