with open('sample.fasta','r') as f, open('fastq2fasta.csv', 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            line = line[:-14]
            line = line.replace(':','_')
            line += '\t'
            line.strip('>')
        output_file.write(format(line.strip('>')))
