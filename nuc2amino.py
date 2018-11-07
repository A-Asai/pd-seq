import sys

DNA2Protein = {
        'TTT' : 'F', 'TCT' : 'S', 'TAT' : 'Y', 'TGT' : 'C',
        'TTC' : 'F', 'TCC' : 'S', 'TAC' : 'Y', 'TGC' : 'C',
        'TTA' : 'L', 'TCA' : 'S', 'TAA' : '*', 'TGA' : '*',
        'TTG' : 'L', 'TCG' : 'S', 'TAG' : '*', 'TGG' : 'W',
        'CTT' : 'L', 'CCT' : 'P', 'CAT' : 'H', 'CGT' : 'R',
        'CTC' : 'L', 'CCC' : 'P', 'CAC' : 'H', 'CGC' : 'R',
        'CTA' : 'L', 'CCA' : 'P', 'CAA' : 'Q', 'CGA' : 'R',
        'CTG' : 'L', 'CCG' : 'P', 'CAG' : 'Q', 'CGG' : 'R',
        'ATT' : 'I', 'ACT' : 'T', 'AAT' : 'N', 'AGT' : 'S',
        'ATC' : 'I', 'ACC' : 'T', 'AAC' : 'N', 'AGC' : 'S',
        'ATA' : 'I', 'ACA' : 'T', 'AAA' : 'K', 'AGA' : 'R',
        'ATG' : 'M', 'ACG' : 'T', 'AAG' : 'K', 'AGG' : 'R',
        'GTT' : 'V', 'GCT' : 'A', 'GAT' : 'D', 'GGT' : 'G',
        'GTC' : 'V', 'GCC' : 'A', 'GAC' : 'D', 'GGC' : 'G',
        'GTA' : 'V', 'GCA' : 'A', 'GAA' : 'E', 'GGA' : 'G',
        'GTG' : 'V', 'GCG' : 'A', 'GAG' : 'E', 'GGG' : 'G'
}

p = ''

with open(sys.argv[1],'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
            if line.startswith('>'):
                    line = line[:-14]
                    line = line.replace(':','_')
                    line += '\n'
                    output_file.write(line)
            else:
                    for i in range(0, int(len(line)/3)):
                        codon = line[3*i:3*i+3]
                        if (codon in DNA2Protein):
                                p += DNA2Protein[codon]
                        else:
                                break
                    line.replace(line, p)
                    p += '\n'
            output_file.write(p)
            p = ''
