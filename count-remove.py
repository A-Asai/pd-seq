with open('nameaminocount.tabular','r') as f, open('count-remove.csv','w') as output_file:
    for line in f:
            if not line.endswith('-\n'):
                    output_file.write(line)
