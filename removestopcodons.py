import sys

a = ''
b = ''

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as output_file:
    for line in f:
        if line.startswith('>'):
            a += line.replace('\n', '\t')
        else:
            a += '<'
            a += line
            a = a.replace('\n', '<')
            a = a.replace('********', '~')
            a = a.replace('*******', '~')
            a = a.replace('******', '~')
            a = a.replace('*****', '~')
            a = a.replace('****', '~')
            a = a.replace('***', '~')
            a = a.replace('**', '~')
            a = a.replace('<*', '~')
            a = a.replace('*<', '-')
            a += '\t'
            a = a.replace('*\t', '')
            if '~' in a:
                a = ''
            else:
                if '-' in a:
                    if '*' not in a:
                        b = a.replace('\t', '\n')
                        b = b.replace('<', '')
                        output_file.write(b.replace('-', '*'))
                        a = ''
                        b = ''
                    else:
                        a = ''
                else:
                    if '*' in a:
                        a = ''
                    else:
                        b = a.replace('\t', '\n')
                        b = b.replace('<', '')
                        output_file.write(b)
                        a = ''
                        b = ''

