amino = ''
data = []

with open('idamino2.fasta','r') as f, open('aminounique.csv', 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            line = line.replace('\n', '\t')
        if not line.startswith('>'):
            list = [line.strip('\n')]
            data += list
            amino += line
            amino = amino.replace('\n', '\t')
            amino = ''
    else:
        from collections import Counter
        counter = Counter(data)
        for cnt in counter.most_common():
            count = str(cnt)
            count = count.replace(')','\n')
            count = count.strip('(')
            count = count.strip('\'')
            count = count.replace(',','\t')
            count = count.replace('\'\t','\t')
            output_file.write(count)

