with open('sample.fasta','r') as f, open('output.csv', 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            line = line.replace('\n','\t')
            line.strip('>')
        output_file.write(format(line.strip('>')))
