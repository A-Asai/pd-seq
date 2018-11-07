import sys

with open(sys.argv[1],'r') as f, open(sys.argv[2],'w') as output_file:
    for line in f:
            if not line.endswith('-\n'):
                    output_file.write(line)
