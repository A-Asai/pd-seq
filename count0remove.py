with open('nameseqcount.tabular','r') as f, open('count0remove.csv','w') as output_file:
    for line in f:
        if not line.endswith('N\n'):
            output_file.write(line)
